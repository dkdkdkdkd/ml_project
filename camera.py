import cv2

# 첫 번째 웹캠과 두 번째 웹캠을 인식
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

if not cap1.isOpened() or not cap2.isOpened():
    print("웹캠을 인식할 수 없습니다.")
    exit()

while True:
    # 각 웹캠으로부터 프레임 읽기
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print("프레임을 읽을 수 없습니다.")
        break

    # 첫 번째 웹캠의 화면을 왼쪽에, 두 번째 웹캠의 화면을 오른쪽에 표시
    combined_frame = cv2.hconcat([frame1, frame2])
    cv2.imshow('Two Webcams', combined_frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
