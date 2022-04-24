import cv2
import numpy as np

class VisionDetectionService:
    def __init__(self) -> None:
        """
        Constructor for class VisionDetectionService
        """
        pass

    def analyze_frame_for_skin(self, frame: np.ndarray) -> np.ndarray:
        """
        Analyzes a frame in order to detect the human skin
        :param frame: The frame to analyze
        :return: The new frame with detected skin only
        """
        # Adding a border to detect the skin on the edge
        borderType = cv2.BORDER_CONSTANT
        top = int(0.006 * frame.shape[0])  # shape[0] = rows
        bottom = top
        left = int(0.002 * frame.shape[1])  # shape[1] = cols
        right = left
        border_color = (0, 0, 0)
        img = cv2.copyMakeBorder(frame, top, bottom, left, right, borderType, None, border_color)

        # We transfer into HSV
        frame_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # We filter the image after smoothing it
        blurred_frame = cv2.medianBlur(frame_hsv, 7)
        lighter_skin = cv2.inRange(blurred_frame, (115, 10, 50), (170, 70, 255))
        darker_skin = cv2.inRange(blurred_frame, (5, 40, 100), (17, 130, 255))
        skin = cv2.bitwise_or(lighter_skin, darker_skin)
        
        # We treat the holes in the filtered frame
        kernel = np.ones((3, 3), np.uint8)
        opening = cv2.morphologyEx(skin, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

        return closing
