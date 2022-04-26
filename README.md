# SkinDetector
Skin detection using multiples color spaces in Python with OpenCV.

# The procedure
First of all, we change the BGR image into its equivalent HSV image. After that, we use a filter with the following values:
--- | H | S | V |
--- | --- | --- | --- |
Min | 335/0 | 0.1  |  40 |
Max | 360/33 | 0.7  | 255 |

# Flowchart of the proposed system
![alt text](https://scontent.fymy1-1.fna.fbcdn.net/v/t1.15752-9/278692184_396057225488342_3718144922394996355_n.png?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_ohc=uinK-8jVldcAX8_ZKGP&_nc_oc=AQk8jgQ_sI3tZjyWUHQuSD-waWXTufyip8LDqaYnu1LwcLkqwP5728pgKWhra5Nyd68&_nc_ht=scontent.fymy1-1.fna&oh=03_AVJ2U1WAf5gSCguXkfKlxIpeg3_7BW21szGho2nhwHrMjQ&oe=628D1E57)


