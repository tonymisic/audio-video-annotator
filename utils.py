import cv2
def get_frames(video_file):
    cap = cv2.VideoCapture(video_file)
    frames = []
    success, image = cap.read()
    while success:
        frames.append(image)
        success, image = cap.read()
    if len(frames) <= 1:
        print("Error loading file!")
        return frames
    return frames
