"""
    Main file
"""

import sys
import random
import argparse
from instance import Instance
from initial_solution import get_random_permutation, get_rz_heuristic
import time
import os

FIRST_IMPROVEMENT = "FIRST_IMPROVEMENT"
BEST_IMPROVEMENT = "BEST_IMPROVEMENT"

TRANSPOSE = "TRANSPOSE"
EXCHANGE = "EXCHANGE"
INSERT = "INSERT"

SRZ = "SRZ"
RANDOM_INIT = "RANDOM_INIT"

FIRST_ORDER = [TRANSPOSE, EXCHANGE, INSERT]
SECOND_ORDER = [TRANSPOSE, INSERT, EXCHANGE]


def parse_args():
    """
        Parses the arguments.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("instance", help="Instance file name")
    parser.add_argument("--measure", help="Measure mode", action="store_true")
    parser.add_argument(
        "--vnd", help="Variable Neighbourhood Descend", action="store_true")
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
    neighbourhood_order_group = parser.add_mutually_exclusive_group()
    neighbourhood_order_group.add_argument(
        "--first_order", help="transpose neighborhood", action="store_true")
    neighbourhood_order_group.add_argument(
        "--second_order", help="exchange neighborhood", action="store_true")

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
    if args.first_order:
        neighbourhood_order = FIRST_ORDER
    elif args.second_order:
        neighbourhood_order = SECOND_ORDER
    else:
        neighbourhood_order = None

    return args.vnd, args.instance, pivoting, neighbourhood, initial_solution, args.measure, neighbourhood_order


def measure_vnd_times():
    os.chdir("instances")
    files = os.listdir()
    files.sort()
    files = files[22:]
    initial_solutions = [RANDOM_INIT, SRZ]
    neighbourhood_orders = [FIRST_ORDER, SECOND_ORDER]
    for f in files:
        if "." not in f and f != "measures":
            output_file = open("./measures/VND/" + f + ".txt", "w")
            instance = Instance()
            instance.read_data_from_file(f)
            for initial_sol_arg in initial_solutions:
                for neighbourhood_order in neighbourhood_orders:
                    start_time = time.time()
                    if initial_sol_arg == RANDOM_INIT:
                        initial_solution = get_random_permutation(
                            instance.get_nb_jobs())
                    else:
                        initial_solution = get_rz_heuristic(instance)
                    print("Initial solution : ", initial_solution)
                    solution, wct = instance.solve_vnd(
                        initial_solution, neighbourhood_order)
                    output_file.write(initial_sol_arg + " " +
                                      "_".join(neighbourhood_order) + " " + str(wct) + " " + str(time.time() - start_time) + "\n")

                    print("Final job permutation : ", solution)
                    print("Weighted sum of Completion Times : ", wct)
                    print("Execution time : %s seconds" %
                          (time.time() - start_time))
            output_file.close()
    return None


def measure_ii_times():
    os.chdir("instances")
    files = os.listdir()
    files.sort()
    initial_solutions = [RANDOM_INIT, SRZ]
    pivoting_args = [FIRST_IMPROVEMENT, BEST_IMPROVEMENT]
    neighbourhood_args = [TRANSPOSE, EXCHANGE, INSERT]
    for f in files:
        if "." not in f and f != "measures":
            output_file = open("./measures/" + f + ".txt", "w")
            instance = Instance()
            instance.read_data_from_file(f)
            for initial_sol_arg in initial_solutions:
                for pivoting_arg in pivoting_args:
                    for neighbourhood_arg in neighbourhood_args:
                        start_time = time.time()
                        if initial_sol_arg == RANDOM_INIT:
                            initial_solution = get_random_permutation(
                                instance.get_nb_jobs())
                        else:
                            initial_solution = get_rz_heuristic(instance)
                        print("Initial solution : ", initial_solution)
                        solution, wct = instance.solve_ii(
                            initial_solution, pivoting_arg, neighbourhood_arg)
                        output_file.write(initial_sol_arg + " " + pivoting_arg + " " +
                                          neighbourhood_arg + " " + str(wct) + " " + str(time.time() - start_time) + "\n")

                        print("Final job permutation : ", solution)
                        print("Weighted sum of Completion Times : ", wct)
                        print("Execution time : %s seconds" %
                              (time.time() - start_time))
            output_file.close()
    return None


# def get_best_solutions():
#     best_solutions_file = open("bestSolutions.txt")
#     best_solutions_file.readline()
#     best_solutions_dict = {}
#     for line in best_solutions_file.readlines():
#         instance, solution = line.split(
#             ",")[0].strip(), line.split(",")[1].strip()
#         best_solutions_dict[instance] = int(float(solution))


def get_experimental_results():
    os.chdir("instances/measures")
    initial_solutions = [RANDOM_INIT, SRZ]
    pivoting_args = [FIRST_IMPROVEMENT, BEST_IMPROVEMENT]
    neighbourhood_args = [TRANSPOSE, EXCHANGE, INSERT]
    files = []
    for init in initial_solutions:
        for piv in pivoting_args:
            for n in neighbourhood_args:
                filename = init + "_" + piv + "_" + n + ".csv"
                f = open(filename, "w")
                f.write("instance,solution,execution_time" + "\n")
                files.append(f)
    result_files = os.listdir()
    result_files.sort()
    print(result_files)
    for file_name in result_files:
        if ".D" not in file_name and file_name != "measures":
            f = open(file_name)
            lines = f.readlines()
            for i in range(len(lines)):
                line = lines[i].split()
                solution, time = line[3], line[4]
                files[i].write(file_name.split(".")[0] + "," +
                               solution + "," + time + "\n")
            f.close()
    for f in files:
        f.close()


if __name__ == '__main__':
    vnd, filename, pivoting_arg, neighbourhood_arg, initial_solution_arg, measure, neighbourhood_order = parse_args()
    if measure:
        if vnd:
            measure_vnd_times()
        else:
            measure_ii_times()
    else:
        instance = Instance()
        instance.read_data_from_file(filename)
        if initial_solution_arg == RANDOM_INIT:
            initial_solution = get_random_permutation(instance.get_nb_jobs())
        else:
            initial_solution = get_rz_heuristic(instance)
        print("Initial solution : ", initial_solution)
        start_time = time.time()

        if vnd:
            solution, wct = instance.solve_vnd(
                initial_solution, neighbourhood_order)
        else:
            solution, wct = instance.solve_ii(
                initial_solution, pivoting_arg, neighbourhood_arg)
        print("Final job permutation : ", solution)
        print("Weighted sum of Completion Times : ", wct)
        print("Execution time : %s seconds" % (time.time() - start_time))
