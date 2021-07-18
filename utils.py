import cv2, torchaudio, torch, matplotlib.pyplot as plt
def get_frames(video_file):
    print(video_file)
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

def plot_waveform(audio_file):
    waveform, sample_rate = torchaudio.load(audio_file)
    waveform = waveform.numpy()
    _, num_frames = waveform.shape
    time_axis = torch.arange(0, num_frames) / sample_rate
    plt.figure(figsize=(9, 1))
    plt.axis('off')
    plt.gca().set_axis_off()
    plt.margins(0,0)
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.plot(time_axis, waveform[0], '#14a1de', linewidth=0.5)
    plt.savefig('current_audio.png', bbox_inches=0, pad_inches=0)

def get_fps(video_len, length=10, rounded=False):
    # rounded to the nearest frame
    if rounded:
        return round(float(video_len) / length)
    else:
        return float(video_len) / float(length)
