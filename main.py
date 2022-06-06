import os
import sys
import json
import time as time
from multiprocessing import Process
from threading import Thread
from PySide6 import QtWidgets
from PySide6.QtCore import Slot, QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from ThreadYoutubeDownload import ThreadYoutubeDownload
from design.ui_main import Ui_mainWidget


    # self.btn_download.setText("DOWNLOAD")
    # self.btn_download.setEnabled(True)


class MainWindow(QMainWindow, Ui_mainWidget):
    json_object = ""

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setFixedSize(self.size())  # 사이즈 고정하기

        self.lbl_download_path.clicked.connect(lambda: self.open_file_dialog(self.edit_download_path))
        self.edit_download_path.clicked.connect(lambda: self.open_file_dialog(self.edit_download_path))
        self.edit_download_path.textChanged.connect(lambda: self.save_config())
        self.btn_download.clicked.connect(lambda: self.download())

        self.ref_edit_youtube_url = self.edit_youtube_url
        self.ref_edit_download_path = self.edit_download_path

        try:
            with open("app.config", "r") as f:
                self.json_object = json.load(f)
                self.edit_download_path.setText(self.json_object["download path"])
                self.edit_youtube_url.setText(self.json_object["youtube url"])
        except Exception:
            print(json.dumps({"youtube url": "", "download path": ""}, ensure_ascii=False, indent="\t"))
            with open("app.config", "w", encoding='utf-8') as f:
                json.dump({"youtube url": "", "download path": ""}, f, ensure_ascii=False, indent="\t")

    @Slot()
    def open_file_dialog(self, edit_download_path):
        dialog = QFileDialog()
        foo_dir = dialog.getExistingDirectory(self, '다운로드 받은 유튜브 영상을 저장할 폴더를 선택하세요.')
        edit_download_path.setText(foo_dir)

    @Slot()
    def download(self):
        if not os.path.isdir(self.edit_download_path.text()):
            self.open_file_dialog(self.edit_download_path)

        self.btn_download.setText("DOWNLOADING...")
        self.btn_download.setEnabled(False)
        self.btn_download.repaint()

        self.save_config()

        th_youtube_download = ThreadYoutubeDownload(self)
        th_youtube_download.url = self.edit_youtube_url.text()
        th_youtube_download.download_path = self.edit_download_path.text()
        th_youtube_download.start()
        # thread_youtube_download = Thread(target=self.youtube_download,
        #                                  args=(self.edit_youtube_url.text(),))
        # thread_youtube_download.start()
        # thread_youtube_download.join()  # wait thread finish

        # yt = YouTube('https://www.youtube.com/watch?v=rRzxEiBLQCA')  # 유튜브 영상 URL 입력
        # yt.streams        # 해당 URL의 영상 스트림을 리스트로 가져온다
        # .filter(progressive=True, file_extension='mp4') \  # 프로그레시브 방식의 인코딩, 파일 포맷은 MP4
        # .order_by('resolution') \  # 영상 해상도 순으로 정렬
        # .desc() \           # 내림차순 정렬
        # .first() \          # 가장 첫 번째 스트림(가장 고화질)
        # .download()         # 다운로드, 매개변수로 다운로드 경로를 지정할 수 있음

    def save_config(self):
        with open("app.config", "w", encoding='utf-8') as f:
            json.dump({"youtube url": self.edit_youtube_url.text(),
                       "download path": self.edit_download_path.text()},
                      f, ensure_ascii=False, indent="\t")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
