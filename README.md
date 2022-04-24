# SkinDetector
Skin detection using HSV color space in Python with OpenCV.

# The procedure
First of all, we change the BGR image into its equivalent HSV image. After that, we use a filter with the following values:
--- | H | S | V |
--- | --- | --- | --- |
Min | 110 | 10  |  50 |
Max | 170 | 70  | 255 |

# Examples
In the following images, you will see the skin detection results of HSV color space threshold for the first draft of the code.
![alt text](https://scontent-lga3-1.xx.fbcdn.net/v/t1.15752-9/278768520_2074264022778023_7813106729143618220_n.png?_nc_cat=111&ccb=1-5&_nc_sid=ae9488&_nc_ohc=Sy1G2qaRrncAX9nXcWz&_nc_ht=scontent-lga3-1.xx&oh=03_AVKhUyrWiBVlxC5yZcwRF6WKZ5d8FQyrsY5BXE-Y2gca8g&oe=628C0F58)
![alt text](https://media.discordapp.net/attachments/575755454919999489/967889419501731930/unknown.png?width=754&height=473)
![alt text](https://scontent-lga3-1.xx.fbcdn.net/v/t1.15752-9/278558459_1331790350661069_7625032366075354887_n.png?_nc_cat=109&ccb=1-5&_nc_sid=ae9488&_nc_ohc=dJ4hJ_RLim0AX8X3xni&_nc_ht=scontent-lga3-1.xx&oh=03_AVKYPEu6XW3Pn7aU7XFv9Y3ZtYyqhnyIP7TzmroWBc395g&oe=6289A001)

