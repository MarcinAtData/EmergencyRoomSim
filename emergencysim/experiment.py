import simpy
import random
import statistics
import numpy as np


def patient(env, er, triage, stats):
    arrival = env.now
    priority = stats["TRIAGE_LEVELS"][triage]

    with er.request(priority=priority) as req:
        result = yield req | env.timeout(stats["MAX_WAIT"][triage])

        if req not in result:
            stats["leaving_count"] += 1
            return

        wait = env.now - arrival
        stats["waiting_times"].append(wait)

        yield env.timeout(stats["TREAT_TIME"][triage]())
        stats["served_count"] += 1


def arrivals(env, er, arrival_rate, stats):
    i = 0
    while True:
        interarrival = random.expovariate(arrival_rate)
        yield env.timeout(interarrival)

        i += 1
        triage = random.choices(
            list(stats["TRIAGE_PROB"].keys()),
            list(stats["TRIAGE_PROB"].values())
        )[0]

        env.process(patient(env, er, triage, stats))


def run_er_simulation(num_doctors, arrival_rate, sim_time=8*60, random_seed=42):

    random.seed(random_seed)

    # Parameters
    TRIAGE_PROB = {"Critical": 0.1, "Serious": 0.3, "Mild": 0.6}
    TRIAGE_LEVELS = {"Critical": 0, "Serious": 1, "Mild": 2}
    MAX_WAIT = {"Critical": 200, "Serious": 60, "Mild": 30}
    TREAT_TIME = {
        "Critical": lambda: random.uniform(20, 40),
        "Serious":  lambda: random.uniform(15, 30),
        "Mild":     lambda: random.uniform(5, 15)
    }

    # Statistics
    stats = {
        "waiting_times": [],
        "leaving_count": 0,
        "served_count": 0,
        "TRIAGE_PROB": TRIAGE_PROB,
        "TRIAGE_LEVELS": TRIAGE_LEVELS,
        "MAX_WAIT": MAX_WAIT,
        "TREAT_TIME": TREAT_TIME,
    }

    # Environment
    env = simpy.Environment()
    er = simpy.PriorityResource(env, capacity=num_doctors)

    env.process(arrivals(env, er, arrival_rate, stats))
    env.run(until=sim_time)

    # Results
    avg_wait = (
        statistics.mean(stats["waiting_times"])
        if stats["waiting_times"]
        else float("inf")
    )

    total_patients = stats["served_count"] + stats["leaving_count"]
    percent_leaving = (
        stats["leaving_count"] / total_patients * 100
        if total_patients > 0
        else 0
    )

    return avg_wait, percent_leaving, stats["served_count"]


def run_experiments():

    doctor_options = [1, 2, 3, 4, 5, 6]
    arrival_rates = [1/10, 1/7, 1/5, 1/4, 1/3]   # patients per minute

    heatmap_wait = np.zeros((len(doctor_options), len(arrival_rates)))

    print("Running simulations...\n")

    for i, docs in enumerate(doctor_options):
        for j, rate in enumerate(arrival_rates):
            avg_wait, pct_leave, served = run_er_simulation(
                docs,
                rate,
                sim_time=12*60
            )
            heatmap_wait[i, j] = avg_wait
            print(
                f"Doctors={docs}, ArrivalRate=1/{1/rate:.1f} "
                f"→ wait={avg_wait:.1f} min, leave={pct_leave:.1f}%"
            )

    return doctor_options, arrival_rates, heatmap_wait