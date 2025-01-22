import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


p.setGravity(0,0,-9.8) #add gravity
planeId = p.loadURDF("plane.urdf") #add floor
robotId = p.loadURDF("body.urdf") #simulate robot in body.urdf
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

# Create a numpy vector filled with zeros
frontLegSensorValues = np.zeros(10000)  # Assuming 10000 iterations in the loop

# Print the numpy vector and exit
print(frontLegSensorValues)


# Run the simulation loop
for i in range(1000):
    start_time = time.time()  # Start the timer for this iteration
    p.stepSimulation()  # Step the simulation

    # Store the touch sensor value for FrontLeg in the array
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # Calculate and print the time elapsed for this iteration
    iteration_duration = time.time() - start_time
    print(f"Iteration {i + 1}: Time taken = {iteration_duration:.6f} seconds")

    time.sleep(1 / 60.0)  # Sleep to control the simulation speed

# Print the stored sensor values after the simulation
print(frontLegSensorValues)



p.disconnect()