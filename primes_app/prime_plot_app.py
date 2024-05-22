from utils.console import read_int, read_bool
import algorithms.primes as primes
import help
from stats.graphs.histogram import * 
import stats.formula.frequency as f



def main():
    more=True
    help.about()
    while more:
        min= read_int("min?")
        max= read_int("max?")
        
        results = primes.prime_range_list(min, max)
        results = [ result%10 for result in results]
        
        prime_frequency = f.frequency(results)

        plot_histogram(prime_frequency)




        more = read_bool("more?")

main()
