import threading
from threading import Thread

#Create a class that inherits from the Thread class in the threading package and override the run method
class FibonacciThread(threading.Thread):
    def __init__(self, num):  #dunder init method overwritten to provide additional state in the object via constructor
        Thread.__init__(self)
        self.num = num


    #Overridden run method: to calculate fibonacci of number passed to constructor
    def run(self):
        fib = [0]*(self.num+1)
        fib[0] = 0
        fib[1]=1
        for i in range(2,self.num+1):
            fib[i]=fib[i-1] + fib[i-2]
        print (fib[self.num])

#creating objects of our class
fib1 = FibonacciThread(10)
fib2 = FibonacciThread(14)

fib1.start()
fib2.start()

fib1.join()
fib2.join()


#Note: Whenever you override a dunder init method in subclass of thread, super class' dunder init method must always be called first before performing any other operations
