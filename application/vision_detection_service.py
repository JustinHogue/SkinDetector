from typing import List
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
        img = cv2.dilate(img, kernel, iterations=1)
        
        # We only keep the pixels that respect the following conditions:
        # R > 95 and G > 40 and B > 20 and R > B and R/G > 1.185 and (G/B - R/G) <= -0.0905 and Y > 80 
        # where Y = 0.299*R + 0.287*G + 0.11*B
        rows,cols,_ = img.shape
        for i in range(rows):
            for j in range(cols):
                k = img[i,j]
                B = k[0]
                G = k[1]
                R = k[2]
                H, S, V = self._rgb_to_hsv(R, G, B)
                Y = (0.299 * R) + (0.587 * G) + (0.114 * B)
                I = 0.596*R - 0.275*G - 0.322*B
                Q = 128 + (0.21153661 * R) + (-0.52273617 * G) + (0.31119955 * B)
                Cb = 128 - 0.169*R - 0.331*G + 0.5*B
                Cr = 128 + 0.5*R - 0.419*G - 0.081*B
                x = 0.431*R + 0.342*G + 0.178*B
                y = -0.222*R + 0.707*G + 0.071*B
                a = 17.5*(((1.02*x)-y)/(y**0.5))
                if not(121.5 < Q and 80 < Y < 242 and 77 <= Cb <= 127 and 133 <= Cr <= 173 and 0.1 < S < 0.7 and V > 40 and
                R > G and R > B and abs(R - G) > 15 and 142 < a and (0 < H < 33 or 335 < H < 360)):
                    img[i,j] = [0,0,0]

        # We filter the image after smoothing it
        blurred_frame = cv2.GaussianBlur(img, (3, 3), 0)
        skin = cv2.inRange(blurred_frame, (20, 40, 95), (255, 255, 255))
        
        # We treat the holes in the filtered frame
        kernel = np.ones((3, 3), np.uint8)
        opening = cv2.morphologyEx(skin, cv2.MORPH_OPEN, kernel)

        return opening

    def _rgb_to_hsv(self, r, g, b):
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        cmax = max(r, g, b)
        cmin = min(r, g, b)
        diff = cmax-cmin
        if cmax == cmin:
            h = 0
        elif cmax == r:
            h = (60 * ((g - b) / diff) + 360) % 360
        elif cmax == g:
            h = (60 * ((b - r) / diff) + 120) % 360
        elif cmax == b:
            h = (60 * ((r - g) / diff) + 240) % 360
        if cmax == 0:
            s = 0
        else:
            s = (diff / cmax)
        v = cmax * 100
        return h, s, v
        