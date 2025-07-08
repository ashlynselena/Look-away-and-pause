import datetime as dt
import logging as log
import sys
import tkinter as tk
from time import sleep

import cv2


def set_haarcascade_face_detector():
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    return faceCascade


def get_screen_dims():
    # Get screen resolution
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()

    return screen_width, screen_height


def main():
    faceCascade = set_haarcascade_face_detector()

    screen_width, screen_height = get_screen_dims()

    # Set dimensions of camera frame
    cam_h, cam_w = int(0.1 * screen_height), int(0.1 * screen_width)

    video_capture = cv2.VideoCapture("fishies.mp4")
    camera_capture = cv2.VideoCapture(0)

    while True:
        if not camera_capture.isOpened():
            print("Unable to load camera.")
            sleep(5)
            pass

        # Read frame from camera
        ret, cam_frame = camera_capture.read()

        if not ret:
            print("Camera feed interrupted")
            sleep(5)
            continue

        gray = cv2.cvtColor(cam_frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = faceCascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        if len(faces) != 0:
            # Draw a rectangle around the faces
            for x, y, w, h in faces:
                cv2.rectangle(cam_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            ## read frame of video
            ret2, video_frame = video_capture.read()
            # If video is over
            if ret2 == False:
                break
            video_frame = cv2.resize(video_frame, (screen_width, screen_height))

        # Resize PiP frame to smaller size
        pip_small = cv2.resize(cam_frame, (cam_w, cam_h))

        # Overlay PiP frame onto main frame
        video_frame[10 : 10 + cam_h, 10 : 10 + cam_w] = pip_small

        cv2.imshow("frame", video_frame)
        if cv2.waitKey(3) & 0xFF == ord("q"):
            break

    # When everything is done, release the capture
    camera_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
