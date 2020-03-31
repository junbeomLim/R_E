import cv2
import time
from datetime import datetime


cameraNum = 0
CAM_width = 640
CAM_height = 480

time = 0

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_height)

masking_state = False
tracking_box = False
once = True
track = cv2.TrackerCSRT_create()
first_count = True


def roiWindow(img):
    global masking_state
    global tracking_box
    # ROI 구하기
    rect = cv2.selectROI("SelectWindow", img, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("SelectWindow")

    # Tracker 설정하기
    track.init(img, rect)
    tracking_box = True
    masking_state = False


def current2Dvelocity(box, currentTime, detaltrate=500):
    global first_count
    millis = 0
    if first_count:
        millis = currentTime
        return


current_milli_time = lambda: int(round(time.time() * 1000))

while True:
    ret, frame = capture.read(cameraNum)
    if masking_state:
        cv2.destroyAllWindows()
        roiWindow(frame)

    if tracking_box:
        sucess, box = track.update(frame)

        left, top, w, h = [int(v) for v in box]

        cv2.rectangle(
            frame,
            pt1=(left, top),
            pt2=(left + w, top + h),
            color=(255, 255, 255),
            thickness=3,
        )

    cv2.imshow("Norm", frame)

    """
    if cv2.waitKey(1) == ord("q"):
        break
    """
    key = cv2.waitKey(1)
    if key == ord("a"):
        print("a")
        masking_state = True
    elif key == ord("q"):
        print("q")
        break

capture.release()
cv2.destroyAllWindows()
