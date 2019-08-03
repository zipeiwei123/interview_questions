""" FAILED check concurrency difference python """
class Foo:
    def __init__(self):
        #create inheritance to ranking the execute
        self.ticket = 0
        


    def first(self, printFirst: 'Callable[[], None]') -> None:
        #CPU runs concurrency when is not the ticket, keep the CPU busy
        while self.ticket != 0:
            continue
        #printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.ticket = 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        #CPU runs concurrency when is not the ticket, keep the CPU busy
        while self.ticket != 1:
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.ticket = 2


    def third(self, printThird: 'Callable[[], None]') -> None:
        #CPU runs concurrency when is not the ticket, keep the CPU busy
        while self.ticket != 2:
            continue
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()