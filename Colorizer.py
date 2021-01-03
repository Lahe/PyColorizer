from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from app.ui_GUI import Ui_MainWindow
from app.colorizer_helpers import *
import traceback


class Colorizer(QMainWindow, Ui_MainWindow):
    inPath = ''
    model = None
    modelName = ''

    def __init__(self, parent=None):
        super(Colorizer, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Colorizer")
        self.setStyle(QApplication.setStyle('windows'))

        self.threadpool = QThreadPool()

        movie = QMovie('resources/spinner.gif')
        self.loadingSpinner.setMovie(movie)
        movie.start()
        self.loadingSpinner.hide()
        self.loadingText.hide()

        self.colorizeImageBtn.hide()
        self.colorizeVideoBtn.hide()

    @pyqtSlot()
    def getModel(self):
        if self.modelDropdown.currentIndex() == 1:
            self.model = getPretrainedModel('models/colorization_deploy_v2.prototxt',
                                            'models/colorization_release_v2.caffemodel',
                                            'models/pts_in_hull.npy')
            self.modelName = 'pretrained'
        elif self.modelDropdown.currentIndex() == 2:
            self.model = getSelftrainedModel('models/1000suvalised500epoch2')
            self.modelName = 'selftrained'
        elif self.modelDropdown.currentIndex() == 3:
            self.model = getSelftrainedModelFaces('models/1000TrFaces500epoch2')
            self.modelName = 'selftrained'
        else:
            self.model = None
            self.modelName = ''

    @pyqtSlot()
    def importImage(self):
        self.inPath, _ = QFileDialog.getOpenFileName(self, "Import File", "",
                                                     "All supported formats (*.png *.jpg *.jpeg);;"
                                                     "PNG files (*.png);;"
                                                     "JPG files (*.jpg);;"
                                                     "JPEG files (*.jpeg)")
        if self.inPath != '':
            self.input.setCurrentIndex(0)
            self.colorizeImageBtn.show()
            self.colorizeVideoBtn.hide()
            self.imgLabelIn.setPixmap(QPixmap(self.inPath))
        else:
            QMessageBox.warning(self, "Error", "Import not specified!");

    @pyqtSlot()
    def importVideo(self):
        self.inPath, _ = QFileDialog.getOpenFileName(self, "Import File", "",
                                                     "MP4 Videos (*.mp4)")
        if self.inPath != '':
            self.input.setCurrentIndex(1)
            self.colorizeVideoBtn.show()
            self.colorizeImageBtn.hide()
            self.video_in.playVideo(self.inPath)
        else:
            QMessageBox.warning(self, "Error", "Import not specified!")

    @pyqtSlot()
    def colorizeImageClicked(self):
        if self.model is not None:
            self.loadingSpinner.show()
            self.loadingText.show()
            self.output.setCurrentIndex(0)
            worker = Worker(self.colorizeImage)
            self.threadpool.start(worker)
        else:
            QMessageBox.warning(self, "Error", "Choose a model!")

    def colorizeImage(self):
        try:
            image_rgb = readImageFromFile(self.inPath)
            colorized = colorizeImage(self.model, image_rgb, self.modelName)

            colorized_path = self.inPath.rsplit('.')[0] + "_colorized.jpg"
            cv.imwrite(colorized_path, colorized)

            self.loadingSpinner.hide()
            self.loadingText.hide()
            self.imgLabelOut.setPixmap(QPixmap(colorized_path))
        except:
            QMessageBox.warning(self, "Error", "Image colorizing failed!")

    @pyqtSlot()
    def colorizeVideoClicked(self):
        if self.model is not None:
            self.loadingSpinner.show()
            self.loadingText.show()
            self.output.setCurrentIndex(1)
            worker = Worker(self.colorizeVideo)
            self.threadpool.start(worker)
        else:
            QMessageBox.warning(self, "Error", "Choose a model!")

    def colorizeVideo(self):
        try:
            outPath = self.inPath.rsplit('.')[0] + "_colorized.mp4"
            if outPath == '':
                outPath = 'out.mp4'

            cap = cv.VideoCapture(self.inPath)
            fourcc = cv.VideoWriter_fourcc(*'mp4v')
            writer = cv.VideoWriter(outPath, fourcc, 30, (640, 480))

            while True:
                hasFrame, frame = cap.read()

                if not hasFrame:
                    break
                colorized_frame = colorizeImage(self.model, frame, self.modelName)
                writer.write(cv.resize(colorized_frame, (640, 480)))

            self.loadingSpinner.hide()
            self.loadingText.hide()
            self.video_out.playVideo(outPath)
        except:
            QMessageBox.warning(self, "Error", "Video colorizing failed!")


# Allikas: https://www.learnpyqt.com/tutorials/multithreading-pyqt-applications-qthreadpool/
class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        # self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Colorizer()
    mainWindow.show()
    sys.exit(app.exec_())
