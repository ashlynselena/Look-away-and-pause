
# Look Away and Pause


This project was developed in 2017 as a fun side-project to be able to pause video feed when people are not looking at the screen. The use case this was developed for was an exhibition event with people passing by an interactive video that needed to restart from the beginning when people are watching and pause when no one was.

This uses the Haar Cascade FrontalFace detector from openCV to detect faces facing forward. When no faces are deteted the video is paused, and the first face detected after a pause restarts the video from the beginning.

## Pre-requisites
- python
- opencv
- A connected webcam

## Usage
```
python main.py
```
