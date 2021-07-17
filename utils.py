import cv2, torchaudio
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

def get_waveform(audio_file):

    return audio_file

def get_fps(video_len, length=10, rounded=False):
    # rounded to the nearest frame
    if rounded:
        return round(float(video_len) / length)
    else:
        return float(video_len) / float(length)