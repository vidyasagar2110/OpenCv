import cv2

video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error reading video file")

frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)

result = cv2.VideoWriter('filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 100, size)

logo = cv2.imread("logo.png")
logo = cv2.resize(logo, (100, 100))

while True:
    ret, frame = video.read()
    if not ret:
        break

    x_offset = frame.shape[1] - logo.shape[1] - 20
    y_offset = 20
    frame[y_offset:y_offset+logo.shape[0], x_offset:x_offset+logo.shape[1]] = logo

    result.write(frame)
    cv2.imshow('Frame with Logo', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

video.release()
result.release()
cv2.destroyAllWindows()
