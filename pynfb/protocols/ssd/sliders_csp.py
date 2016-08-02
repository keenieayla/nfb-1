from PyQt4 import QtGui, QtCore
from pynfb.widgets.parameter_slider import ParameterSlider


class Sliders(QtGui.QWidget):
    def __init__(self, sample_freq=1000):
        super(Sliders, self).__init__()
        h_layout = QtGui.QHBoxLayout()
        v_layout = QtGui.QVBoxLayout()
        self.setLayout(h_layout)
        h_layout.addLayout(v_layout)
        self.parameters = {}

        self.defaults = {'bandpass_low': 8,
                        'regularizator': 0.05,
                        'bandpass_high': 12}


        # regularizator slider
        self.parameters['regularizator'] = ParameterSlider('Regularization coefficient:', 0, 10, 0.5,
                                                           value=self.defaults['regularizator'])
        self.parameters['regularizator'].slider.valueChanged.connect(lambda: self.revert_button.setEnabled(True))
        v_layout.addWidget(self.parameters['regularizator'])

        # central bandpass_low slider
        self.parameters['bandpass_low'] = ParameterSlider('Bandpass low:', 0, sample_freq/2, sample_freq/10,
                                                          value=self.defaults['bandpass_low'])
        self.parameters['bandpass_low'].slider.valueChanged.connect(lambda: self.revert_button.setEnabled(True))
        v_layout.addWidget(self.parameters['bandpass_low'])

        # flanker bandpass_low
        self.parameters['bandpass_high'] = ParameterSlider('Bandpass high:', 0, sample_freq/2, sample_freq/10,
                                                           value=self.defaults['bandpass_high'])
        self.parameters['bandpass_high'].slider.valueChanged.connect(lambda: self.revert_button.setEnabled(True))
        v_layout.addWidget(self.parameters['bandpass_high'])

        button_layout = QtGui.QVBoxLayout()
        h_layout.addLayout(button_layout)
        # apply button
        self.apply_button = QtGui.QPushButton('Apply')
        button_layout.addWidget(self.apply_button)

        # revert button
        self.revert_button = QtGui.QPushButton('Restore\ndefaults')
        self.revert_button.setEnabled(False)
        self.revert_button.clicked.connect(self.restore_defaults)
        button_layout.addWidget(self.revert_button)

    def restore_defaults(self):
        for key in self.defaults.keys():
            self.parameters[key].setValue(self.defaults[key])
        self.revert_button.setEnabled(False)

    def getValues(self):
        values = dict([(key, param.getValue()) for key, param in self.parameters.items()])
        return values


if __name__ == '__main__':
    app = QtGui.QApplication([])
    widget = Sliders()
    widget.show()
    app.exec_()
