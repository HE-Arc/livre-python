"""Utilisation de termcolor sous Windows."""

from colorama import init

from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()

# then use Termcolor for all colored text output
print(colored('Text from termcolor on Windows', 'red', 'on_yellow'))
