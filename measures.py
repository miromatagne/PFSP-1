import time
from initial_solution import get_random_permutation, get_rz_heuristic
from instance import Instance
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


def measure_vnd_times():
    """
        Measures the execution times as well as the solutions to the PFSP instance
        by applying Variable Neighbourhood Descend to all instances (with all combinations 
        of initial solutions and neighbourhood orders).
    """
    os.chdir("instances")
    files = os.listdir()
    files.sort()
    files = [files[31]]
    print(files)
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
    """
        Measures the execution times as well as the solutions to the PFSP instance
        by applying Iterative Improvement to all instances (with all combinations 
        of initial solutions, pivoting rules and neighbourhood methods).
    """
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


def get_experimental_results_vnd():
    """
        Measure execution times and solutions for all instances, and group the results
        by the combinations used for resolution.
    """
    os.chdir("instances/measures/VND")
    initial_solutions = [RANDOM_INIT, SRZ]
    neighbourhood_orders = [FIRST_ORDER, SECOND_ORDER]
    files = []
    for init in initial_solutions:
        for n in neighbourhood_orders:
            filename = init + "_" + "_".join(n) + ".csv"
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
                solution, time = line[2], line[3]
                files[i].write(file_name.split(".")[0] + "," +
                               solution + "," + time + "\n")
            f.close()
    for f in files:
        f.close()


def get_experimental_results_ii():
    """
        Measure execution times and solutions for all instances, and group the results
        by the combinations used for resolution.
    """
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
