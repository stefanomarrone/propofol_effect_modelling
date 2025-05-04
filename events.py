import numpy as np
from core import BaseHandler, SeparateHandler

class TimeHandler(BaseHandler):
    def run(self):
        final_list = []
        for p in self.patients:
            final_list.extend(list(np.arange(self.min, self.max, self.step)))
        dictionary = {self.name: final_list}
        return dictionary


class PropofolHandler(SeparateHandler):

    def find_interval(self, time_value, times_values):
        min_interval = None
        max_interval = None
        index = 0
        found = False
        while index < len(times_values) - 1 and not found:
            this_time_value = times_values[index][0]
            next_time_value = times_values[index + 1][0]
            found = this_time_value <= time_value < next_time_value
            if found:
                min_interval = times_values[index]
                max_interval = times_values[index + 1]
            index += 1
        if not found:
            max_interval = times_values[len(times_values) - 1]
            min_interval = times_values[len(times_values) - 1]
        return time_value, min_interval, max_interval

    def get_linear_imterpolation(self, min_time_value, max_time_value, actual_time):
        min_time, min_value = min_time_value
        max_time, max_value = max_time_value
        if max_time - min_time == 0.0:
            y = max_value
        else:
            y = (actual_time - min_time) * max_value / (max_time - min_time)
            y -= (actual_time - max_time) * min_value / (max_time - min_time)
        return y

    def generate_single_patient_measure(self, patient_number):
        values = [0., 0., 1., 2., 3., 4., 5., 3.75, 2.5, 1.25, 0.]
        csv_filename = self.extra_argument['csv_filename']
        csv_filename = self.get_concrete_string(csv_filename, patient_number)
        filehandler = open(csv_filename, 'r')
        times = ['0']
        times.extend(list(filehandler.readline()[:-1].split(',')))
        times = [float(time) for time in times]
        filehandler.close()
        times_values = list(zip(times, values))
        actual_times = list(np.arange(self.min, self.max, self.step))
        actual_intervals = [self.find_interval(actual_time, times_values) for actual_time in actual_times]
        actual_values = [self.get_linear_imterpolation(min_tv, max_tv, a_time)
                         for a_time, min_tv, max_tv in actual_intervals]
        return actual_values

    def decompress_arguments(self, compressed_arguments):
        argument_dictionary = {'csv_filename': compressed_arguments[0]}
        return argument_dictionary


class RRHandler(SeparateHandler):

    def averag_in_period(self, min_time, max_time, list_of_values):
        retval = 0
        slot_points = list(filter(lambda x: min_time <= x[0] < max_time, list_of_values))
        slot_values = list(map(lambda x: x[1], slot_points))
        if len(slot_values) > 0:
            retval = sum(slot_values) / len(slot_values)
        return retval

    def generate_single_patient_measure(self, patient_number):
        actual_times = list(np.arange(self.min, self.max, self.step))
        time_filename = self.extra_argument['time_filename']
        time_filename = self.get_concrete_string(time_filename, patient_number)
        time_file_handler = open(time_filename, 'r')
        times = list(time_file_handler.readline()[:-1].split(','))
        times = [float(time) for time in times]
        time_file_handler.close()
        value_filename = self.extra_argument['csv_filename']
        value_filename = self.get_concrete_string(value_filename, patient_number)
        value_file_handler = open(value_filename, 'r')
        values = list(value_file_handler.readline()[:-1].split(','))
        values = [float(value) for value in values]
        value_file_handler.close()
        data = list(zip(times, values))
        actual_values = []
        counter = 1
        for actual_time in actual_times:
            #print(str(counter) + '/' + str(len(actual_times)))
            counter += 1
            actual_value = self.averag_in_period(actual_time - self.step / 2, actual_time + self.step / 2, data)
            actual_values.append(actual_value)
        return actual_values

    def decompress_arguments(self, compressed_arguments):
        argument_dictionary = {
            'csv_filename': compressed_arguments[0],
            'time_filename': compressed_arguments[1]
        }
        return argument_dictionary

