import pygame
import os


class Player:
    def __init__(self, music_folder):
        pygame.mixer.init()

        self.music_folder = music_folder
        self.playlist = self.load_music()
        self.current_index = 0
        self.is_playing = False

        # auto music playing aafter each other
        pygame.mixer.music.set_endevent(pygame.USEREVENT)

    def load_music(self):
        files = []
        for file in os.listdir(self.music_folder):
            if file.endswith(".wav") or file.endswith(".mp3"):
                files.append(os.path.join(self.music_folder, file))
        return files

    def play(self):
        if not self.playlist:
            return
        pygame.mixer.music.load(self.playlist[self.current_index])
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def pause(self):
        pygame.mixer.music.pause()
        self.is_playing = False

    def resume(self):
        pygame.mixer.music.unpause()
        self.is_playing = True

    def set_volume(self, volume):
        # volume: float от 0.0 до 1.0
        pygame.mixer.music.set_volume(volume)

    def next_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def get_current_track_name(self):
        if not self.playlist:
            return "No tracks"
        return os.path.basename(self.playlist[self.current_index])

    def get_position(self):
        # миллисекунды to секунды
        pos = pygame.mixer.music.get_pos() / 1000
        return max(0, int(pos))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.next_track()

    def show_playlist(self):
        for i, track in enumerate(self.playlist):
            print(f"{i+1}. {os.path.basename(track)}")


# main
if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    music_path = os.path.join(base_dir, "music")

    player = Player(music_path)
    player.show_playlist()

    # пример запуска
    player.play()
    print("Playing:", player.get_current_track_name())
