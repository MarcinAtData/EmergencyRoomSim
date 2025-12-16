
import emergencysim.visualization as viz

from emergencysim.experiment import run_experiments

if __name__ == "__main__":

    doctors, rates, heatmap = run_experiments()

    viz.plot_heatmap(doctors, rates, heatmap)
    viz.plot_line_chart(doctors, rates, heatmap)
    viz.plot_wait_vs_arrival(doctors, rates, heatmap)
    viz.plot_surface(doctors, rates, heatmap)
    viz.plot_contour(doctors, rates, heatmap)



