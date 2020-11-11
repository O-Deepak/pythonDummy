import threading


class threads(threading.Thread):

    def run(self):
        print("{} : Inside run".format(threading.currentThread().getName()))


def func(i):
    print("{} : I am #{}".format(threading.currentThread().getName(), i))


threadList = []
if __name__ == "__main__":
    for i in range(5):
        t = threads()
        t.start()