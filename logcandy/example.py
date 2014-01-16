import log, decorators
from decorators import FootprintAllMethods, footprint, footprintcls


@footprintcls()
class Test(object):

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


class Test2(object):

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
    
    t2 = Test2()
    t2.bar(hello='World!!!')

if __name__ == '__main__':
    main()

