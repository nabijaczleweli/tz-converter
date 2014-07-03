import sys
import os
real_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(u'%s/lib' % real_path)
from PySide.QtGui import QWidget, QGroupBox, QVBoxLayout, QHBoxLayout, QTimeEdit, QCalendarWidget, QComboBox, \
    QPushButton, QIcon
from PySide.QtCore import QTime, QDate
from tzlocal import get_localzone
import timezone_info
import datetime
from delorean import Delorean


class MainWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        # Set Time One Group
        self.time_one_calendar = QCalendarWidget()
        self.time_one_country_combobox = QComboBox()
        self.time_one_vbox = QVBoxLayout()
        self.time_one_groupbox = QGroupBox("Time One")
        self.time_one_bottom_hbox = QHBoxLayout()
        self.time_one_time_edit = QTimeEdit()
        self.time_one_default_button = QPushButton()
        self.time_one_default_button.setIcon(QIcon("%s/icons/gnome-set-time.png" % real_path))
        self.time_one_default_button.setMaximumSize(50, 50)
        self.time_one_bottom_hbox.addWidget(self.time_one_time_edit)
        self.time_one_bottom_hbox.addWidget(self.time_one_default_button)
        self.time_one_vbox.addWidget(self.time_one_country_combobox)
        self.time_one_vbox.addWidget(self.time_one_calendar)
        self.time_one_vbox.addLayout(self.time_one_bottom_hbox)
        self.time_one_groupbox.setLayout(self.time_one_vbox)

        # Set Time Two Group
        self.time_two_groupbox = QGroupBox("Time Two")
        self.time_two_calendar = QCalendarWidget()
        self.time_two_vbox = QVBoxLayout()
        self.time_two_country_combobox = QComboBox()
        self.time_two_bottom_hbox = QHBoxLayout()
        self.time_two_time_edit = QTimeEdit()
        self.time_two_default_button = QPushButton()
        self.time_two_default_button.setIcon(QIcon("%s/icons/gnome-set-time.png" % real_path))
        self.time_two_default_button.setMaximumSize(50, 50)
        self.time_two_bottom_hbox.addWidget(self.time_two_time_edit)
        self.time_two_bottom_hbox.addWidget(self.time_two_default_button)
        self.time_two_vbox.addWidget(self.time_two_country_combobox)
        self.time_two_vbox.addWidget(self.time_two_calendar)
        self.time_two_vbox.addLayout(self.time_two_bottom_hbox)
        self.time_two_groupbox.setLayout(self.time_two_vbox)

        # Set main layout
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.time_one_groupbox)
        self.main_layout.addWidget(self.time_two_groupbox)
        self.setLayout(self.main_layout)

        # Wire-up your widgets!
        self.time_one_connect()
        self.time_two_connect()
        self.time_one_default_button.clicked.connect(self.set_local_time_one)
        self.time_two_default_button.clicked.connect(self.set_local_time_two)

        # Set the local time for time one
        self.set_local_country()
        self.set_local_time_one()

        # Finally, convert the second time based on the first
        self.convert_timeone_to_timetwo()

    def set_local_country(self):
        global_timezone_list = timezone_info.get_global_timezone_list()
        local_tz_index = global_timezone_list.index(str(get_localzone()))
        self.time_one_country_combobox.addItems(global_timezone_list)
        self.time_one_country_combobox.setCurrentIndex(local_tz_index)
        self.time_two_country_combobox.addItems(global_timezone_list)

    @staticmethod
    def get_local_times():
        local_hour = datetime.datetime.now().strftime("%H")
        local_minute = datetime.datetime.now().strftime("%M")
        local_current_time = QTime(int(local_hour), int(local_minute), 0, 0)

        return local_current_time

    def set_local_time_one(self):

        # Set time for one time
        local_current_time = self.get_local_times()
        self.time_one_time_edit.setTime(local_current_time)

        # Set date for one calendar
        self.time_one_calendar.setSelectedDate(QDate.currentDate())

        #convert the second time based on the first
        self.convert_timeone_to_timetwo()

    def set_local_time_two(self):

        # Set time for one time
        local_current_time = self.get_local_times()
        self.time_two_time_edit.setTime(local_current_time)

        # Set date for one calendar
        self.time_two_calendar.setSelectedDate(QDate.currentDate())

        #convert the first time based on the second
        self.convert_timetwo_to_timeone()

    def time_one_connect(self):
        self.time_one_country_combobox.activated.connect(self.convert_timeone_to_timetwo)
        self.time_one_calendar.clicked.connect(self.convert_timeone_to_timetwo)
        self.time_one_time_edit.timeChanged.connect(self.convert_timeone_to_timetwo)

    def time_two_connect(self):
        self.time_two_country_combobox.activated.connect(self.convert_timeone_to_timetwo)
        self.time_two_calendar.clicked.connect(self.convert_timetwo_to_timeone)
        self.time_two_time_edit.timeChanged.connect(self.convert_timetwo_to_timeone)

    def time_one_disconnect(self):
        self.time_one_calendar.clicked.disconnect()
        self.time_one_country_combobox.activated.disconnect()
        self.time_one_time_edit.timeChanged.disconnect()

    def time_two_disconnect(self):
        self.time_two_calendar.clicked.disconnect()
        self.time_two_country_combobox.activated.disconnect()
        self.time_two_time_edit.timeChanged.disconnect()

    def clear_combo_boxes(self):
        self.time_one_country_combobox.clear()
        self.time_two_country_combobox.clear()

    def convert_timeone_to_timetwo(self):

        #Diconnecting time two widgets,so that they do not run
        self.time_two_disconnect()

        date_time_one = datetime.datetime(self.time_one_calendar.selectedDate().year(),
                                          self.time_one_calendar.selectedDate().month(),
                                          self.time_one_calendar.selectedDate().day(),
                                          self.time_one_time_edit.time().hour(),
                                          self.time_one_time_edit.time().minute())

        d = Delorean(datetime=date_time_one, timezone=self.time_one_country_combobox.currentText())
        d.shift(self.time_two_country_combobox.currentText())
        new_timezone_two = d.datetime

        new_date_two = QDate(new_timezone_two.year, new_timezone_two.month, new_timezone_two.day)
        self.time_two_calendar.setSelectedDate(new_date_two)

        new_time_two = QTime(int(new_timezone_two.hour), int(new_timezone_two.minute))
        self.time_two_time_edit.setTime(new_time_two)

        #Reconnect time one widgets.
        self.time_two_connect()

    def convert_timetwo_to_timeone(self):

        #Diconnecting time one widgets,so that they do not run
        self.time_one_disconnect()

        date_time_two = datetime.datetime(self.time_two_calendar.selectedDate().year(),
                                          self.time_two_calendar.selectedDate().month(),
                                          self.time_two_calendar.selectedDate().day(),
                                          self.time_two_time_edit.time().hour(),
                                          self.time_two_time_edit.time().minute())


        d = Delorean(datetime=date_time_two, timezone=self.time_two_country_combobox.currentText())
        d.shift(self.time_one_country_combobox.currentText())
        new_timezone_one = d.datetime

        new_date_one = QDate(new_timezone_one.year, new_timezone_one.month, new_timezone_one.day)
        self.time_one_calendar.setSelectedDate(new_date_one)

        new_time_one = QTime(int(new_timezone_one.hour), int(new_timezone_one.minute))
        self.time_one_time_edit.setTime(new_time_one)

        #Reconnect time one widgets
        self.time_one_connect()
