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

        kernel = np.ones((3, 3), np.uint8)
        img = cv2.erode(img, kernel, iterations=1)

        img_cie_lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
        img_y_cr_cb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        
        # We only keep the pixels that respect certains criterias such as R > B, 77 <= Cb <= 133, 127 <= Cr <= 175
        # and many others that can be found on the README of the repo
        rows,cols,_ = img.shape
        for i in range(rows):
            for j in range(cols):
                U, V = img_yuv[i,j][1], img_yuv[i,j][2]
                B, G, R = img[i,j][0], img[i,j][1], img[i,j][2]
                S = img_hsv[i,j][1]
                Y, Cr, Cb = img_y_cr_cb[i,j][0], img_y_cr_cb[i,j][1], img_y_cr_cb[i,j][2]
                L, a, b = img_cie_lab[i,j][0], img_cie_lab[i,j][1], img_cie_lab[i,j][2]
                I = 0.596*R - 0.275*G - 0.322*B
                Q = 128 + (0.21153661 * R) + (-0.52273617 * G) + (0.31119955 * B)
                if not(121.5 < Q and 80 < Y < 242 and 77 <= Cb <= 133 and 127 <= Cr <= 175 and 26 < S < 178 and R > G and 136 < V < 200 and
                80 < U < 130 and R > B and abs(R - G) > 15 and 14 <= I <= 90 and 100 < L and 134 < a and 115 < b < 177):
                    img[i,j] = [0,0,0]

        # We filter the image after smoothing it
        blurred_frame = cv2.GaussianBlur(img, (3, 3), 0)
        skin = cv2.inRange(blurred_frame, (20, 40, 95), (255, 255, 255))
        
        # We treat the holes in the filtered frame
        kernel = np.ones((3, 3), np.uint8)
        opening = cv2.morphologyEx(skin, cv2.MORPH_OPEN, kernel)
        kernel = np.ones((4, 4), np.uint8)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

        return closing
        