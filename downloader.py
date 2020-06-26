import os


class Downloader:

    def __init__(self, save_dir):
        self.dir = save_dir

    def download_song(self, song):
        command = 'youtube-dl -x --audio-format mp3 -o "{}/%(title)s.%(ext)s" "ytsearch1:{} - {}"'.format(
            self.dir, song[0], song[1])
        # print(command)
        os.system(command)
