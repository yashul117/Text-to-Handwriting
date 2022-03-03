# Requirements:
# pip install opencv-python
# pip install pywhatkit

import pywhatkit as kit
import cv2

kit.text_to_handwriting("Hey guys, this is Yashul Tyagi. I am a software developer from Ghaziabad, Uttar Pradesh, India.png")
cv2.imshow("Text to Handwriting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()