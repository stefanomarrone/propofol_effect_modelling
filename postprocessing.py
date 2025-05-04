from core import BaseHandler
from factory import SignalKnowledge
import numpy as np

class DictionaryHandler(BaseHandler):
    def handles(self, input_dictionary, elems):
        output_dictionary = {'Patient': []}
        actual_elems = list(map(lambda x: SignalKnowledge.getOutputTag(x), elems))
        for output_tag in actual_elems:
            output_dictionary[output_tag] = []
        output_dictionary['Time'] = input_dictionary['Time']
        actual_elems.remove('Time')
        chunk_length = len(list(np.arange(self.min, self.max, self.step)))
        for i in self.patients:
            tag = 'patient_' + str(i)
            temporary_patient = [tag] * chunk_length
            output_dictionary['Patient'].extend(temporary_patient)
            for ae in actual_elems:
                output_dictionary[ae].extend(input_dictionary[ae][tag])
            pass
        return output_dictionary

