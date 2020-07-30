import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QThread, pyqtSignal,Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import serial.tools.list_ports
from w import *






class back_Thread(QThread):
    countChanged = pyqtSignal(object)
    SerialIn_name = pyqtSignal(str)
    serial_data = pyqtSignal(object)
    clear_signal = pyqtSignal()
    P_count = 0
    def __init__(self,parent=None):
        super().__init__(parent)
        self.S_flag = False
        self.data_flag = False

    def stop_th(self):
        self.S_flag=True

    def save_data(self):
        self.data_flag = True



    def run(self):

        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) <= 0:
            print("The Serial port can't find!")
        else:
            port_list_0 = list(port_list[0])
            port_serial = port_list_0[0]
            SerialIn = serial.Serial(port_serial, 115200)
            self.SerialIn_name.emit(SerialIn.name)

        ys = []
        ys_txt=[]
        head=0
        while (not self.S_flag):
            data = int(SerialIn.readline())
            ys.append(data)
            a = len(ys)

            if self.P_count < L:
                self.P_count += 1
                self.countChanged.emit(self.P_count)


            if a > L:
                ys = ys[-L:]
                a = L
            if a == L:
                self.serial_data.emit(ys)
                if self.data_flag:
                    head=head+1
                    fp = open(str(head) + ".txt", "w")
                    fp.writelines(ys_txt)
                    self.data_flag = False
                    fp.close()
                    print('save ok!')







        SerialIn.close()
        self.clear_signal.emit()










class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes= fig.add_subplot(1, 1, 1)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)



    def chart_clear(self):
        self.axes.clear()
        self.draw()


    def chart_update_ori(self,value):
        self.axes.clear()
        self.axes.plot(value, 'r')
        self.axes.grid(True)
        self.draw()




class MainWindow(QWidget):
    def __init__(self,parent=None):
        super(self.__class__, self).__init__()
        self.ui=Ui_HB_Form()
        self.ui.setupUi(self)
        self.main_widget = QtWidgets.QWidget(self)
        self.ui.lineEdit.setAlignment(Qt.AlignCenter)
        self.ui.canvas = MyMplCanvas(self.main_widget, width=6, height=6, dpi=100)
        self.ui.verticalLayout.addWidget(self.ui.canvas)
        self.ui.pushButton_start.clicked.connect(self.start)
        self.ui.pushButton_stop.clicked.connect(self.stop)
        self.ui.pushButton_save.clicked.connect(self.save_file)
        self.ui.serial_portLineEdit.setEnabled(False)







    def start(self):
        global L
        if self.ui.lineEdit.text()=='':
            L=100
        else:
            L = int(self.ui.lineEdit.text())
        self.ui.progressBar.setMaximum(L)
        self._back_Thread = back_Thread()
        self._back_Thread.serial_data.connect(self.ui.canvas.chart_update_ori)
        self._back_Thread.countChanged.connect(self.onCountChanged)
        self._back_Thread.SerialIn_name.connect(self.port_name)
        self._back_Thread.start()
        self.ui.pushButton_start.setEnabled(False)

    def stop(self):
        self._back_Thread.stop_th()
        self.ui.pushButton_start.setEnabled(True)




    def port_name(self, text):
        self.ui.serial_portLineEdit.setText(text)
        self.ui.serial_portLineEdit.setAlignment(Qt.AlignCenter)


    def onCountChanged(self, value):
        self.ui.progressBar.setValue(value)

    def save_file(self):
        self._back_Thread.save_data()


