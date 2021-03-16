"""
    Main file
"""

import sys
import random
import argparse
from instance import Instance
from initial_solution import get_random_permutation, get_rz_heuristic


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("instance", help="Instance file name")
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

    pivoting = 0
    neighbourhood = 0
    initial_solution = 0
    if args.best:
        pivoting = 1
    if args.exchange:
        neighbourhood = 1
    elif args.insert:
        neighbourhood = 2
    if args.srz:
        initial_solution = 1

    return args.instance, pivoting, neighbourhood, initial_solution


if __name__ == '__main__':
    filename, pivoting_arg, nighbourhood_arg, initial_solution_arg = parse_args()
    # Initialize random seed
    random.seed(7)

    instance = Instance()
    instance.read_data_from_file(filename)
    if initial_solution_arg == 0:
        initial_solution = get_random_permutation(instance.get_nb_jobs())
    else:
        initial_solution = get_rz_heuristic(instance)

    print(initial_solution)
    # print(instance.compute_wct(get_random_permutation(instance.get_nb_jobs())))
