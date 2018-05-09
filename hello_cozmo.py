'''Hello World'''
import cozmo
from cozmo.util import distance_mm, speed_mmps
from cozmo.util import degrees

def cozmo_program(robot: cozmo.robot.Robot):
        
        count=1
        while count==1:
            robot.say_text("Hello").wait_for_completed()
            for a in range(2):
                robot.drive_straight(distance_mm(100), speed_mmps(5000)).wait_for_completed()

            lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
            cubes = robot.world.wait_until_observe_num_objects(1, object_type=cozmo.objects.LightCube, timeout=15)
            lookaround.stop()
            if len(cubes)>0:
                robot.pickup_object(cubes[0]).wait_for_completed()

            robot.turn_in_place(degrees(90)).wait_for_completed()
            anim = robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin)
            anim.wait_for_completed()

cozmo.run_program(cozmo_program)

'''source: http://cozmosdk.anki.com/docs/tutorial-beginner.html '''
