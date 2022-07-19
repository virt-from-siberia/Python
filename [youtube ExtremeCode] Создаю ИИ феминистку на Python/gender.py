import cv2
import math

faceProto = "./data/opencv_face_detector.pbtxt"
faceModel = "./data/opencv_face_detector_uint8.pb"
genderProto = "./data/gender_deploy.prototxt"
genderModel = "./data/gender_net.caffemodel"

genderList = ["male", "female"]

faceNet = cv2.dnn.readNet(faceModel, faceProto)
genderNet = cv2.ann.readNet(genderModel, genderProto)

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
