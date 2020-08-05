# Compatible with ranger 1.6.0 through 1.7.*
#
# This plugin adds the sorting algorithm called 'pathdate'.  To enable it, type
# ":set sort=pathdate" or create a key binding with ":map od set sort=pathdate"

from __future__ import (absolute_import, division, print_function)

from random import random

from ranger.container.directory import Directory

from shanepy import *

# The function must return a number. The numbers are then compared
# Directory.sort_dict['pathdate'] = lambda path: tv(path)
Directory.sort_dict['pathdate'] = lambda path: random()

def extract_date(path):
    return b("rosie-extract-date", path)[0][:-1]

def sort_by_pathdate(path):
    # I can't do it this way because I need the entire list of paths.
    # Instead, I must use a hash function
    # b("sort -t . -n -k 3,3 -k 2,2 -k 1,1", b("ls /home/shane/notes/ws/tabs")[0])[0]