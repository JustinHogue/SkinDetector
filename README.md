# SkinDetector
Skin detection using multiples color spaces in Python with OpenCV.

# Flowchart of the proposed system
![alt text](https://media.discordapp.net/attachments/575755454919999489/968616064072179863/unknown.png?width=432&height=473)

# Description of the procedure
OpenCV reads images in the BGR color space. Therefore, we start by treating each pixel with the threshold in the BGR color space. For the space, the conditions go as follow:
```
1. R > B
2. |R - G| > 15
3. R > G
4. R > 95, G > 40 and B > 20
```

After that, we transfer the image to the HSV color space where we keep the pixels respecting only this condition:
```
0.1 < S < 0.7
```

To pursue, the next color space is YUV, which is very similar to the HSV one. We must respect the following conditions:
```
1. 136 < V < 200
2. 80 < U < 130
```

Then, we go to the YIQ color space where in order to have a skin-related pixel, we must respect the following conditions where I = 0.596R - 0.275G - 0.322B
and Q = 128 + (0.21153661R) + (-0.52273617G) + (0.31119955B):
```
1. 121.5 < Q
2. 14 <= I <= 90
```

The last color space used was the Lab color space where we keep the pixels respecting the three last following conditions:
```
1. 100 < L
2. 134 < a
3. 115 < b < 177
```

This method took for granted that if a pixel respect all the conditions presented above, then it must be a skin-related pixel!

## How to use it
In order to use this program, you first need to install all the requirements with the following command:
```
pip install -r .\requirements.txt
```
After that, you only need to run the main.py program. If you want to change the treated picture, you only have to change the path inside this line:

![alt text](https://media.discordapp.net/attachments/575755454919999489/968690648439980072/unknown.png)

## Examples
![alt text](https://media.discordapp.net/attachments/575755454919999489/968684830248271962/unknown.png?width=631&height=473)
![alt text](https://media.discordapp.net/attachments/575755454919999489/968685158075088936/unknown.png)
![alt text](https://media.discordapp.net/attachments/575755454919999489/968685759458607124/unknown.png)
![alt text](https://media.discordapp.net/attachments/575755454919999489/968687613928173628/unknown.png?width=666&height=473)
![alt text](https://media.discordapp.net/attachments/575755454919999489/968688328121659435/unknown.png)
![alt text](https://media.discordapp.net/attachments/575755454919999489/968686178125627442/unknown.png)

## Conclusion and limitations
From what we can see with the examples, the results are quite good. In some situations, we even manage to separate the wood and the skin. However, when the skin is too bright or not bright enough, the program is no longer able to detect the skin. An interesting addition would be to try to determine the filters needed to detect only the lighted or very shaded skin.

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
