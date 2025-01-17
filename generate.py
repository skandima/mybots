import pyrosim.pyrosim as pyrosim

def Create_World():
    # Start the SDF file
    pyrosim.Start_SDF("world.sdf")
    #Add cube
    pyrosim.Send_Cube(name="Box", pos=[-3.0,3.0,0.5] , size=[1.0,1.0,1.0])
    # End the SDF file
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[0,0,0.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0.5,0,1.0])
    pyrosim.Send_Cube(name="Link1", pos=[0.5,0,0.5] , size=[1.0,1.0,1.0])
    pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [1,0,0.0])
    pyrosim.Send_Cube(name="Link2", pos=[0.5,0,-0.5] , size=[1.0,1.0,1.0])
    pyrosim.End()

if __name__ == "__main__":
    Create_World()
    Create_Robot()
