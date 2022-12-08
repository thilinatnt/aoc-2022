import timeit
from statistics import median


def run_time(code: any):
    n = 100
    durations = timeit.Timer(code).repeat(repeat=n, number=1)
    print("\t--- %s ms ---\n" % round(median(durations) * 1000, 3))
