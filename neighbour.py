FIRST_IMPROVEMENT = "FIRST_IMPROVEMENT"
BEST_IMPROVEMENT = "BEST_IMPROVEMENT"

TRANSPOSE = "TRANSPOSE"
EXCHANGE = "EXCHANGE"
INSERT = "INSERT"


def get_neighbour(instance, solution, pivoting_rule, neighbourhood_method):
    print(solution)
    if pivoting_rule == FIRST_IMPROVEMENT:
        sol, wct = solution, 0
        while True:
            temp_sol, temp_wct = get_first_improvement_neighbour(
                instance, sol, neighbourhood_method)
            # print(temp_wct)
            if not temp_sol:
                if wct == 0:
                    wct = temp_wct
                return sol, wct
            sol, wct = temp_sol, temp_wct
    else:
        sol, wct = solution, 0
        while True:
            temp_sol, temp_wct = get_best_improvement_neighbour(
                instance, sol, neighbourhood_method)
            # print(temp_wct)
            if not temp_sol:
                if wct == 0:
                    wct = temp_wct
                return sol, wct
            sol, wct = temp_sol, temp_wct


def get_first_improvement_neighbour(instance, solution, neighbourhood_method):
    # print(solution)
    initial_wct = instance.compute_wct(solution)
    # print(initial_wct)
    if neighbourhood_method == TRANSPOSE:
        for i in range(len(solution)):
            temp_sol = solution.copy()
            if i == len(solution) - 1:
                temp_sol[0], temp_sol[len(
                    temp_sol)-1] = temp_sol[len(temp_sol)-1], temp_sol[0]
            else:
                temp_sol[i], temp_sol[i+1] = temp_sol[i+1], temp_sol[i]
            wct = instance.compute_wct(temp_sol)
            # print(i)
            # print(temp_sol)
            if wct < initial_wct:
                return temp_sol, wct
        return None, initial_wct
    if neighbourhood_method == EXCHANGE:
        for i in range(len(solution)-1):
            for j in range(i+1, len(solution)-1):
                temp_sol = solution.copy()
                temp_sol[i], temp_sol[j] = temp_sol[j], temp_sol[i]
                wct = instance.compute_wct(temp_sol)
                # print(i)
                if wct < initial_wct:
                    return temp_sol, wct
        return None, initial_wct
    if neighbourhood_method == INSERT:
        for i in range(len(solution)):
            for j in range(len(solution)):
                temp_sol = solution.copy()
                temp_rem = temp_sol.pop(i)
                temp_sol.insert(j, temp_rem)
                wct = instance.compute_wct(temp_sol)
                # print(temp_sol)
                if wct < initial_wct:
                    print(temp_sol, wct)
                    return temp_sol, wct
        return None, initial_wct


def get_best_improvement_neighbour(instance, solution, neighbourhood_method):
    initial_wct = instance.compute_wct(solution)
    min_wct = initial_wct
    min_sol = None
    if neighbourhood_method == TRANSPOSE:
        for i in range(len(solution)):
            temp_sol = solution.copy()
            if i == len(solution) - 1:
                temp_sol[0], temp_sol[len(
                    temp_sol)-1] = temp_sol[len(temp_sol)-1], temp_sol[0]
            else:
                temp_sol[i], temp_sol[i+1] = temp_sol[i+1], temp_sol[i]
            wct = instance.compute_wct(temp_sol)
            # print(i)
            # print(temp_sol)
            if wct < min_wct:
                min_wct = wct
                min_sol = temp_sol
        if min_wct != initial_wct and min_sol:
            return min_sol, min_wct
        return None, initial_wct
    if neighbourhood_method == EXCHANGE:
        for i in range(len(solution)-1):
            for j in range(i+1, len(solution)-1):
                temp_sol = solution.copy()
                temp_sol[i], temp_sol[j] = temp_sol[j], temp_sol[i]
                wct = instance.compute_wct(temp_sol)
                # print(i)
                if wct < min_wct:
                    min_wct = wct
                    min_sol = temp_sol
        if min_wct != initial_wct and min_sol:
            return min_sol, min_wct
        return None, initial_wct
    if neighbourhood_method == INSERT:
        for i in range(len(solution)):
            for j in range(len(solution)):
                temp_sol = solution.copy()
                temp_rem = temp_sol.pop(i)
                temp_sol.insert(j, temp_rem)
                wct = instance.compute_wct(temp_sol)
                # print(temp_sol)
                if wct < min_wct:
                    min_wct = wct
                    min_sol = temp_sol
        if min_wct != initial_wct and min_sol:
            return min_sol, min_wct
        return None, initial_wct
