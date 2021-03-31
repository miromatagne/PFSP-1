"""
    Computes the neighbors used in the PFSP problem solving algorithm, following
    several pivoting rules (FIRST_IMPROVEMENT or BEST_IMPROVEMENT) and several
    neighborhood relations (TRANSPOSE, EXCHANGE or INSERT).
"""

FIRST_IMPROVEMENT = "FIRST_IMPROVEMENT"
BEST_IMPROVEMENT = "BEST_IMPROVEMENT"

TRANSPOSE = "TRANSPOSE"
EXCHANGE = "EXCHANGE"
INSERT = "INSERT"


def get_first_improvement_neighbour(instance, solution, initial_wct, neighbourhood_method):
    # print(solution)
    # print(initial_wct)
    if neighbourhood_method == TRANSPOSE:
        for i in range(len(solution)):
            if i == len(solution) - 1:
                solution[0], solution[len(
                    solution)-1] = solution[len(solution)-1], solution[0]
            else:
                solution[i], solution[i+1] = solution[i+1], solution[i]
            wct = instance.compute_wct(solution)
            if wct < initial_wct:
                return solution, wct
            if i != len(solution) - 1:
                solution[i], solution[i+1] = solution[i+1], solution[i]
        return None, initial_wct
    if neighbourhood_method == EXCHANGE:
        for i in range(len(solution)-1):
            for j in range(i+1, len(solution)):
                solution[i], solution[j] = solution[j], solution[i]
                wct = instance.compute_wct(solution)
                # print(i)
                if wct < initial_wct:
                    return solution, wct
                solution[i], solution[j] = solution[j], solution[i]
        return None, initial_wct
    if neighbourhood_method == INSERT:
        for i in range(len(solution)):
            temp_sol = solution.copy()
            temp_rem = temp_sol.pop(i)
            temp_sol.insert(0, temp_rem)
            for j in range(len(solution)):
                # print(temp_sol)
                wct = instance.compute_wct(temp_sol)
                if wct < initial_wct:
                    return temp_sol, wct
                if j != len(solution) - 1:
                    temp_sol[j], temp_sol[j+1] = temp_sol[j+1], temp_sol[j]
        return None, initial_wct


def get_best_improvement_neighbour(instance, solution, initial_wct, neighbourhood_method):
    min_wct = initial_wct
    min_sol = None
    if neighbourhood_method == TRANSPOSE:
        for i in range(len(solution)):
            if i == len(solution) - 1:
                solution[0], solution[len(
                    solution)-1] = solution[len(solution)-1], solution[0]
            else:
                solution[i], solution[i+1] = solution[i+1], solution[i]
            wct = instance.compute_wct(solution)
            # print(i)
            # print(temp_sol)
            if wct < min_wct:
                min_wct = wct
                min_sol = solution.copy()
            if i != len(solution) - 1:
                solution[i], solution[i+1] = solution[i+1], solution[i]
        if min_wct != initial_wct and min_sol:
            return min_sol, min_wct
        return None, initial_wct
    if neighbourhood_method == EXCHANGE:
        for i in range(len(solution)-1):
            for j in range(i+1, len(solution)):
                solution[i], solution[j] = solution[j], solution[i]
                wct = instance.compute_wct(solution)
                # print(i)
                if wct < min_wct:
                    min_wct = wct
                    min_sol = solution.copy()
                solution[i], solution[j] = solution[j], solution[i]
        if min_wct != initial_wct and min_sol:
            return min_sol, min_wct
        return None, initial_wct
    if neighbourhood_method == INSERT:
        for i in range(len(solution)):
            temp_sol = solution.copy()
            temp_rem = temp_sol.pop(i)
            temp_sol.insert(0, temp_rem)
            for j in range(len(solution)-1):
                wct = instance.compute_wct(temp_sol)
                if wct < min_wct:
                    min_wct = wct
                    min_sol = temp_sol.copy()
                if j != len(solution) - 1:
                    temp_sol[j], temp_sol[j+1] = temp_sol[j+1], temp_sol[j]
        if min_wct != initial_wct and min_sol:
            return min_sol, min_wct
        return None, initial_wct
    # if neighbourhood_method == INSERT:
    #     for i in range(len(solution)):
    #         temp_sol = solution.copy()
    #         value = temp_sol.pop(i)
    #         #temp_sol.insert(0, temp_rem)
    #         for j in range(len(solution)):
    #             if i != j and j != i-1:
    #                 temp_sol.insert(j, value)
    #                 wct = instance.compute_wct(temp_sol)
    #                 if wct < min_wct:
    #                     min_wct = wct
    #                     min_sol = temp_sol.copy()
    #                 temp_sol.remove(value)
    #     if min_wct != initial_wct and min_sol:
    #         return min_sol, min_wct
    #     return None, initial_wct
