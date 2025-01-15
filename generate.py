import pyrosim.pyrosim as pyrosim

# Start the SDF file
pyrosim.Start_SDF("boxes.sdf")

# Initial dimensions
initial_length = 1.0
initial_width = 1.0
initial_height = 1.0

# Loop over columns (x-axis)
for col in range(5):  # Iterate over 5 columns
    x = col * initial_length  # Position along x-axis

    # Loop over rows (y-axis)
    for row in range(5):  # Iterate over 5 rows
        y = row * initial_width  # Position along y-axis

        # Reset dimensions for each column-row stack
        length = initial_length
        width = initial_width
        height = initial_height
        z = height / 2  # Start at ground level for this column-row stack

        # Stack 10 cubes vertically in this column-row
        for layer in range(10):  # 10 cubes per column-row stack
            # Send cube to pyrosim
            pyrosim.Send_Cube(
                name=f"Box_C{col+1}_R{row+1}_L{layer+1}",
                pos=[x, y, z],
                size=[length, width, height]
            )

            # Update z for the next cube in the stack
            z += height

            # Reduce dimensions by 10% for the next cube in this stack
            length *= 0.9
            width *= 0.9
            height *= 0.9

# End the SDF file
pyrosim.End()
