from pandas import DataFrame
from parameters import Parameters
from factory import HandlerFactory
from postprocessing import DictionaryHandler


def single_execution(params, elems, outfile):
    dictionary = dict()
    for element in elems:
        print(element)
        handler = HandlerFactory.generate(element, params)
        temporary_dictionary = handler.run()
        dictionary.update(temporary_dictionary)
    dhandler = DictionaryHandler(params, None, None)
    dictionary = dhandler.handles(dictionary, elements)
    dataframe = DataFrame(dictionary)
    dataframe.to_csv(outfile)


if __name__ == '__main__':
    elements = ['time', 'events', 'sigmaHR', 'muHR', 'sigmaRR', 'muRR', 'LF', 'HF']
    training = Parameters([1, 2, 3, 4, 5, 6], 0, 12000, 15)
    testing = Parameters([7, 8, 9], 0, 12000, 15)
    print('Start training')
    single_execution(training, elements, 'training_completo.csv')
    print('Start testing')
    single_execution(testing, elements, 'testing.csv')
