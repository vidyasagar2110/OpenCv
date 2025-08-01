import cv2
import numpy as np

url = "http://10.67.98.45:8080/video"  # Replace with your IP webcam URL
cp = cv2.VideoCapture(url)

# Load and resize hero image
hero = cv2.imread("hero.jpg")
if hero is None:
    print("Error: hero.jpg not found.")
    exit()
hero = cv2.resize(hero, (200, 200))  # Bigger size

while True:
    camera, frame = cp.read()
    if frame is not None:
        # Overlay hero image at top-left corner
        frame[20:220, 20:220] = hero
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break

cv2.destroyAllWindows()