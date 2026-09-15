import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PHASES = {"A": 0, "B": -2 * np.pi / 3, "C": 2 * np.pi / 3}
AMPLITUDE = 1.0
CURRENT_AMPLITUDE = 0.7
CURRENT_LAG = np.deg2rad(30)
STEP = np.pi / 50

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_aspect("equal")
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.3)
ax.axhline(0, linewidth=0.8)
ax.axvline(0, linewidth=0.8)
ax.grid(True, alpha=0.2)
# ax.set_xlabel("Real")
# ax.set_ylabel("Imaginary")
ax.set_title("Three-Phase Phasor Rotation")

circle = plt.Circle((0, 0), AMPLITUDE, fill=False, linestyle="--", alpha=0.5)
ax.add_patch(circle)

vectors = {}
current_vectors = {}
labels = {}
current_labels = {}

for phase in PHASES:
    vector, = ax.plot([], [], linewidth=2, marker="o")
    current_vector, = ax.plot([], [], linewidth=2, linestyle="--", marker="o")

    label = ax.text(0, 0, phase, fontsize=12, fontweight="bold")
    current_label = ax.text(0, 0, f"I{phase}", fontsize=10)

    vectors[phase] = vector
    current_vectors[phase] = current_vector
    labels[phase] = label
    current_labels[phase] = current_label

angle_text = ax.text(0.02, 0.98, "", transform=ax.transAxes, verticalalignment="top")


def update(frame):
    angle = frame * STEP

    for phase, phase_shift in PHASES.items():
        voltage_theta = angle + phase_shift
        current_theta = voltage_theta - CURRENT_LAG

        voltage_x = AMPLITUDE * np.cos(voltage_theta)
        voltage_y = AMPLITUDE * np.sin(voltage_theta)
        current_x = CURRENT_AMPLITUDE * np.cos(current_theta)
        current_y = CURRENT_AMPLITUDE * np.sin(current_theta)

        vectors[phase].set_data([0, voltage_x], [0, voltage_y])
        current_vectors[phase].set_data([0, current_x], [0, current_y])

        labels[phase].set_position((voltage_x * 1.08, voltage_y * 1.08))
        current_labels[phase].set_position((current_x * 1.08, current_y * 1.08))

    angle_text.set_text(f"Angle: {np.degrees(angle) % 360:.1f}°")

    return (
        *vectors.values(),
        *current_vectors.values(),
        *labels.values(),
        *current_labels.values(),
        angle_text,
    )


animation = FuncAnimation(fig, update, frames=360, interval=35, blit=True)
plt.show()


if __name__ == "__main__":
    pass
