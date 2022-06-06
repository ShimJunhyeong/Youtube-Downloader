from PySide6.QtCore import Slot, QThread, Signal
from pytube import YouTube


class ThreadYoutubeDownload(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__url = ""
        self.__download_path = ""

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @property
    def download_path(self):
        return self.__download_path

    @download_path.setter
    def download_path(self, download_path):
        self.__download_path = download_path

    def run(self):
        self.youtube_download(self.url, self.download_path)

    @staticmethod
    def youtube_download(url: str, download_path: str):
        print(url)
        yt = YouTube(url)  # 유튜브 영상 URL 입력
        yt.streams.filter(progressive=True, file_extension='mp4') \
            .order_by('resolution').desc().first().download(download_path)
