from events import *

class SignalKnowledge:
    lookup_table = {
        'time': (TimeHandler, None, 'Time'),
        'events': (PropofolHandler, ('data/S$_events.csv',), 'Events'),
        'LF': (RRHandler, ('data/S$_LF.csv', 'data/S$_t_HRV.csv'), 'LF'),
        'HF': (RRHandler, ('data/S$_HF.csv', 'data/S$_t_HRV.csv'), 'HF'),
        'sigmaRR': (RRHandler, ('data/S$_sigmaRR.csv', 'data/S$_t_HRV.csv'), 'SigmaRR'),
        'muRR': (RRHandler, ('data/S$_muRR.csv', 'data/S$_t_HRV.csv'), 'MuRR'),
        'sigmaHR': (RRHandler, ('data/S$_sigmaHR.csv', 'data/S$_t_HRV.csv'), 'SigmaHR'),
        'muHR': (RRHandler, ('data/S$_muHR.csv', 'data/S$_t_HRV.csv'), 'MuHR')
    }

    def getOutputTag(tag):
        handler_class, argument, name = SignalKnowledge.lookup_table[tag]
        return name


class HandlerFactory(SignalKnowledge):

    def generate(tag, parameters):
        handler_class, argument, name = HandlerFactory.lookup_table[tag]
        handler = handler_class(parameters, argument, name)
        return handler
