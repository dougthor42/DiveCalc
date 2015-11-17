# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:03:19 2015

@author: dthor
"""
# ---------------------------------------------------------------------------
### Imports
# ---------------------------------------------------------------------------
# Standard Library
import logging

# Third Party
import wx
import wx.lib.plot as wxplot
import numpy as np

# Package / Application
try:
    # Imports used by unit test runners
#    from . import pbsql
#    from . import plots
#    from . import utils
    from . import (__project_name__,
                   __version__,
                   )

    logging.debug("Imports for UnitTests")
except (SystemError, ImportError):
    try:
        # Imports used by Spyder
#        import pbsql
#        import plots
#        import utils
        from __init__ import (__project_name__,
                              __version__,
                              )

        logging.debug("Imports for Spyder IDE")
    except ImportError:
         # Imports used by cx_freeze
#        from pybank import pbsql
#        from pybank import plots
#        from pybank import utils
        from divecalc import (__project_name__,
                              __version__,
                              )

        logging.debug("imports for Executable")

# ---------------------------------------------------------------------------
### Module Constants
# ---------------------------------------------------------------------------
METER_TO_FT = 3.281
GROUPS = tuple(x for x in "ABCDEFGHIJK")
print(GROUPS)
TABLE_DEPTHS = (10, 15, 20, 25, 30, 35, 40, 50, 60,
                70, 80, 90, 100, 110, 120, 130)

DOPPLER_LIMITS = (-1, -1, -1, 245, 205, 160, 130, 70, 50,
                  40, 30, 25, 20, 15, 10, 5)

TBL1_GRPA = (60, 35, 25, 20, 15, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0)
TBL1_GRPB = (120, 70, 50, 35, 30, 15, 15, 10, 10, 5, 5, 5, 5, 0, 0, 0)
TBL1_GRPC = (210, 110, 75, 55, 45, 25, 25, 15, 15, 10, 10, 10, 7, 5, 5, 5)
TBL1_GRPD = (300, 160, 100, 75, 60, 40, 30, 25, 20, 15, 15, 12, 10, 10, 10, 0)
TBL1_GRPE = (-1, 225, 135, 100, 75, 50, 40, 30, 25, 20, 20, 15, 15, 13, 0, 0)
TBL1_GRPF = (-1, 350, 180, 125, 95, 60, 50, 40, 30, 30, 25, 20, 20, 15, 0, 0)
TBL1_GRPG = (-1, -1, 240, 160, 120, 80, 70, 50, 40, 35, 30, 25, 0, 0, 0, 0)
TBL1_GRPH = (-1, -1, 325, 195, 145, 100, 80, 60, 50, 40, 0, 0, 0, 0, 0, 0)
TBL1_GRPI = (-1, -1, -1, 245, 170, 120, 100, 70, 0, 0, 0, 0, 0, 0, 0, 0)
TBL1_GRPJ = (-1, -1, -1, -1, 205, 140, 110, 0, 0, 0, 0, 0, 0, 0, 0, 0)
TBL1_GRPK = (-1, -1, -1, -1, -1, 160, 130, 0, 0, 0, 0, 0, 0, 0, 0, 0)

TABLE1_GROUPS = (TBL1_GRPA, TBL1_GRPB, TBL1_GRPC, TBL1_GRPD, TBL1_GRPE,
                 TBL1_GRPF, TBL1_GRPG, TBL1_GRPH, TBL1_GRPI, TBL1_GRPJ,
                 TBL1_GRPK)

           #  A    B    C    D    E    F    G    H    I    J    K
TABLE_1 = (( 60, 120, 210, 300,  -1,  -1,  -1,  -1,  -1,  -1,  -1),
           ( 35,  70, 110, 160, 225, 350,  -1,  -1,  -1,  -1,  -1),
           ( 25,  50,  75, 100, 135, 180, 240, 325,  -1,  -1,  -1),
           ( 20,  35,  55,  75, 100, 125, 160, 195, 245,  -1,  -1),
           ( 15,  30,  45,  60,  75,  95, 120, 145, 170, 205,  -1),
           (  5,  15,  25,  40,  50,  60,  80, 100, 120, 140, 160),
           (  5,  15,  25,  30,  40,  50,  70,  80, 100, 110, 130),
           (  0,  10,  15,  25,  30,  40,  50,  60,  70,  -1,  -1),
           (  0,  10,  15,  20,  25,  30,  40,  50,  -1,  -1,  -1),
           (  0,   5,  10,  15,  20,  30,  35,  40,  -1,  -1,  -1),
           (  0,   5,  10,  15,  20,  25,  30,  -1,  -1,  -1,  -1),
           (  0,   5,  10,  12,  15,  20,  25,  -1,  -1,  -1,  -1),
           (  0,   5,   7,  10,  15,  20,  -1,  -1,  -1,  -1,  -1),
           (  0,   0,   5,  10,  13,  15,  -1,  -1,  -1,  -1,  -1),
           (  0,   0,   5,  10,  -1,  -1,  -1,  -1,  -1,  -1,  -1),
           (  0,   0,   5,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1),
           )

class DeathError(ValueError):
    pass


def table_depth(depth):
    """
    Rounds the depth up to the nearest table depth.

    The SSI Dive tables do not allow for arbitrary depths, so whatever depth
    is reached must be rounded up to the next table depth.

    Parameters:
    -----------
    depth : int or float
        The depth to round

    Returns:
    --------
    int
        The nearest table depth

    """
    if isinstance(depth, bool) or not isinstance(depth, (int, float)):
        raise TypeError("Depth must be an int or float")
    if depth < 0:
        raise ValueError("Depth must be positive")
    if depth > max(TABLE_DEPTHS):
        raise DeathError("{} ft is too deep!".format(depth))
    return [x for x in TABLE_DEPTHS if x >= depth][0]


def table_depth_index(depth):
    """
    Returns the index of the table depth.

    Parameters:
    -----------
    depth : int or float

    Returns:
    --------
    index : int

    """
    if depth not in TABLE_DEPTHS:
        depth = table_depth(depth)
    return TABLE_DEPTHS.index(depth)


def find_group_given_depth_time(depth, time):
    """
    Finds the group designation for a given depth and time.

    Parameters:
    -----------
    depth : int or float
        The maximum depth reached during the dive (even if it was only reached
        for 1 second).

    time : int or float
        The Bottom Time of the dive. Bottom Time is measured from the start
        of the descent to the start of the ascent. If on a repetitive dive,
        this number needs to include the resisdual nitrogen time (RT).

    Returns:
    --------
    group : string
        The group designation, a letter from A to K.

    """
    index = table_depth_index(depth)
    times = TABLE_1[index]
    table_time = [x for x in times if x >= time][0]
    table_time_index = times.index(table_time)
    group = GROUPS[table_time_index]
    return group


def find_new_group_after_si(group, surface_interval):
    pass


def find_rt_given_depth_group(depth, group):
    pass


def find_max_bt_given_depth_group(depth, group):
    pass







def ft_to_m(ft):
    return ft / METER_TO_FT

def m_to_ft(m):
    return m * METER_TO_FT


def main():
    print(table_depth(5))

if __name__ == "__main__":
    main()
