import pybullet as p
import time

physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")

for i in range(1000):
    start_time = time.time()  # Start the timer for this iteration
    p.stepSimulation()
    iteration_duration = time.time() - start_time  # Time elapsed in this iteration
    # Print the loop index (i) and the time it took for this iteration
    print(f"Iteration {i+1}: Time taken = {iteration_duration:.6f} seconds")
    time.sleep(1/60.0)

p.disconnect()