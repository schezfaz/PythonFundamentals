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

Simplest way to create a thread is to instantiate an object of the thread class

threading.Thread: constructor

.join() method: suspend all program execution until the thread that  has  started completes execution

 ## Thread LifeCycle
-  When a program starts, there is only one thread (main thread) that is running
- Main thread is responsible for imports, creating functions,etc.
- Creates a new thread 1 :  New thread is in the new state
- When the main thread calls start on the new thread, it goes into the ready state, available to be scheduled on the CPU
- Join: Main Thread goes from running state to the blocked state i.e. it is suspended and cannot proceed any execution further
- Thread 1 goes into the running state and ends
- Signals the completion to the main thread, and main thread resumes execution

New  --> Ready ----> Running --> Terminated

Blocked state: When thread waits for particular event/condition to take place


Each  thread has its own counter: maintaining instructions being  executed in the current time,its own registers  and its own stack

Memory is set aside in a stack place for a thread

Any data or memory owned by a process can be accessed by any of the threads which are a part of the process

Once a thread is started we have little control over how it runs

The OS runs an algorithm, the scheduler which determines what threads run for how long and when, which processor core they run on and when they  will get suspended

Context Switch: Process of saving and restoring the state of a thread or process
If a thread from another process is switching into, a full process switch occurs which is an expensive process

Thread switching is less expensive than process switching, thus, parallel programming using threads is preferred over parallel processing.

Memory sharing with indetermined scheduling can lead to thread interference/race condition: read/write on same variable (may lead to data corruption)
- Solution: Thread Synchronisation     

## Thread Synchronisation
- Keep shared memory access between threads minimum
- The more shared memory between threads, the more complex your code gets, the less concurrent it runs because of the need to combat thread interference

__threading.LOCK:__ The lock is in one of 2 states: locked / unlocked 
- When put in the locked state by one thread, it can only be unlocked by that same thread, cannot be locked or unlocked by any other thread

i.e. Acqurie: signifies a thread putting a lock into a locked state, once the lock is acquired by a thread, it cannot be  acquired by until thread until the lock is released by the first thread (i.e the owner)

When a  thread tries to acquire a lock held by another thread, that thread goes into the blocked state i.e. it's execution is paused and it cannot continue until it acquires the lock i.e. after it is released by the first thread

`lock = threading.Lock()`
 : creates a lock for the shared resource

`lock.acquire()`
`..acess shared resource`
`lock.release()` 

Need to use a try/finally block while accessing shared resource to ensure that if an execption occurs, the lock will get released at some point so as to prevent indefinite blocking of other threads

 with lock: lock is automatically acquired while entering this block and automatically released while leaving the block, even if an exception occurs during shared resource access

 * Use locks only when shared variables are modified
 * locks are not needed for automic operations i.e. single steps like retrieving items, adding items, etc.

 lock.locked() method tells us if the lock has already been acquired or not

### Type of lock: RLock or Re-entering lock
allows a thread to acquire a lock it already holds. In the regular lock, if a thread that has already acquired the lock tries to acquire the same lock, it will get blocked. RLock fixes this.

## Semaphore: Thread Synchronisation Mechanism
Sync. primitive that manages an internal counter, instead of a single locked or unlocked switch.

Everytime the thread calls acquire, internal counter is -- (decremented), release()  ++ (incremented)

```
semaphore = threading.Semaphore()
semaphore.acquire() --> decrements the counter
semaphore.release() --> increments the counter
```

Internal counter can never go below zero.





 

