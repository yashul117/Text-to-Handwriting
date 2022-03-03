# Requirements:
# pip install opencv-python
# pip install pywhatkit

import pywhatkit as kit
import cv2

kit.text_to_handwriting("Scarcity means that there are fewer resources than are needed to fill human wants and needs. These resources can come from the land, labor resources or capital resources. Keep reading for scarcity examples that you may see on a global economic level or in your everyday life.", save_to="handwriting.png")
img = cv2.imread("handwriting.png")
cv2.imshow("Text to Handwriting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()