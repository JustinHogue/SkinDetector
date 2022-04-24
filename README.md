# SkinDetector
Skin detection using HSV color space in Python with OpenCV.

# The procedure
First of all, we change the BGR image into its equivalent HSV image. After that, we use a filter with the following values:
--- | H | S | V |
--- | --- | --- | --- |
Min | 110 | 10  |  50 |
Max | 170 | 70  | 255 |
