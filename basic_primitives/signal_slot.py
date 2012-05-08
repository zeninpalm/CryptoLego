__author__ = 'ThinkPad'

class SignalSupporter(object):
    def __init__(self, *signals):
        self._signals = []
        for s in signals:
            self._signals.append(s)

    def __call__(self, cls):
        supported_signals = self._signals

        class wrapper(cls):
            def __init__(self, *args, **kwargs):
                cls.__init__(self, *args, **kwargs)
                self._signal_handlers = {}
                for signal in supported_signals:
                    self._signal_handlers[signal] = []

            def emit(self, signal, **signal_parameters):
                handlers = self._signal_handlers[signal]
                for handler in handlers:
                    handler(**signal_parameters)

        return wrapper

def slot_supporter(*args):
    pairs = []
    for arg in args:
        pairs.append('"' + arg + '":self.' + arg + '_handler')

    dict_str = ",".join(pairs)
    code_to_eval = '{' + dict_str + '}'

    def outer(func):
        def wrapped_init(self, *args, **kwargs):
            self._slots = eval(code_to_eval)
            func(self, *args, **kwargs)

        return wrapped_init
    return outer

def connect(source, signal, target, slot):
    source._signal_handlers[signal].append(target._slots[slot])

if __name__ == '__main__':
    @SignalSupporter('bitstring', 'groupelement', 'intvalue')
    class test_source(object):
        pass

    #@SignalSupporter('bitstring', 'int', 'fieldelement')
    class test_target(object):
        @slot_supporter('bitstring', 'intvalue', 'groupelement')
        def __init__(self):
            pass
            #self._slots = {'bitstring':self.bitstring_handler}

        def bitstring_handler(self, **kwargs):
            print 'Bitstring handler'
            for key,val in kwargs.iteritems():
                print key, '-->', val

        def intvalue_handler(self, **kwargs):
            print 'intvalue handler'
            for key,val in kwargs.iteritems():
                print key, '-->', val

        def groupelement_handler(self, **kwargs):
            print 'Groupelement handler'
            for key,val in kwargs.iteritems():
                print key, '-->', val

    t1 = test_target()
    t2 = test_target()

    s1 = test_source()
    s2 = test_source()

    connect(s1, 'bitstring', t1, 'bitstring')
    connect(s1, 'bitstring', t2, 'bitstring')
    connect(s1, 'intvalue', t2, 'intvalue')
    connect(s1, 'groupelement', t2, 'groupelement')

    s1.emit('bitstring', bitstring=1001)
    s1.emit('intvalue', intvalue=97)
    s1.emit('groupelement', groupelement=970)


