import matplotlib.pyplot as plt
import numpy as np

# Load the sensor values from the saved .npy files
front_leg_values = np.load("data/frontLegSensorValues.npy")
torso_values = np.load("data/torsoSensorValues.npy")

# Plot the sensor values
plt.plot(front_leg_values, label="FrontLeg Sensor", linewidth = 3)
plt.plot(torso_values, label="Torso Sensor")

# Add labels and legend
plt.xlabel("Time (Iterations)")
plt.ylabel("Sensor Value")
plt.title("Touch Sensor Values for FrontLeg and Torso")
plt.legend()

# Display the plot
plt.show()
