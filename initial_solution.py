import random


def get_random_permutation(nb_jobs):
    random.seed(5)
    job_numbers = list(range(nb_jobs))
    random.shuffle(job_numbers)
    return job_numbers


def get_rz_heuristic(instance):
    weighed_sum = list(instance.get_weighed_sum())
    first_job = weighed_sum.pop(0)
    sol = [first_job]
    for i in range(len(weighed_sum)):
        job = weighed_sum.pop()
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
