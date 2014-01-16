from logcandy import log, decorators
from logcandy.decorators import FootprintAllMethods, footprint


class Test(object):

    __metaclass__ = FootprintAllMethods

    def __init__(self):
        self.foo = 'Foo'

    def __str__(self):
        return 'Test'

    __repr__ = __str__

    def bar(self, hello='World'):
        self.aj()

    def aj(self):
        self.waj()

    def waj(self):
        log.debug('waj!')


def main():
    t = Test()
    t.bar(hello='World!!!')

print vars()

decorators.register_footprint(vars())

if __name__ == '__main__':
    main()

