#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 2
day = 18

def test_code():
    assert main.calendar("march") == 3, 'calendar("march") == 3 failed'
    assert main.calendar("august") == 8, 'calendar("august") == 8 failed'
    assert main.calendar("potato") == "potato is not a month", 'calendar("potato") == "potato is not a month" failed'

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
