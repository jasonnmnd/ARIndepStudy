import numpy as np
import cv2
import skimage
import os

def getPictureDetails():
    rootdir = "/Users/jasondong/Desktop/AR/dataFolder"
    for directory in os.listdir(rootdir):
        dirPath = os.path.join(rootdir, directory)
        filePath = os.path.join(dirPath, "position1.png")
        img_clr = cv2.imread(filePath)
        cv2.imshow('image', img_clr)

        cropped_image = img_clr[210:1200, 0:1200]
        cv2.imshow("cropped", cropped_image)
        # cv2.waitKey(0)
        # Calculate brightness
        brightness = (np.mean(cropped_image)) / 255

        # Calculate contrast
        contrast = cropped_image.std()

        # Calculate entropy
        entropy = skimage.measure.shannon_entropy(cropped_image)

        # Calculate variance of the laplacian
        laplacian = cv2.Laplacian(cropped_image, cv2.CV_64F).var()

        # Calculate corners
        fast = cv2.FastFeatureDetector_create()
        kp = fast.detect(img_clr, None)
        corners = len(kp)

        print("Image - Brightness: " + str(brightness) + " Contrast: " + str(contrast) + " Entropy: " + str(entropy) + " Laplacian: " + str(laplacian) + " Corners: " + str(corners))

def parseData():
    rootdir = "/Users/jasondong/Desktop/AR/dataFolder"
    positionInWorldSpace = []
    distanceFromCameraToObject = []
    changeInViewingAngle = []
    magnitudeOfDrift = []

    for directory in os.listdir(rootdir):
        dirPath = os.path.join(rootdir, directory)
        # checking if it is a file
        filePath = os.path.join(dirPath, "position1.txt")
        if os.path.isfile(filePath):
            with open(filePath, 'r') as f:
                dataArr = []
                dataArr.append(f.read())
                for data in dataArr:
                    splitArr = data.split("\n")
                    positionInWorldSpace.append(splitArr[0])
                    distanceFromCameraToObject.append(splitArr[1])
                    changeInViewingAngle.append(splitArr[2])
                    magnitudeOfDrift.append(splitArr[3])

    print("Position in world space: " + str(positionInWorldSpace))
    print("Distance from Camera to Object: " + str(distanceFromCameraToObject))
    print("Change in viewing angle: " + str(changeInViewingAngle))
    print("Magnitude of drift: " + str(magnitudeOfDrift))

    userInputArr = []
    for directory in os.listdir(rootdir):
        dirPath = os.path.join(rootdir, directory)
        filePath = os.path.join(dirPath, "userInput.txt")
        if (os.path.isfile(filePath)):
            with open(filePath, 'r') as f:
                userInputArr.append(f.read())



if __name__ == '__main__':
    getPictureDetails()
    #parseData()

