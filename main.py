import os
import sys
import json
from PySide6.QtCore import Slot, QThread, Signal, QObject
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from design.ui_main import Ui_mainWidget
import pytube
from pytube import YouTube


class ThreadSignal(QObject):
    sig = Signal()
    suc_sig = Signal()


class ThreadYoutubeDownload(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.signal = ThreadSignal()
        self.url = ""
        self.download_path = ""

    def run(self):
        try:
            self.youtube_download(self.url, self.download_path)
            self.signal.suc_sig.emit()
        except pytube.exceptions.RegexMatchError:
            self.signal.sig.emit()

    @staticmethod
    def youtube_download(url: str, download_path: str):
        yt = YouTube(url)  # 유튜브 영상 URL 입력
        yt.streams.filter(progressive=True, file_extension='mp4') \
            .order_by('resolution').desc().first().download(download_path)


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
        self.thread = ThreadYoutubeDownload()
        self.thread.signal.sig.connect(self.activate_btn_fail)
        self.thread.signal.suc_sig.connect(self.activate_btn_success)

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

        self.thread.url = self.edit_youtube_url.text()
        self.thread.download_path = self.edit_download_path.text()
        self.thread.start()

    def save_config(self):
        with open("app.config", "w", encoding='utf-8') as f:
            json.dump({"youtube url": self.edit_youtube_url.text(),
                       "download path": self.edit_download_path.text()},
                      f, ensure_ascii=False, indent="\t")

    def activate_btn_fail(self):
        msg_box = QMessageBox()
        msg_box.setText("Please Check URL")
        msg_box.exec()

        self.btn_download.setText("DOWNLOAD")
        self.btn_download.setEnabled(True)
        self.btn_download.repaint()

    def activate_btn_success(self):
        msg_box = QMessageBox()
        msg_box.setText("Download Complete")
        msg_box.exec()

        self.btn_download.setText("DOWNLOAD")
        self.btn_download.setEnabled(True)
        self.btn_download.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
