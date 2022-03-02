import sys
import os

# import qtcore
from qt_core import *

# import windows
from gui.ui_inertiawindow import *

# import equations
from equations import *


# main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set main title of app and favicon
        self.setWindowTitle("N3D Inertia Tensors Calculator")
        
        # Setup MainWindow
        self.ui = Ui_Inertia3DTensorsWindow()
        self.ui.setupUi(self)

        # object instance to store formula values
        self.eq = Inertials()

        # populate the formula combo-box with data provided from database
        self.cb_populate()

        # update TableView with formulas
        self.hide_boxes()
        self.hide_fields()

        # flag from first execution
        self.first_exec = True

        # show gb check signal
        self.ui.btn_select.clicked.connect(self.check_solid)

        # calculate
        self.ui.btn_calculate.clicked.connect(self.calculate)

        # export data to txt file
        self.ui.btn_export.clicked.connect(self.save_file)

        # signal to enable calculate button
        self.ui.led_mass.textChanged.connect(self.enable_calculation)
        self.ui.led_depth.textChanged.connect(self.enable_calculation)
        self.ui.led_length.textChanged.connect(self.enable_calculation)
        self.ui.led_radius.textChanged.connect(self.enable_calculation)
        self.ui.led_height.textChanged.connect(self.enable_calculation)
        self.ui.led_width.textChanged.connect(self.enable_calculation)
        self.ui.led_axis_a.textChanged.connect(self.enable_calculation)
        self.ui.led_axis_b.textChanged.connect(self.enable_calculation)
        self.ui.led_axis_c.textChanged.connect(self.enable_calculation)
        self.ui.led_r1.textChanged.connect(self.enable_calculation)
        self.ui.led_r2.textChanged.connect(self.enable_calculation)
      
        # Show MainWindow
        self.show()
    
    def closeEvent(self, event):
        """
        Override Method of PyQt for check if the window is closed or not
        :param event: signal to close (true) or not (false)
        :return: none
        """

        reply = QMessageBox.question(self, 'Close', 'Are you sure you want to close this window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def cb_populate(self):
        """
        Method used to populate the combobox with shapes supported
        :return: none
        """
        # clear comboboxes - for good pratices
        self.ui.cb_shape.clear()

        a = ("Solid Sphere",
            "Hollow Sphere",
            "Solid Ellipsoid",
            "Right Circular Cone",
            "Solic Cuboid",
            "Slender Rod - End",
            "Slender Rod - Center",
            "Solid Cylinder",
            "TW Cylindrical Tube"
        )
        # populate the combobox
        self.ui.cb_shape.addItems(sorted(a))

    def hide_boxes(self):
        self.ui.gb_check.hide()
        self.ui.gb_input.hide()
        self.ui.gb_results.hide()

    def hide_fields(self):

        self.ui.lbl_radius_fix.hide()
        self.ui.led_radius.hide()

        self.ui.lbl_axis_a_fix.hide()
        self.ui.led_axis_a.hide()

        self.ui.lbl_axis_b_fix.hide()
        self.ui.led_axis_b.hide()

        self.ui.lbl_axis_c_fix.hide()
        self.ui.led_axis_c.hide()

        self.ui.lbl_heigth_fix.hide()
        self.ui.led_height.hide()

        self.ui.lbl_depth_fix.hide()
        self.ui.led_depth.hide()

        self.ui.lbl_length_fix.hide()
        self.ui.led_length.hide()

        self.ui.lbl_width_fix.hide()
        self.ui.led_width.hide()

        self.ui.lbl_r1_fix.hide()
        self.ui.led_r1.hide()

        self.ui.lbl_r2_fix.hide()
        self.ui.led_r2.hide()
        
        # self.ui.btn_calculate.hide()
        self.ui.btn_calculate.setEnabled(False)
    
    def show_fields(self):

        solid = str(self.ui.cb_shape.currentText())

        if solid == "Hollow Sphere":
            self.ui.lbl_radius_fix.show()
            self.ui.led_radius.show()
        elif solid == "Solid Sphere":
            self.ui.lbl_radius_fix.show()
            self.ui.led_radius.show()
        elif solid == "Solid Ellipsoid":
            self.ui.lbl_axis_a_fix.show()
            self.ui.led_axis_a.show()
            self.ui.lbl_axis_b_fix.show()
            self.ui.led_axis_b.show()
            self.ui.lbl_axis_c_fix.show()
            self.ui.led_axis_c.show()
        elif solid == "Right Circular Cone":
            self.ui.lbl_radius_fix.show()
            self.ui.led_radius.show()
            self.ui.lbl_heigth_fix.show()
            self.ui.led_height.show()
        elif solid == "Solic Cuboid":
            self.ui.lbl_heigth_fix.show()
            self.ui.led_height.show()
            self.ui.lbl_depth_fix.show()
            self.ui.led_depth.show()
            self.ui.lbl_width_fix.show()
            self.ui.led_width.show()
        elif solid == "Slender Rod - End":
            self.ui.lbl_length_fix.show()
            self.ui.led_length.show()
        elif solid == "Slender Rod - Center":
            self.ui.lbl_length_fix.show()
            self.ui.led_length.show()
        elif solid == "Solid Cylinder":
            self.ui.lbl_radius_fix.show()
            self.ui.led_radius.show()
            self.ui.lbl_heigth_fix.show()
            self.ui.led_height.show()
        elif solid == "TW Cylindrical Tube":
            self.ui.lbl_r1_fix.show()
            self.ui.led_r1.show()
            self.ui.lbl_r2_fix.show()
            self.ui.led_r2.show()
            self.ui.lbl_heigth_fix.show()
            self.ui.led_height.show()

    def check_solid(self):

        solid = str(self.ui.cb_shape.currentText())

        self.ui.gb_check.show()
        self.ui.gb_input.show()
        
        # image paths
        app_path = os.path.abspath(os.getcwd())
        img_folder = "images"
        path = os.path.join(app_path, img_folder)
        model_file = "model_matrix.svg"

        if not self.first_exec:
            self.ui.figure_layout.removeWidget(self.fig_widget)
            self.ui.matrix_layout.removeWidget(self.matrix_widget)
            self.ui.model_layout.removeWidget(self.model_widget)
            self.fig_widget.deleteLater()
            self.matrix_widget.deleteLater()
            self.model_widget.deleteLater()

        if solid == "Hollow Sphere":
            matrix_file = "hollow_sphere_matrix.svg"
            fig_file = "hollow_sphere.svg"
        elif solid == "Solid Sphere":
            matrix_file = "solid_sphere_matrix.svg"
            fig_file = "solid_sphere.svg"
        elif solid == "Solid Ellipsoid":
            matrix_file = "solid_ellipsoid_matrix.svg"
            fig_file = "solid_ellipsoid.svg"
        elif solid == "Right Circular Cone":
            matrix_file = "right_circular_cone_matrix.svg"
            fig_file = "right_circular_cone.svg"
        elif solid == "Solic Cuboid":
            matrix_file = "solid_cuboid_matrix.svg"
            fig_file = "solid_cuboid.svg"
        elif solid == "Slender Rod - End":
            matrix_file = "slender_rod_end_matrix.svg"
            fig_file = "slender_rod_end.svg"
        elif solid == "Slender Rod - Center":
            matrix_file = "slender_rod_center_matrix.svg"
            fig_file = "slender_rod_center.svg"
        elif solid == "Solid Cylinder":
            matrix_file = "solid_cylinder_matrix.svg"
            fig_file = "solid_cylinder.svg"
        elif solid == "TW Cylindrical Tube":
            matrix_file = "thick_walled_cylindrical_tube_open_ends_matrix.svg"
            fig_file = "thick_walled_cylindrical_tube_open_ends.svg"

        # figure
        fig_path = os.path.normpath(os.path.join(path, fig_file))
        self.get_size = QSvgRenderer(fig_path)
        self.fig_widget = QSvgWidget(fig_path)
        # self.fig_widget.setFixedSize(self.get_size.defaultSize())
        self.ui.figure_layout.addWidget(self.fig_widget, Qt.AlignCenter, Qt.AlignCenter)

        # matrix
        matrix_path = os.path.normpath(os.path.join(path, matrix_file))
        self.get_size = QSvgRenderer(matrix_path)
        self.matrix_widget = QSvgWidget(matrix_path)
        # self.matrix_widget.setFixedSize(self.get_size.defaultSize() / 4)
        self.ui.matrix_layout.addWidget(self.matrix_widget, Qt.AlignCenter, Qt.AlignCenter)

        # model
        model_path = os.path.normpath(os.path.join(path, model_file))
        self.get_size = QSvgRenderer(model_path)
        self.model_widget = QSvgWidget(model_path)
        # self.model_widget.setFixedSize(self.get_size.defaultSize())
        self.ui.model_layout.addWidget(self.model_widget, Qt.AlignCenter, Qt.AlignCenter)

        self.first_exec = False

        self.hide_fields()
        self.show_fields()
        self.check_values()

    def check_values(self):
        # to allow double values only
        self.only_double = QDoubleValidator()
        self.ui.led_mass.setValidator(self.only_double)
        self.ui.led_mass.setMaxLength(10)
        self.ui.led_radius.setValidator(self.only_double)
        self.ui.led_radius.setMaxLength(10)
        self.ui.led_axis_a.setValidator(self.only_double)
        self.ui.led_axis_a.setMaxLength(10)
        self.ui.led_axis_b.setValidator(self.only_double)
        self.ui.led_axis_b.setMaxLength(10)
        self.ui.led_axis_c.setValidator(self.only_double)
        self.ui.led_axis_c.setMaxLength(10)
        self.ui.led_height.setValidator(self.only_double)
        self.ui.led_height.setMaxLength(10)
        self.ui.led_depth.setValidator(self.only_double)
        self.ui.led_depth.setMaxLength(10)
        self.ui.led_length.setValidator(self.only_double)
        self.ui.led_length.setMaxLength(10)
        self.ui.led_width.setValidator(self.only_double)
        self.ui.led_width.setMaxLength(10)
        self.ui.led_r1.setValidator(self.only_double)
        self.ui.led_r1.setMaxLength(10)
        self.ui.led_r2.setValidator(self.only_double)
        self.ui.led_r2.setMaxLength(10)

    def enable_calculation(self):

        solid = str(self.ui.cb_shape.currentText())
        self.ui.cb_shape.setEnabled(False)

        if solid == "Hollow Sphere":
            if len(self.ui.led_mass.text()) > 0 \
                and len(self.ui.led_radius.text()) > 0:
                self.ui.btn_calculate.setEnabled(True)
        elif solid == "Solid Sphere":
            if len(self.ui.led_mass.text()) > 0 \
                and len(self.ui.led_radius.text()) > 0:
                self.ui.btn_calculate.setEnabled(True)
        elif solid == "Solid Ellipsoid":
            if len(self.ui.led_mass.text()) > 0 \
                and len(self.ui.led_axis_a.text()) > 0 \
                and len(self.ui.led_axis_b.text()) > 0 \
                and len(self.ui.led_axis_c.text()) > 0:
                self.ui.btn_calculate.setEnabled(True)
        elif solid == "Right Circular Cone":
            if len(self.ui.led_mass.text()) > 0 \
                and len(self.ui.led_radius.text()) > 0 \
                and len(self.ui.led_height.text()) > 0:
                self.ui.btn_calculate.setEnabled(True)
        elif solid == "Solic Cuboid":
            if len(self.ui.led_mass.text()) > 0 \
                and len(self.ui.led_height.text()) > 0 \
                and len(self.ui.led_depth.text()) > 0 \
                and len(self.ui.led_width.text()) > 0:
                self.ui.btn_calculate.setEnabled(True)
        elif solid == "Slender Rod - End":
            if len(self.ui.led_mass.text()) > 0 \
                and len(self.ui.led_length.text()) > 0:
                self.ui.btn_calculate.setEnabled(True)
        elif solid == "Slender Rod - Center":
            if len(self.ui.led_mass.text()) > 0 \
                and len(self.ui.led_length.text()) > 0:
                self.ui.btn_calculate.setEnabled(True)
        elif solid == "Solid Cylinder":
            if len(self.ui.led_mass.text()) > 0 \
                and len(self.ui.led_radius.text()) > 0 \
                and len(self.ui.led_height.text()) > 0:
                self.ui.btn_calculate.setEnabled(True)
        elif solid == "TW Cylindrical Tube":
            if len(self.ui.led_mass.text()) > 0 \
                and len(self.ui.led_height.text()) > 0 \
                and len(self.ui.led_r1.text()) > 0 \
                and len(self.ui.led_r2.text()) > 0:
                self.ui.btn_calculate.setEnabled(True)

    def calculate(self):
        # variables
        m = float(self.ui.led_mass.text())      

        solid = str(self.ui.cb_shape.currentText())

        self.ui.txtb_results.clear()

        if solid == "Hollow Sphere":
            r = float(self.ui.led_radius.text())
            matrix = self.eq.hollow_sphere(m, r)
        elif solid == "Solid Sphere":
            r = float(self.ui.led_radius.text())
            matrix = self.eq.solid_sphere(m, r)
        elif solid == "Solid Ellipsoid":
            a = float(self.ui.led_axis_a.text())
            b = float(self.ui.led_axis_b.text())
            c = float(self.ui.led_axis_c.text())
            matrix = self.eq.solid_ellipsoid(m, a, b, c)
        elif solid == "Right Circular Cone":
            r = float(self.ui.led_radius.text())
            h = float(self.ui.led_height.text())
            matrix = self.eq.right_circular_cone(m, r, h)
        elif solid == "Solic Cuboid":
            w = float(self.ui.led_width.text())
            d = float(self.ui.led_depth.text())
            h = float(self.ui.led_height.text())
            matrix = self.eq.solid_cuboid(m, w, h, d)
        elif solid == "Slender Rod - End":
            l = float(self.ui.led_length.text())
            matrix = self.eq.slender_rod_end(m, l)
        elif solid == "Slender Rod - Center":
            l = float(self.ui.led_length.text())
            matrix = self.eq.slender_rod_center(m, l)
        elif solid == "Solid Cylinder":
            h = float(self.ui.led_height.text())
            r = float(self.ui.led_radius.text())
            matrix = self.eq.solid_cylinder(m, h, r)
        elif solid == "TW Cylindrical Tube":
            h = float(self.ui.led_height.text())
            r1 = float(self.ui.led_r1.text())
            r2 = float(self.ui.led_r2.text())
            matrix = self.eq.thick_walled_tube(m, r1, r2, h)

        print(matrix)
        self.ui.gb_results.show()

        result = 'ixx="{}" ixy="{}" ixz="{}" iyx="{}" iyy="{}" iyz="{}" izx="{}" izy="{}" izz="{}"'.format(matrix[0][0], 
                                                                                                            matrix[0][1],
                                                                                                            matrix[0][2],
                                                                                                            matrix[1][0],
                                                                                                            matrix[1][1],
                                                                                                            matrix[1][2],
                                                                                                            matrix[2][0],
                                                                                                            matrix[2][1],
                                                                                                            matrix[2][2],      
                                                                                                            )

        self.ui.txtb_results.append(str(matrix))
        self.ui.txtb_results.append("")
        self.ui.txtb_results.append("or")
        self.ui.txtb_results.append("")
        self.ui.txtb_results.append(result)
        self.ui.cb_shape.setEnabled(True)

    def save_file(self):
        # This will let you access the test in your QTextBrowser
        text = self.ui.txtb_results.toPlainText()
        
        # Finally this will Save your file to the path selected.
        with open("results.txt", 'w') as file:
            file.write(text)
        

# execution code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
