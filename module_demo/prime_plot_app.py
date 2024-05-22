from console import read_int, read_bool
import primes 
from histogram import * 
import frequency as f



def main():
    more=True
    while more:
        min= read_int("min?")
        max= read_int("max?")
        
        results = primes.prime_range_list(min, max)
        results = [ result%10 for result in results]
        
        prime_frequency = f.frequency(results)

        plot_histogram(prime_frequency)




        more = read_bool("more?")

main()
