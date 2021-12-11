import logging, os

LOG_FILE = 'log.txt'
LOG_FORMAT = "%(message)s"

class Log():
    def __init__(self, clean = False):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(LOG_FORMAT)

        if clean:
            if os.path.isfile(LOG_FILE):
                with open(LOG_FILE, 'w') as f:
                    pass

        fh = logging.FileHandler(LOG_FILE)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def log(self, *args):
        s = ''
        for i in args:
            s += (str(i) + ' ')

        logging.debug(s)

log = Log(True)

def test():
    log.log('aaa')
    log.log('bbb', 3)
    log.log('ccc %.2f CCC' % (3.1415926))
    log.log('ddd', 'ee %.2f fff' % (3.1415926))

if __name__ == '__main__':
    test()