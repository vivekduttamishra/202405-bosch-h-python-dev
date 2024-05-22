from help import about
import sys

import utils.console as console

import utils.dates as d

print(d.__name__)

def main():
    
    if len(sys.argv)>=3:
        year=int(sys.argv[1])
        month=int(sys.argv[2])
        d.print_calendar(year,month)
        sys.exit(0)
    else:
        about()
        more=True
        while more:
            date=console.read_string('date in format yyyy-mm?')    
            year,month = [int(value) for value in date.split('-')]
            d.print_calendar(year,month)
            more = console.read_bool('want another calendar?')


    
    





    print(year, month)



main()