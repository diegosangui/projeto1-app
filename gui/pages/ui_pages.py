# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesLhsXco.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_app_pages(object):
    def setupUi(self, app_pages):
        if not app_pages.objectName():
            app_pages.setObjectName(u"app_pages")
        app_pages.resize(929, 562)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout = QVBoxLayout(self.page1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_pg1 = QLabel(self.page1)
        self.lbl_pg1.setObjectName(u"lbl_pg1")
        self.lbl_pg1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_pg1)

        app_pages.addWidget(self.page1)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.verticalLayout_3 = QVBoxLayout(self.page3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_pg3 = QLabel(self.page3)
        self.lbl_pg3.setObjectName(u"lbl_pg3")
        self.lbl_pg3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_pg3)

        app_pages.addWidget(self.page3)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_2 = QVBoxLayout(self.page2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_pg2 = QLabel(self.page2)
        self.lbl_pg2.setObjectName(u"lbl_pg2")
        self.lbl_pg2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_pg2)

        app_pages.addWidget(self.page2)

        self.retranslateUi(app_pages)

        app_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(app_pages)
    # setupUi

    def retranslateUi(self, app_pages):
        app_pages.setWindowTitle(QCoreApplication.translate("app_pages", u"StackedWidget", None))
        self.lbl_pg1.setText(QCoreApplication.translate("app_pages", u"PAGINA INICIAL", None))
        self.lbl_pg3.setText(QCoreApplication.translate("app_pages", u"PAGINA 3", None))
        self.lbl_pg2.setText(QCoreApplication.translate("app_pages", u"PAGINA 2", None))
    # retranslateUi

