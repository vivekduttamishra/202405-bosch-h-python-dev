
import console

import dateutils as d

print(d.__name__)

def main():
    more=True
    while more:
        date=console.read_string('date in format yyyy-mm?')    
        year,month = [int(value) for value in date.split('-')]
        d.print_calendar(year,month)
        more = console.read_bool('want another calendar?')


    
    





    print(year, month)



main()