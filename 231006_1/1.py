import cv2

def put_string(frame, text, pt, value, color=(120, 200, 90) ):
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)
    cv2.putText(frame, text, pt, font, 0.7, color, 2)

capture = cv2.VideoCapture("C:/Users/USER/Desktop/video_file.avi")
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

## 카메라 속설 획득 및 출력
print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))
print("프레임 %d" % capture.get(cv2.CAP_PROP_FPS))

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    put_string(frame, 'WIDTH: ', (10, 40), width)

    height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    put_string(frame, 'HEIGHT: ', (10, 70), height)

    exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
    put_string(frame, 'EXPOS: ', (10, 100), exposure)

    brightness = capture.get(cv2.CAP_PROP_BRIGHTNESS)
    put_string(frame, 'BRIGHTNESS: ', (10, 130), brightness)

    second_frame = capture.get(cv2.CAP_PROP_FPS)
    put_string(frame, 'FRAME: ', (10, 160), second_frame)
    title = "View Frame from Camera"
    cv2.imshow(title, frame)
capture.release()