from matplotlib import pyplot as plt
import numpy as np
import cv2

def getVideoInfo(vidCapture): 
    """
    Prints out the video information
    such as FPS, total frame count, 
    frame width, and frame height. 
    Return(s): FPS, total frame count, 
    frame width, and frame height. 
    """
    fps = vidCapture.get(5)
    frameCount = vidCapture.get(7)
    frameWidth = int(vidCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(vidCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print("Frames per second : {}".format(fps), 'FPS')
    print("Frame Count : {}".format(frameCount))
    print("Frame Width : {}".format(frameWidth))
    print("Frame Height : {}".format(frameHeight))
    
    return fps, frameCount, frameWidth, frameHeight;

def getFrames(vidCapture, inputFrameCount):
    """
    Takes the individual frames of the 
    input video and stores them into
    a list. 
    Return(s): Array of input video frames
    """
    inputFrames = []
    idx = 0
    ret = True
    while((idx < inputFrameCount) and ret):
        ret, frame = vidCapture.read()         
        inputFrames.append(frame)
        idx = idx + 1
        
    vidCapture.release()
    return inputFrames;

def generateVideo(markedFrames, fps, size, outputPath):
    """
    Turns the array of images with the found
    line marking contours drawn on into 
    a video file. In this implementation, 
    the output file format is an mp4. 
    """
    out = cv2.VideoWriter(outputPath, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(markedFrames)):
        out.write(markedFrames[i])
        
    out.release()