from djitellopy import tello
from time import sleep
import cv2
import KeyBoard

def getInput():
    left_right, front_back, up_down, clock_counter = 0,0,0,0
    
    if KeyBoard.getKey("a"): left_right = -10
    if KeyBoard.getKey("d"): left_right = 30
    if KeyBoard.getKey("w"): front_back = 30
    if KeyBoard.getKey("s"): front_back = -30

    if KeyBoard.getKey("k"): up_down = -10
    if KeyBoard.getKey("l"): up_down = 30
    if KeyBoard.getKey("i"): clock_counter = 30
    if KeyBoard.getKey("o"): clock_counter = -30

    if KeyBoard.getKey("UP"): drone.takeoff()
    if KeyBoard.getKey("DOWN"): drone.land()

    return [left_right, front_back, up_down, clock_counter]

def video_stream():
    image = drone.get_frame_read().frame
    image = cv2.resize(image, (360, 240))
    cv2.imshw("Image", image)
    cv2.waitKey(1)

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

KeyBoard.init()
drone.streamon()

while True:
    video_stream()
    results = getInput()
    drone.send_rc_control(results[0],results[1],results[2],results[3])
    sleep(1)