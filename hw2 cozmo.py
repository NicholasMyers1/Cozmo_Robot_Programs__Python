import cozmo
from cozmo.util import distance_mm, speed_mmps
from cozmo.util import degrees

def cozmo_program(robot: cozmo.robot.Robot):

            robot.say_text("Hello, Nick programmed me.").wait_for_completed()
            robot.say_text("Driving in a line.").wait_for_completed()
            robot.drive_straight(distance_mm(250), speed_mmps(5000)).wait_for_completed()
                
            robot.say_text("Driving in a triangle.").wait_for_completed()
            for num in range(0,4):
                            robot.drive_straight(distance_mm(250), speed_mmps(5000)).wait_for_completed()
                            robot.turn_in_place(degrees(120)).wait_for_completed()
                    
            robot.say_text("Driving in a square.").wait_for_completed()
            for num in range(0,5):
                            robot.drive_straight(distance_mm(250), speed_mmps(5000)).wait_for_completed()
                            robot.turn_in_place(degrees(90)).wait_for_completed()

            robot.say_text("Driving in a circle.").wait_for_completed()
            for num in range(0,36):
                            robot.drive_straight(distance_mm(10), speed_mmps(5000)).wait_for_completed()
                            robot.turn_in_place(degrees(10)).wait_for_completed()

            robot.say_text("Success!").wait_for_completed()
cozmo.run_program(cozmo_program)

'''source: http://cozmosdk.anki.com/docs/tutorial-beginner.html '''
