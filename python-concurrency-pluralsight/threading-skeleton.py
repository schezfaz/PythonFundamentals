import threading

def print_in_terminal(val):
    print("inside the thread")
    print("echo: {}".format(val))
    return

val="Threading!!!"

#Construct the thread using the threading.Thread() constructor
#Parameters: target - target function to be executes + other args that the target function requires
t = threading.Thread(target=print_in_terminal(val))

#schedule the new thread to start
t.start()

#suspend execution until the new thread completes
t.join()
