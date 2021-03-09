"""
    Main file
"""

import sys
import random
import argparse


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
    elif args.inster:
        neighbourhood = 2
    if args.srz:
        initial_solution = 1

    return pivoting, neighbourhood, initial_solution


if __name__ == '__main__':
    piuvoting, nighbourhood, initial_solution = parse_args()
    # Initialize random seed
    random.seed(4)
