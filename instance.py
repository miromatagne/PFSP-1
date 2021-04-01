"""
    PFSP instance file
"""

from neighbour import get_best_improvement_neighbour, get_first_improvement_neighbour

FIRST_IMPROVEMENT = "FIRST_IMPROVEMENT"
BEST_IMPROVEMENT = "BEST_IMPROVEMENT"


class Instance:
    """
        Class describing an instance of the PFSP problem.
    """

    def __init__(self):
        self.nb_jobs = 0
        self.nb_machines = 0
        self.processing_times_matrix = []
        self.due_dates = []
        self.priority = []

    def read_data_from_file(self, filename):
        """
            Reads data from a PFSP instance file and stores the content.

            :param filename: name of the instance file
        """
        try:
            with open(filename, "r") as f:
                print("File " + filename + " is now open, start to read...")
                self.nb_jobs, self.nb_machines = tuple(
                    map(int, f.readline().split(" ")))
                print("Number of jobs : " + str(self.nb_jobs))
                print("Number of machines  : " + str(self.nb_machines))
                print("Start to read matrix...")
                for i in range(self.nb_jobs):
                    line = f.readline().strip().split(" ")
                    line = list(map(int, line))
                    self.processing_times_matrix.append(line[1::2])
                # print(self.processing_times_matrix)
                f.readline()
                for i in range(self.nb_jobs):
                    line = f.readline().split(" ")
                    self.due_dates.append(int(line[1]))
                    self.priority.append(int(line[-1]))
                # print(self.due_dates)
                # print(self.priority)
            return True
        except OSError as e:
            print("Error while opening" + filename)
            return False

    def compute_wct(self, sol):
        """
            Computes the Weighed sum of Completion Times (WCT) for a given solution (ordering of jobs).

            :param sol: job ordering on which the WCT is computed
        """
        previous_machine_end_time = [0 for i in range(len(sol))]

        # First machine
        for j in range(len(sol)):
            job_number = sol[j]
            previous_machine_end_time[j] = previous_machine_end_time[j -
                                                                     1] + self.processing_times_matrix[job_number][0]
        # Following machines
        for m in range(1, self.nb_machines):
            previous_machine_end_time[0] += self.processing_times_matrix[sol[0]][m]
            previous_job_end_time = previous_machine_end_time[0]
            for j in range(1, len(sol)):
                job_number = sol[j]
                previous_machine_end_time[j] = max(
                    previous_job_end_time, previous_machine_end_time[j]) + self.processing_times_matrix[job_number][m]
                previous_job_end_time = previous_machine_end_time[j]
        wct = 0
        for j in range(len(sol)):
            wct += previous_machine_end_time[j] * self.priority[sol[j]]
        return wct

    def get_nb_jobs(self):
        return self.nb_jobs

    def get_weighed_sum(self):
        """
            Computes the weighed sum used for the SRZ Heuristic initial solution.
        """
        weights = {}
        for i in range(self.nb_jobs):
            total_processing_time = sum(self.processing_times_matrix[i])
            weights[i] = total_processing_time / self.priority[i]
        sorted_weighed_sum = dict(
            sorted(weights.items(), key=lambda item: item[1]))
        # print(sorted_weighed_sum)
        return sorted_weighed_sum.keys()

    def solve_ii(self, solution, pivoting_rule, neighbourhood_method):
        """
            Solves the PSFP problem using Iterative Improvement and returns the solution.

            :param solution: initial solution used to start the algorithm
            :pivoting_rule: pivoting rule used during the algorithm (LEAST_IMPROVEMENT or BEST_IMPORVEMENT)
            :neighborhood_rule: neighborhood rule used during the algorithm (EXCHANGE, TRASPOSE or INSERT)
        """
        initial_wct = self.compute_wct(solution)
        if pivoting_rule == FIRST_IMPROVEMENT:
            sol, wct = solution, initial_wct
            while True:
                temp_sol, temp_wct = get_first_improvement_neighbour(
                    self, sol, wct, neighbourhood_method)
                # print(temp_wct)
                if not temp_sol:
                    if wct == 0:
                        wct = temp_wct
                    return sol, wct
                sol, wct = temp_sol, temp_wct
        else:
            sol, wct = solution, initial_wct
            while True:
                temp_sol, temp_wct = get_best_improvement_neighbour(
                    self, sol, wct, neighbourhood_method)
                if not temp_sol:
                    if wct == 0:
                        wct = temp_wct
                    return sol, wct
                sol, wct = temp_sol, temp_wct

    def solve_vnd(self, solution, neighbourhood_order):
        k = 3
        i = 0
        sol = solution.copy()
        wct = self.compute_wct(solution)
        while k > i:
            # print(i)
            temp_sol, temp_wct = get_first_improvement_neighbour(
                self, sol.copy(), wct, neighbourhood_order[i])
            if not temp_sol:
                i = i + 1
            else:
                sol = temp_sol.copy()
                wct = temp_wct
                # print(wct)
                # print(i)
                i = 0
        return sol, wct
