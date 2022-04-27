# SkinDetector
Skin detection using multiples color spaces in Python with OpenCV.

# Flowchart of the proposed system
![alt text](https://scontent.fymy1-1.fna.fbcdn.net/v/t1.15752-9/278692184_396057225488342_3718144922394996355_n.png?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_ohc=uinK-8jVldcAX8_ZKGP&_nc_oc=AQk8jgQ_sI3tZjyWUHQuSD-waWXTufyip8LDqaYnu1LwcLkqwP5728pgKWhra5Nyd68&_nc_ht=scontent.fymy1-1.fna&oh=03_AVJ2U1WAf5gSCguXkfKlxIpeg3_7BW21szGho2nhwHrMjQ&oe=628D1E57)

# Description of the procedure
OpenCV reads images in the BGR color space. Therefore, we start by treating each pixel with the threshold in the BGR color space. It's pretty simple, we only want to keep the pixels that respect the following conditions R > G and R > B
--- | H | S | V |
--- | --- | --- | --- |
Min | 335/0 | 0.1  |  40 |
Max | 360/33 | 0.7  | 255 |

## References
<a id="1">[1]</a> 
Patil, Prajakta M., and Y. M. Patil, "Robust Skin Colour Detection and Tracking Algorithm", 
International Journal of Engineering Research and Technology Vol. 1. No.8 (October-2012), ISSN: 2278-0181 (2012).

<a id="2">[2]</a> 
Phung, S. L., Bouzerdoum, A., And Chai, D: “A novel skin color model in ycbcr color space and its
application to human face detection” , IEEE International Conference on Image Processing (ICIP’
2002), vol. 1, 289-292(2002).

<a id="3">[3]</a>
Alejo, D. A. C. , & Gallegos Funes, F. J. (2017). Detection and Tracking of the Regions of Skin Using the Technique HS-ab. In (Ed.), Biomimetic Prosthetics. IntechOpen. https://doi.org/10.5772/intechopen.70027
