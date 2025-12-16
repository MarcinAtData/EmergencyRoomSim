
import matplotlib.pyplot as plt
import numpy as np


def plot_heatmap(doctors, rates, heatmap):
    plt.figure(figsize=(10, 6))
    plt.imshow(heatmap, cmap="turbo", interpolation="nearest")
    plt.colorbar(label="Average Waiting Time (min)")

    plt.xticks(range(len(rates)), [f"1/{round(1/r, 1)}" for r in rates])
    plt.yticks(range(len(doctors)), doctors)

    plt.xlabel("Patient Arrival Rate (patients per minute)")
    plt.ylabel("Number of Doctors")
    plt.title("ER Performance: Average Waiting Time")

    for i in range(len(doctors)):
        for j in range(len(rates)):
            plt.text(j, i, f"{heatmap[i,j]:.1f}",
                     ha="center", va="center", color="white", fontsize=8)

    plt.tight_layout()
    plt.show()


def plot_line_chart(doctors, rates, heatmap):
    plt.figure(figsize=(10,6))

    for j, rate in enumerate(rates):
        plt.plot(doctors, heatmap[:, j], marker='o', label=f"Arrival 1/{round(1/rate)}")

    plt.xlabel("Number of Doctors")
    plt.ylabel("Average Waiting Time (min)")
    plt.title("Waiting Time vs Number of Doctors")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_wait_vs_arrival(doctors, rates, heatmap):
    plt.figure(figsize=(10,6))

    for i, d in enumerate(doctors):
        plt.plot([1/r for r in rates], heatmap[i], marker='o', label=f"{d} doctors")

    plt.xlabel("Patients per Minute")
    plt.ylabel("Average Waiting Time (min)")
    plt.title("Waiting Time vs Arrival Rate")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_surface(doctors, rates, heatmap):
    X, Y = np.meshgrid([1/r for r in rates], doctors)
    Z = heatmap

    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap="turbo")
    fig.colorbar(surf, shrink=0.5, aspect=5)

    ax.set_xlabel("Patients per Minute")
    ax.set_ylabel("Number of Doctors")
    ax.set_zlabel("Average Waiting Time (min)")
    ax.set_title("3D View: ER System Performance")

    plt.show()


def plot_contour(doctors, rates, heatmap):
    X, Y = np.meshgrid([1/r for r in rates], doctors)

    plt.figure(figsize=(10,7))
    contour = plt.contourf(X, Y, heatmap, levels=20, cmap="turbo")
    plt.colorbar(contour)

    plt.xlabel("Patients per Minute")
    plt.ylabel("Number of Doctors")
    plt.title("Contour Plot: ER Waiting Time")

    plt.show()


