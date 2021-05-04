from k_sat import Functions

class VarNeigh:
    def hill_climbing(self, f, sat, state, bits_changed, number_clauses):
            if number_clauses == f.eval_function(sat, state):
                return state, True
            else:
                candidate_solutions = f.generate_moves(state, bits_changed)
                # print("Candidate Solutions: ",candidate_solutions)
                next_candidate = []
                max_value = f.eval_function(sat, state)
                got = False
                for i in candidate_solutions:
                    val = f.eval_function(sat, i)
                    if max_value < val:
                        got = True
                        next_candidate.clear()
                        next_candidate = i.copy()
                if got == False:
                    return state, False
                else:
                    # print("Next Candidate: ", next_candidate)
                    return self.hill_climbing(f, sat, next_candidate, bits_changed, number_clauses)


    def var_neigh(self, f, sat, state, bits_changed, number_clauses):
        for i in range(len(bits_changed)):
            state, boolval = self.hill_climbing(f, sat, state, bits_changed[i], number_clauses)
            if boolval:
                return state, boolval
        if i == len(bits_changed)-1:
            return state, False


# n = int(input("Enter the number of variables: "))
# m = int(input("Enter the number of clauses: "))
# k = int(input("Enter the length of each clause: "))
# initial_state = list(map(int,input("Enter the initial state: ").split()))

# bits_changed = []
# for i in range(3):
#     bits_changed.append(int(input("Enter the no. of bits to be changed for the {} th function: ".format(i+1))))

# f = Functions()
# vn = VarNeigh()
# sat = f.generate_sat(n,m,k)
# print("The generated 3-sat problem is: ", sat)

# state, boolval = vn.var_neigh(f, sat, initial_state, bits_changed, m)

# if boolval:
#     print("Found Solution: ", state)
# else:
#     print("No Solution: ", state)