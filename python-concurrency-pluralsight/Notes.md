# Python Concurrency
Process: Execution context of a running program or a running instance of a computer program

Every executing process has system resources and a section of memory assigned to it.

## Threading
Thread: smallest sequence of instructions that can be managed by the OS

When multiple cores are available, multiple threads can run at the same time in parallel on multiple cores. If only a single core is available, threads share time on that core.

Pool of threads to respond to multiple request simultaneously (on an app. server for example). Each request is handled by a thread from the pool. The thread executes the task assigned and then returns to the pool for the next request. 

Python threading library allows us to create threads that map directly to the operating system threads.

class threading.Thread(group = None, 
                       target = None, 
                       name = None,
                       args = (),
                       kwargs={},
                       daemon = None)

__group parameter__: future use, always set to None
__target__ : function to be invoked
__name__ : name for thread, if blank default name = Thread + counter, Thread1, Thread2, etc.
__args__ : arguement tuple for the target function
__kwargs__: dictionary of keyword arguements
__daemon__: whether thread will be terminated if its parent thread terminates or not

in threading-skeleton.py we consider thread to be a worker executing the instructions in the target function

in threading-work.py we consider threads to be units of work




