def divide_conquer(problem, param1, param2,...):
    if problem is None:
        print_result
        return

    #prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    #conquer subproblems
    subres1 = self.divide_conquer(subproblem[0], p1, ...)
    subres2 = self.divide_conquer(subproblem[1], p1, ...)
    subres3 = self.divide_conquer(subproblem[2], p1, ...)

    #process and generate the final result
    result = process_result(subres1, subres2, subres3,...)

    #revert the current level state


def divide_conquer(problem, param1, param2,...):
    if problem is None:
        print_result
        return

    #prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    subres1 = self.divide_conquer(subproblems[0], p1, ...)
    subres2 = self.divide_conquer(subproblems[1], p1, ...)
    subres3 = self.divide_conquer(subproblems[2], p1, ...)

    result = process_result(subres1, subres2, subres3)

def divide_conquer(problem, param1, param2, ...):
    if problem is None:
        print_result
        return

    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    subres1 = self.divide_conquer(subprolbems[0], p1, ...)
    subres2 = self.divide_conquer(subprolbems[1], p1, ...)
    subres3 = self.divide_conquer(subprolbems[2], p1, ...)

    result = process_result(subres1, subres2, subres3)
