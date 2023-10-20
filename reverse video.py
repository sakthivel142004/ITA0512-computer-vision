import cv2
def reverse_video_play(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    cv2.destroyAllWindows()
    for frame in reversed(frames):
        cv2.imshow('Reversed Video', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
if __name__ == "__main__":
    video_path = "D:/Samsung Galaxy A71/Movies/WhatsApp/VID-20230125-WA0039.mp4"
    reverse_video_play(video_path)
