"""
    Main file
"""

import sys
import random
import argparse
from instance import Instance
from initial_solution import get_random_permutation, get_rz_heuristic
import time

FIRST_IMPROVEMENT = "FIRST_IMPROVEMENT"
BEST_IMPROVEMENT = "BEST_IMPROVEMENT"

TRANSPOSE = "TRANSPOSE"
EXCHANGE = "EXCHANGE"
INSERT = "INSERT"

SRZ = "SRZ"
RANDOM_INIT = "RANDOM_INIT"


def parse_args():
    """
        Parses the arguments.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("instance", help="Instance file name")
    parser.add_argument("--measure", help="Measure mode", action="store_true")
    pivoting_group = parser.add_mutually_exclusive_group()
    pivoting_group.add_argument(
        "--first", help="first-improvement pivoting rule", action="store_true")
    pivoting_group.add_argument(
        "--best", help="best-improvement pivoting rule", action="store_true")
    neighbourhood_group = parser.add_mutually_exclusive_group()
    neighbourhood_group.add_argument(
        "--transpose", help="transpose neighborhood", action="store_true")
    neighbourhood_group.add_argument(
        "--exchange", help="exchange neighborhood", action="store_true")
    neighbourhood_group.add_argument(
        "--insert", help="instert neighborhood", action="store_true")
    initial_solution_group = parser.add_mutually_exclusive_group()
    initial_solution_group.add_argument(
        "--random-init", help="randomly generated initial solution", action="store_true")
    initial_solution_group.add_argument(
        "--srz", help="simplified RZ heuristic initial solution", action="store_true")

    args = parser.parse_args()

    pivoting = FIRST_IMPROVEMENT
    neighbourhood = TRANSPOSE
    initial_solution = RANDOM_INIT
    if args.best:
        pivoting = BEST_IMPROVEMENT
    if args.exchange:
        neighbourhood = EXCHANGE
    elif args.insert:
        neighbourhood = INSERT
    if args.srz:
        initial_solution = SRZ

    return args.instance, pivoting, neighbourhood, initial_solution, args.measure


if __name__ == '__main__':
    filename, pivoting_arg, neighbourhood_arg, initial_solution_arg, measure = parse_args()
    # Initialize random seed
    # random.seed(7)

    instance = Instance()
    instance.read_data_from_file(filename)
    if initial_solution_arg == RANDOM_INIT:
        initial_solution = get_random_permutation(instance.get_nb_jobs())
    else:
        initial_solution = get_rz_heuristic(instance)
    print("Initial solution : ", initial_solution)
    start_time = time.time()
    solution, wct = instance.solve(
        initial_solution, pivoting_arg, neighbourhood_arg)
    print("Final job permutation : ", solution)
    print("Weighted sum of Completion Times : ", wct)
    print("Execution time : %s seconds" % (time.time() - start_time))
