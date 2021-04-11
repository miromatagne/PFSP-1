"""
    Computes the initial solution of the the PFSP instance, either based
    on a random permutation or on a Simplified RZ Heuristic.
"""

import random


def get_random_permutation(nb_jobs):
    """
        Returns a random permutation of the jobs.

        :param nb_jobs: number of jobs in the considered instance
        :return: random permutation of the jobs
    """
    print("Started generating random initial solution...")
    random.seed(5)
    job_numbers = list(range(nb_jobs))
    random.shuffle(job_numbers)
    return job_numbers


def get_rz_heuristic(instance):
    """
        Returns an initial solution based on a simplified RZ Heuristic.

        :param instance: instance of PFSP problem on which the initial solution is computed.
        :return: initial solution
    """
    print("Started generating initial solution based on Simplified RZ Heuristic...")
    weighed_sum = list(instance.get_weighed_sum())
    first_job = weighed_sum.pop(0)
    sol = [first_job]
    for i in range(len(weighed_sum)):
        job = weighed_sum.pop(0)
        min_wct = float('inf')
        min_sol = None
        for j in range(len(sol)+1):
            temp_sol = sol.copy()
            temp_sol.insert(j, job)
            wct = instance.compute_wct(temp_sol)
            if wct < min_wct:
                min_wct = wct
                min_sol = temp_sol
        sol = min_sol
    return sol
