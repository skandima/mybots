import pybullet as p
import time
import pybullet_data


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


p.setGravity(0,0,-9.8) #add gravity
planeId = p.loadURDF("plane.urdf") #add floor
robotId = p.loadURDF("body.urdf") #simulate robot in body.urdf
p.loadSDF("world.sdf")

for i in range(1000):
    start_time = time.time()  # Start the timer for this iteration
    p.stepSimulation()
    iteration_duration = time.time() - start_time  # Time elapsed in this iteration
    # Print the loop index (i) and the time it took for this iteration
    print(f"Iteration {i+1}: Time taken = {iteration_duration:.6f} seconds")
    time.sleep(1/60.0)

p.disconnect()