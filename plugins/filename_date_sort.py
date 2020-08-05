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
