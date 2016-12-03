#!/usr/bin/env python

# timeoutingChatServer.py

# Command Line Interface (CLI) version

import time
import signal
# from contextlib import contextmanager

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


def outputWithDelay(s, n):
    """Outputs string s as chat message after a
    delay of n seconds. This future output will be
    discarded when another input from the user is
    received, or when another call to `outputWithDelay`
    is made, or if a call to `delayedCallback` is made.
    """
    def signal_handle(signum, frame):
        output("\b\b  \b\b" + s)
        raise Exception("chatServerDelayTimeout")
    signal.signal(signal.SIGALRM, signal_handle)
    signal.alarm(n)


def delayedCallback(n, callback):
    """Executes the callback after a delay of n
    seconds. The execution of the callback is cancelled
    if another `delayedCallback` is made, or if a
    call to `outputWithDelay` is made.
    """
    def signal_handle(signum, frame):
        print "\b\b  \b\b",
        callback()
        raise Exception("chatServerDelayTimeout")
    signal.signal(signal.SIGALRM, signal_handle)
    signal.alarm(n)


# Run forever on the command line

def forever():
    while True:
        humanSpeak = raw_input("> ")
        # Clear a possible delayed message
        signal.alarm(0)
        bot.response(humanSpeak)


def main():
    """docstring for main"""
    # Setup
    bot.setup()
    #
    # Run continuesly
    while True:
        try:
            forever()
        except Exception, exc:
            pass


if __name__ == '__main__':
    main()
