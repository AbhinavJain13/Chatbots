#!/usr/bin/env python

# Command Line Interface (CLI) version

import time
import signal
import rogerbot as bot


# Chat Server Framework functions

def sleep(n):
    """Sleep n number of seconds.
    Pauses the execution of the program.
    """
    time.sleep(n)


def output(s):
    """Outputs string s as chat message.
    Send the given string to the chat client.
    """
    print s


def timeout_handler(signum, frame):
    # print "\b\b  "
    raise Exception("chatServer timeout")


# Register the signal function handler
signal.signal(signal.SIGALRM, timeout_handler)


# Run forever on the command line

def forever():
    while True:
        humanSpeak = raw_input("> ")
        bot.response(humanSpeak)


def main():
    """docstring for main"""
    # Setup
    bot.setup()
    signal.alarm(10)
    #
    # Run continuesly
    while True:
        try:
            forever()
        except Exception, exc:
            print "\b\bimpatient"
            # output("impatient")


if __name__ == '__main__':
    main()
