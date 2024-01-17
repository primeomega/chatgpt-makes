import pygame
from tkinter import Tk, Button, filedialog

class AudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Player")

        self.current_file = None

        # Buttons
        self.load_button = Button(root, text="Load Audio File", command=self.load_audio_file)
        self.load_button.pack(pady=10)

        self.play_button = Button(root, text="Play", command=self.play_audio)
        self.play_button.pack(pady=10)

        self.pause_button = Button(root, text="Pause", command=self.pause_audio)
        self.pause_button.pack(pady=10)

        self.stop_button = Button(root, text="Stop", command=self.stop_audio)
        self.stop_button.pack(pady=10)

    def load_audio_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".mp3",
                                                 filetypes=[("Audio files", "*.mp3"), ("All files", "*.*")])
        if file_path:
            self.current_file = file_path
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)

    def play_audio(self):
        if self.current_file:
            pygame.mixer.music.play()

    def pause_audio(self):
        pygame.mixer.music.pause()

    def stop_audio(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = Tk()
    app = AudioPlayer(root)
    root.mainloop()
