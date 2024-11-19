from grim.client import EventLoop

eventloop = EventLoop()


def main():
    print("hello grim!")
    eventloop.run()
