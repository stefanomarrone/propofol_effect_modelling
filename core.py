
class BaseHandler:
    def __init__(self, params, arg, nname):
        self.name = nname
        self.patients = params.patients
        self.min = params.min
        self.max = params.max
        self.step = params.step
        self.extra_argument = self.decompress_arguments(arg)

    def run(self):
        pass

    def decompress_arguments(self, compressed_arguments):
        pass

class MultipleHandler(BaseHandler):

    def run(self):
        average_measures = []
        measures_of_patients = [self.generate_single_patient_measure(patient) for patient in self.patients]
        for i, _ in enumerate(measures_of_patients[0]):
            measures_column = [row[i] for row in measures_of_patients]
            average = float(sum(measures_column))/float(len(measures_column))
            average_measures.append(average)
        dictionary = {self.name: average_measures}
        return dictionary

    def get_concrete_string(self, old_string, patient_number):
        retval = old_string.replace('$', str(patient_number))
        return retval

    def generate_single_patient_measure(self, patient_number):
        pass

    def decompress_arguments(self, compressed_arguments):
        pass


class SeparateHandler(BaseHandler):

    def run(self):
        innerdictionay = {}
        for patient in self.patients:
            tag = "patient_" + str(patient)
            measures_of_patients = self.generate_single_patient_measure(patient)
            innerdictionay[tag] = measures_of_patients
        dictionary = {self.name: innerdictionay}
        return dictionary

    def get_concrete_string(self, old_string, patient_number):
        retval = old_string.replace('$', str(patient_number))
        return retval

    def generate_single_patient_measure(self, patient_number):
        pass

    def decompress_arguments(self, compressed_arguments):
        pass


