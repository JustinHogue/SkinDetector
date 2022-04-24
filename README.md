# SkinDetector
Skin detection using HSV color space in Python with OpenCV.

# The procedure
First of all, we change the BGR image value into its equivalent HSV value. After that, we use two filters. The first one detects the lighter skin and the second one detects the darker skin. We then combine them by using a bitwise or on the frame.
