import xloil as xlo
import xloil as xlo
import sys
import datetime as dt
import asyncio
import os 

 
#
# Functions are registered by decorating them with xloil.func.  The function
# doc-string will be displayed in Excel's function wizard
#
@xlo.func
def pySum(x, y, z):
    '''Adds up numbers'''
    return x + y + z



# if xlOil is embedded: no need to specify Application.
# Returns a numpy array
xlo.Range("A1:C1").value

# Using COM (win32com) to access a range with empty index
# Returns a tuple rather than a numpy array
xlo.app().Range("A1", "C1").Value

# Set the entire range to a single value
wb = xlo.active_workbook()  # Only available when embedded


@xlo.func
def pyTestRange(r: xlo.Range):
    return 5
    print(xlo.app().range("A1:C1").font)

