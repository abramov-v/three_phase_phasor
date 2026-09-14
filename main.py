import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PHASES = {"A": 0, "B": -2 * np.pi / 3, "C": 2 * np.pi / 3}
AMPLITUDE = 1.0
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
labels = {}
for phase in PHASES:
    vector, = ax.plot([], [], linewidth=2, marker="o")
    label = ax.text(0, 0, phase, fontsize=12, fontweight="bold")
    vectors[phase] = vector
    labels[phase] = label

angle_text = ax.text(0.02, 0.98, "", transform=ax.transAxes, verticalalignment="top")


def update(frame):
    angle = frame * STEP
    for phase, phase_shift in PHASES.items():
        theta = angle + phase_shift
        x = AMPLITUDE * np.cos(theta)
        y = AMPLITUDE * np.sin(theta)
        vectors[phase].set_data([0, x], [0, y])
        labels[phase].set_position((x * 1.08, y * 1.08))

    angle_text.set_text(f"Angle: {np.degrees(angle) % 360:.1f}°")
    return (*vectors.values(), *labels.values(), angle_text)


animation = FuncAnimation(fig, update, frames=360, interval=35, blit=True)
plt.show()


if __name__ == "__main__":
    pass
