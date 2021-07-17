import tkinter as tk
from tkinter import ttk
from tkinter.constants import FALSE, GROOVE
from tkinter import messagebox as mb
from ttkthemes import ThemedTk, THEMES
from tkinter.filedialog import askdirectory, askopenfilename
import os, utils
from PIL import Image

class Editor(ThemedTk):
    ''' Viewing and annotating audio and video samples.
    '''
    def __init__(self, theme="adapta"):
        # globals
        self.AUDIO_FOLDER = "Unselected"
        self.VIDEO_FOLDER = "Unselected"
        self.ANNOTATIONS_FILE = "Unselected"
        self.PLAYING = False
        self.CURRENT_FRAME = 0
        self.CURRENT_SEGMENT = 0
        self.CURRENT_INDEX = 0
        self.AUDIO_SELECTED = False
        self.VIDEO_SELECTED = False
        self.ANNOTATIONS_SELECTED = False
        self.VIDEOS = []
        self.CURRENT_VIDEO = []
        self.AUDIOS = []
        self.CURRENT_AUDIO = []
        self.ANNOS = []
        # initialize and set theme
        border, b_width = GROOVE, 3
        ThemedTk.__init__(self, fonts=True, themebg=True)
        self.set_theme(theme)
        self.title("Audio Video Shenanigans")
        # frame view
        self.frame_view = ttk.Frame(self, borderwidth = b_width, relief=border)
        self.video_canvas = tk.Canvas(self, width=900, height=600, background='gray75')
        self.create_frame_view()
        # audio waveform view
        self.audio_view = ttk.Frame(self, borderwidth = b_width, relief=border)
        self.slider = tk.Scale(from_=0, to=100, length=900, command=lambda *args: self.change_frame(), orient=tk.HORIZONTAL, showvalue=FALSE)
        self.audio_canvas = tk.Canvas(self, width=900, height=100, background='gray75')
        self.create_audio_view()
        # video and frame level controllers
        self.controls_view = ttk.Frame(self, borderwidth = 0, relief=border)
        self.play = ttk.Button(command=lambda *args: self.play_video(), text="Play")
        self.load = ttk.Button(command=lambda *args: self.load_data(), text="Load")
        self.pause = ttk.Button(command=lambda *args: self.pause_video(), text="Pause")
        self.next_video = ttk.Button(command=lambda *args: self.change_video(1), text="Next Video")
        self.previous_video = ttk.Button(command=lambda *args: self.change_video(-1), text="Previous Video")
        self.create_controls_view()
        # statistics viewer
        self.stats_view = ttk.Frame(self, borderwidth = b_width, relief=border)
        self.table = ttk.Treeview(columns=('Variable', 'Value'), show='headings')
        self.grid_stats()
        self.create_stats_view()
        # file and folder level controllers
        self.file_view = ttk.Frame(self, borderwidth = 0, relief=border)
        self.folder_a = ttk.Label(text="Audio Folder: " + str('Unselected'))
        self.folder_v = ttk.Label(text="Video Folder: " + str('Unselected'))
        self.file = ttk.Label(text="Annotation File: " + str('Unselected'))
        self.select_v_folder = ttk.Button(command=lambda *args: self.select_folder('video'), text="Select Video Folder")
        self.select_a_folder = ttk.Button(command=lambda *args: self.select_folder('audio'), text="Select Audio Folder")
        self.select_file = ttk.Button(command=lambda *args: self.select_folder('annos'), text="Select Annotation File")
        self.create_file_view()
        # spectrogram viewing
        self.spectrogram_view = ttk.Frame(self, borderwidth = b_width, relief=border)
        self.spectrogram_canvas = tk.Canvas(self, width=500, height=200, background='gray75')
        self.create_spectrogram_view()
        # Grid widgets
        self.grid_widgets()

    def change_video(self, change):
        print(change)
    def play_video(self):
        print("Playing~!")
    def pause_video(self):
        print("Paused~!")
    def change_frame(self):
        print(self.slider.get())
    def load_data(self):
        if self.ANNOTATIONS_SELECTED and self.AUDIO_SELECTED and self.VIDEO_SELECTED:
            print("Loading data!")
            self.VIDEOS = os.listdir(self.VIDEO_FOLDER)
            self.CURRENT_VIDEO = utils.get_frames(self.VIDEO_FOLDER + self.VIDEOS[self.CURRENT_INDEX])
            self.AUDIOS = os.listdir(self.AUDIO_FOLDER)
            self.CURRENT_AUDIO = utils.get_waveform(self.AUDIO_FOLDER + self.AUDIOS[self.CURRENT_INDEX])
            self.ANNOS = open(self.ANNOTATIONS_FILE, 'r').readlines()
        else:
            mb.showwarning("Warning!", "Please make sure all required files are selected!")
    
    def select_folder(self, modality):
        if modality == 'audio':
            self.AUDIO_FOLDER = askdirectory(title='Select folder with .wav files', initialdir='/')
            self.folder_a['text'] = "Audio Folder: " + self.AUDIO_FOLDER
            self.AUDIO_SELECTED = True
        elif modality == 'video':
            self.VIDEO_FOLDER = askdirectory(title='Select folder with .mp4 files', initialdir='/')
            self.folder_v['text'] = "Video Folder: " + self.VIDEO_FOLDER
            self.VIDEO_SELECTED = True
        elif modality == 'annos':
            self.ANNOTATIONS_FILE = askopenfilename(title='Select annotation file', initialdir='/')
            self.file['text'] = "Annotation File: " + self.ANNOTATIONS_FILE
            self.ANNOTATIONS_SELECTED = True
        else:
            print("No such modality exists!")
        
    def grid_widgets(self):
        self.frame_view.grid(row=0, column=0, rowspan=2)
        self.audio_view.grid(row=2, column=0, rowspan=1)
        self.slider.grid(row=3, column=0, rowspan=1)
        self.controls_view.grid(row=4, column=0, rowspan=1)
        self.stats_view.grid(row=0, column=1, rowspan=1)
        self.file_view.grid(row=1, column=1, rowspan=1)
        self.spectrogram_view.grid(row=2, column=1, rowspan=3)

    def create_frame_view(self):
        self.video_canvas.pack(in_=self.frame_view, expand=False)

    def create_audio_view(self):
        self.audio_canvas.pack(in_=self.audio_view, expand=False)

    def create_controls_view(self):
        self.previous_video.pack(in_=self.controls_view, side=tk.LEFT, expand=False, padx=60)
        self.play.pack(in_=self.controls_view, side=tk.LEFT, expand=False)
        self.load.pack(in_=self.controls_view, side=tk.LEFT, expand=False)
        self.pause.pack(in_=self.controls_view, side=tk.LEFT, expand=False)
        self.next_video.pack(in_=self.controls_view, side=tk.LEFT, expand=False, padx=60)

    def create_stats_view(self):
        self.table.pack(in_=self.stats_view, side=tk.TOP, expand=True)
    def grid_stats(self):
        self.table.heading('Variable', text="Variable")
        self.table.heading('Value', text="Value")
        self.table.insert("", "end", values=("File", "undetermined"))
        self.table.insert("", "end", values=("Current Frame", "undetermined"))
        self.table.insert("", "end", values=("Current Segment", "undetermined"))
        self.table.insert("", "end", values=("Class", "undetermined"))
        self.table.insert("", "end", values=("Event Start", "undetermined"))
        self.table.insert("", "end", values=("Event End", "undetermined"))
        self.table.insert("", "end", values=("Audio Quality", "undetermined"))
        self.table.insert("", "end", values=("Frame Count", "undetermined"))
        self.table.insert("", "end", values=("FPS", "undetermined"))
        self.table.insert("", "end", values=("Mel-Frames", "undetermined"))
        self.table.insert("", "end", values=("Mel-Bands", "undetermined"))

    def create_file_view(self):
        self.folder_a.pack(in_=self.file_view, expand=True)
        self.select_a_folder.pack(in_=self.file_view, expand=True)
        self.folder_v.pack(in_=self.file_view, expand=True)
        self.select_v_folder.pack(in_=self.file_view, expand=True)
        self.file.pack(in_=self.file_view, expand=True)
        self.select_file.pack(in_=self.file_view, expand=True)

    def create_spectrogram_view(self):
        self.spectrogram_canvas.pack(in_=self.spectrogram_view, expand=False)