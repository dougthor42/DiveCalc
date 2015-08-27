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
    # Imports used for unittests
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
TABLE_DEPTHS = (10, 15, 20, 25, 30, 35, 40, 50, 60,
                70, 80, 90, 100, 110, 120, 130)


class DeathError(ValueError):
    pass


def table_depth(depth):
    if isinstance(depth, bool) or not isinstance(depth, (int, float)):
        raise TypeError("Depth must be an int or float")
    if depth < 0:
        raise ValueError("Depth must be positive")
    if depth > max(TABLE_DEPTHS):
        raise DeathError("{} ft is too deep!".format(depth))
    return [x for x in TABLE_DEPTHS if x >= depth][0]


def find_group_given_depth_time(depth, time):
    pass


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
    print(table_depth("h"))

if __name__ == "__main__":
    main()
