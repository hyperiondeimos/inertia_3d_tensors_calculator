# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inertiawindowGBbjfv.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# import qtcore
from qt_core import *

class Ui_Inertia3DTensorsWindow(object):
    def setupUi(self, Inertia3DTensorsWindow):
        if not Inertia3DTensorsWindow.objectName():
            Inertia3DTensorsWindow.setObjectName(u"Inertia3DTensorsWindow")
        Inertia3DTensorsWindow.resize(800, 1000)
        Inertia3DTensorsWindow.setMinimumSize(QSize(800, 1000))
        Inertia3DTensorsWindow.setMaximumSize(QSize(800, 1000))
        self.centralwidget = QWidget(Inertia3DTensorsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 1000))
        self.centralwidget.setMaximumSize(QSize(800, 1000))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb_input = QGroupBox(self.centralwidget)
        self.gb_input.setObjectName(u"gb_input")
        self.gb_input.setMinimumSize(QSize(780, 350))
        self.gb_input.setMaximumSize(QSize(16777215, 300))
        font = QFont()
        font.setBold(True)
        self.gb_input.setFont(font)
        self.formLayout = QFormLayout(self.gb_input)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.lbl_mass_fix = QLabel(self.gb_input)
        self.lbl_mass_fix.setObjectName(u"lbl_mass_fix")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_mass_fix)

        self.led_mass = QLineEdit(self.gb_input)
        self.led_mass.setObjectName(u"led_mass")
        self.led_mass.setMinimumSize(QSize(200, 25))
        self.led_mass.setMaximumSize(QSize(200, 25))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.led_mass)

        self.lbl_radius_fix = QLabel(self.gb_input)
        self.lbl_radius_fix.setObjectName(u"lbl_radius_fix")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_radius_fix)

        self.led_radius = QLineEdit(self.gb_input)
        self.led_radius.setObjectName(u"led_radius")
        self.led_radius.setMinimumSize(QSize(200, 25))
        self.led_radius.setMaximumSize(QSize(200, 25))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.led_radius)

        self.lbl_axis_a_fix = QLabel(self.gb_input)
        self.lbl_axis_a_fix.setObjectName(u"lbl_axis_a_fix")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_axis_a_fix)

        self.lbl_axis_b_fix = QLabel(self.gb_input)
        self.lbl_axis_b_fix.setObjectName(u"lbl_axis_b_fix")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_axis_b_fix)

        self.lbl_axis_c_fix = QLabel(self.gb_input)
        self.lbl_axis_c_fix.setObjectName(u"lbl_axis_c_fix")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_axis_c_fix)

        self.lbl_heigth_fix = QLabel(self.gb_input)
        self.lbl_heigth_fix.setObjectName(u"lbl_heigth_fix")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.lbl_heigth_fix)

        self.lbl_depth_fix = QLabel(self.gb_input)
        self.lbl_depth_fix.setObjectName(u"lbl_depth_fix")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.lbl_depth_fix)

        self.lbl_length_fix = QLabel(self.gb_input)
        self.lbl_length_fix.setObjectName(u"lbl_length_fix")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lbl_length_fix)

        self.lbl_r1_fix = QLabel(self.gb_input)
        self.lbl_r1_fix.setObjectName(u"lbl_r1_fix")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_r1_fix)

        self.lbl_r2_fix = QLabel(self.gb_input)
        self.lbl_r2_fix.setObjectName(u"lbl_r2_fix")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_r2_fix)

        self.led_r1 = QLineEdit(self.gb_input)
        self.led_r1.setObjectName(u"led_r1")
        self.led_r1.setMinimumSize(QSize(200, 25))
        self.led_r1.setMaximumSize(QSize(200, 25))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.led_r1)

        self.led_r2 = QLineEdit(self.gb_input)
        self.led_r2.setObjectName(u"led_r2")
        self.led_r2.setMinimumSize(QSize(200, 25))
        self.led_r2.setMaximumSize(QSize(200, 25))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.led_r2)

        self.led_axis_a = QLineEdit(self.gb_input)
        self.led_axis_a.setObjectName(u"led_axis_a")
        self.led_axis_a.setMinimumSize(QSize(200, 25))
        self.led_axis_a.setMaximumSize(QSize(200, 25))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.led_axis_a)

        self.led_axis_b = QLineEdit(self.gb_input)
        self.led_axis_b.setObjectName(u"led_axis_b")
        self.led_axis_b.setMinimumSize(QSize(200, 25))
        self.led_axis_b.setMaximumSize(QSize(200, 25))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.led_axis_b)

        self.led_axis_c = QLineEdit(self.gb_input)
        self.led_axis_c.setObjectName(u"led_axis_c")
        self.led_axis_c.setMinimumSize(QSize(200, 25))
        self.led_axis_c.setMaximumSize(QSize(200, 25))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.led_axis_c)

        self.led_length = QLineEdit(self.gb_input)
        self.led_length.setObjectName(u"led_length")
        self.led_length.setMinimumSize(QSize(200, 25))
        self.led_length.setMaximumSize(QSize(200, 25))

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.led_length)

        self.led_depth = QLineEdit(self.gb_input)
        self.led_depth.setObjectName(u"led_depth")
        self.led_depth.setMinimumSize(QSize(200, 25))
        self.led_depth.setMaximumSize(QSize(200, 26))

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.led_depth)

        self.led_height = QLineEdit(self.gb_input)
        self.led_height.setObjectName(u"led_height")
        self.led_height.setMinimumSize(QSize(200, 25))
        self.led_height.setMaximumSize(QSize(200, 25))

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.led_height)

        self.btn_calculate = QPushButton(self.gb_input)
        self.btn_calculate.setObjectName(u"btn_calculate")
        self.btn_calculate.setMinimumSize(QSize(200, 30))
        self.btn_calculate.setMaximumSize(QSize(200, 30))

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.btn_calculate)

        self.lbl_width_fix = QLabel(self.gb_input)
        self.lbl_width_fix.setObjectName(u"lbl_width_fix")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.lbl_width_fix)

        self.led_width = QLineEdit(self.gb_input)
        self.led_width.setObjectName(u"led_width")
        self.led_width.setMinimumSize(QSize(200, 25))
        self.led_width.setMaximumSize(QSize(200, 25))

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.led_width)


        self.gridLayout.addWidget(self.gb_input, 2, 0, 1, 2, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gb_check = QGroupBox(self.centralwidget)
        self.gb_check.setObjectName(u"gb_check")
        self.gb_check.setMinimumSize(QSize(0, 230))
        self.gb_check.setMaximumSize(QSize(16777215, 230))
        self.gb_check.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.gb_check)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.figure_layout = QVBoxLayout()
        self.figure_layout.setObjectName(u"figure_layout")
        self.lbl_figure_fix = QLabel(self.gb_check)
        self.lbl_figure_fix.setObjectName(u"lbl_figure_fix")
        self.lbl_figure_fix.setMinimumSize(QSize(160, 20))
        self.lbl_figure_fix.setMaximumSize(QSize(160, 20))

        self.figure_layout.addWidget(self.lbl_figure_fix)


        self.horizontalLayout_2.addLayout(self.figure_layout)

        self.matrix_layout = QVBoxLayout()
        self.matrix_layout.setObjectName(u"matrix_layout")
        self.lbl_matrix_fix = QLabel(self.gb_check)
        self.lbl_matrix_fix.setObjectName(u"lbl_matrix_fix")
        self.lbl_matrix_fix.setMinimumSize(QSize(160, 20))
        self.lbl_matrix_fix.setMaximumSize(QSize(160, 20))

        self.matrix_layout.addWidget(self.lbl_matrix_fix)


        self.horizontalLayout_2.addLayout(self.matrix_layout)

        self.model_layout = QVBoxLayout()
        self.model_layout.setObjectName(u"model_layout")
        self.lbl_model_matrix_fix = QLabel(self.gb_check)
        self.lbl_model_matrix_fix.setObjectName(u"lbl_model_matrix_fix")
        self.lbl_model_matrix_fix.setMinimumSize(QSize(160, 20))
        self.lbl_model_matrix_fix.setMaximumSize(QSize(160, 20))

        self.model_layout.addWidget(self.lbl_model_matrix_fix)


        self.horizontalLayout_2.addLayout(self.model_layout)


        self.gridLayout.addWidget(self.gb_check, 1, 1, 1, 1)

        self.gb_selection = QGroupBox(self.centralwidget)
        self.gb_selection.setObjectName(u"gb_selection")
        self.gb_selection.setMinimumSize(QSize(0, 230))
        self.gb_selection.setMaximumSize(QSize(250, 230))
        self.gb_selection.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.gb_selection)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cb_shape = QComboBox(self.gb_selection)
        self.cb_shape.setObjectName(u"cb_shape")
        self.cb_shape.setMaximumSize(QSize(150, 25))

        self.horizontalLayout.addWidget(self.cb_shape)

        self.btn_select = QPushButton(self.gb_selection)
        self.btn_select.setObjectName(u"btn_select")
        self.btn_select.setMaximumSize(QSize(50, 25))

        self.horizontalLayout.addWidget(self.btn_select)


        self.gridLayout.addWidget(self.gb_selection, 1, 0, 1, 1, Qt.AlignVCenter)

        self.lbl_about = QLabel(self.centralwidget)
        self.lbl_about.setObjectName(u"lbl_about")
        self.lbl_about.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.lbl_about, 0, 0, 1, 2)

        self.gb_results = QGroupBox(self.centralwidget)
        self.gb_results.setObjectName(u"gb_results")
        self.gb_results.setMinimumSize(QSize(0, 350))
        self.gb_results.setMaximumSize(QSize(16777215, 300))
        self.gb_results.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.gb_results)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.txtb_results = QTextBrowser(self.gb_results)
        self.txtb_results.setObjectName(u"txtb_results")
        self.txtb_results.setMinimumSize(QSize(760, 280))
        self.txtb_results.setMaximumSize(QSize(800, 280))
        self.txtb_results.setBaseSize(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.txtb_results)

        self.btn_export = QPushButton(self.gb_results)
        self.btn_export.setObjectName(u"btn_export")
        self.btn_export.setMinimumSize(QSize(200, 25))
        self.btn_export.setMaximumSize(QSize(200, 25))

        self.verticalLayout_4.addWidget(self.btn_export, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.gb_results, 3, 0, 1, 2, Qt.AlignHCenter|Qt.AlignVCenter)

        Inertia3DTensorsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Inertia3DTensorsWindow)

        QMetaObject.connectSlotsByName(Inertia3DTensorsWindow)
    # setupUi

    def retranslateUi(self, Inertia3DTensorsWindow):
        Inertia3DTensorsWindow.setWindowTitle(QCoreApplication.translate("Inertia3DTensorsWindow", u"MainWindow", None))
        self.gb_input.setTitle(QCoreApplication.translate("Inertia3DTensorsWindow", u"3. Input data", None))
        self.lbl_mass_fix.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Mass (m) in kg", None))
        self.lbl_radius_fix.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Radius (r) in meters", None))
        self.lbl_axis_a_fix.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Semi-Axis (a) in meters", None))
        self.lbl_axis_b_fix.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Semi-Axis (b) in meters", None))
        self.lbl_axis_c_fix.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Semi-Axis (c) in meters", None))
        self.lbl_heigth_fix.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Height (h) in meters", None))
        self.lbl_depth_fix.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Depth (d) in meters", None))
        self.lbl_length_fix.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Length (l) in meters", None))
        self.lbl_r1_fix.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Inner Radius (r1) in meters", None))
        self.lbl_r2_fix.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Outer Radius (r2) in meters", None))
        self.btn_calculate.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Calculate!!", None))
        self.lbl_width_fix.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Width (w) in meters", None))
        self.gb_check.setTitle(QCoreApplication.translate("Inertia3DTensorsWindow", u"2. Check if the shape is correct", None))
        self.lbl_figure_fix.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Figure", None))
        self.lbl_matrix_fix.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Inertia Matrix", None))
        self.lbl_model_matrix_fix.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Inertia Matrix (Model)", None))
        self.gb_selection.setTitle(QCoreApplication.translate("Inertia3DTensorsWindow", u"1. Select the 3D shape", None))
        self.btn_select.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Select", None))
        self.lbl_about.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Developed by Anderson Fontoura \u00a92022. Based on Wikipedia Article List of Moments of Inertia", None))
        self.gb_results.setTitle(QCoreApplication.translate("Inertia3DTensorsWindow", u"4. Results", None))
        self.btn_export.setText(QCoreApplication.translate("Inertia3DTensorsWindow", u"Export to . txt file", None))
    # retranslateUi

