# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

from QLabelCustom import QLabelCustom
from QLineEditCustom import QLineEditCustom
import resource_rc

class Ui_mainWidget(object):
    def setupUi(self, mainWidget):
        if not mainWidget.objectName():
            mainWidget.setObjectName(u"mainWidget")
        mainWidget.resize(415, 265)
        icon = QIcon()
        icon.addFile(u":/icon/static/YouTube.ico", QSize(), QIcon.Normal, QIcon.Off)
        mainWidget.setWindowIcon(icon)
        mainWidget.setStyleSheet(u"#mainWidget{\n"
"	background-color: #3C3F41;\n"
"}\n"
"\n"
"#edit_download_path:disabled {\n"
"	background-color: #ffffff;\n"
"}\n"
"")
        self.lbl_title = QLabel(mainWidget)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setGeometry(QRect(87, 10, 281, 61))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lbl_title.setFont(font)
        self.lbl_title.setText(u"<html><head/><body><p><span style=\" color:#ffffff;\">You</span><span style=\" color:#ff0000;\">Tube</span> Downloader</p></body></html>")
        self.lbl_title.setScaledContents(False)
        self.lbl_title.setWordWrap(False)
        self.lbl_logo = QLabel(mainWidget)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setGeometry(QRect(17, 16, 61, 51))
        self.lbl_logo.setPixmap(QPixmap(u":/icon/static/YouTube.ico"))
        self.edit_download_path = QLineEditCustom(mainWidget)
        self.edit_download_path.setObjectName(u"edit_download_path")
        self.edit_download_path.setEnabled(True)
        self.edit_download_path.setGeometry(QRect(20, 150, 371, 22))
        self.edit_download_path.setReadOnly(True)
        self.lbl_download_path = QLabelCustom(mainWidget)
        self.lbl_download_path.setObjectName(u"lbl_download_path")
        self.lbl_download_path.setGeometry(QRect(22, 130, 101, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.lbl_download_path.setFont(font1)
        self.edit_youtube_url = QLineEdit(mainWidget)
        self.edit_youtube_url.setObjectName(u"edit_youtube_url")
        self.edit_youtube_url.setGeometry(QRect(20, 100, 371, 22))
        self.lbl_youtube_url = QLabel(mainWidget)
        self.lbl_youtube_url.setObjectName(u"lbl_youtube_url")
        self.lbl_youtube_url.setGeometry(QRect(22, 80, 191, 16))
        self.lbl_youtube_url.setFont(font1)
        self.btn_download = QPushButton(mainWidget)
        self.btn_download.setObjectName(u"btn_download")
        self.btn_download.setGeometry(QRect(20, 190, 371, 51))
        font2 = QFont()
        font2.setPointSize(15)
        self.btn_download.setFont(font2)

        self.retranslateUi(mainWidget)

        QMetaObject.connectSlotsByName(mainWidget)
    # setupUi

    def retranslateUi(self, mainWidget):
        mainWidget.setWindowTitle(QCoreApplication.translate("mainWidget", u"YouTube Downloader", None))
        self.lbl_logo.setText("")
        self.lbl_download_path.setText(QCoreApplication.translate("mainWidget", u"<html><head/><body><p><span style=\" color:#ffffff;\">\ub2e4\uc6b4\ub85c\ub4dc \ud560 \uacbd\ub85c</span></p></body></html>", None))
        self.lbl_youtube_url.setText(QCoreApplication.translate("mainWidget", u"<html><head/><body><p><span style=\" color:#ffffff;\">\ub2e4\uc6b4\ub85c\ub4dc \ud560 YouTube \uc601\uc0c1 URL</span></p></body></html>", None))
        self.btn_download.setText(QCoreApplication.translate("mainWidget", u"DOWNLOAD", None))
    # retranslateUi
