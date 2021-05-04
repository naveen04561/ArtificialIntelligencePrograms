from k_sat import Functions

class HillClimb:
    # Hill Climbing algorithm
    def hill_climbing(self, f, sat, state, bits_changed, number_clauses):
        if number_clauses == f.eval_function(sat, state):
            return state, True
        else:
            candidate_solutions = f.generate_moves(state, bits_changed)
            # print("Candidates: ", candidate_solutions)
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
                return [], False
            else:
                # print("Next Candidate: ", next_candidate)
                return self.hill_climbing(f, sat, next_candidate, bits_changed, number_clauses)

# n = int(input("Enter the number of variables: "))
# m = int(input("Enter the number of clauses: "))
# k = int(input("Enter the length of each clause: "))
# bits_changed = int(input("Enter the no. of bits to be changed: "))
# initial_state = list(map(int,input("Enter the initial state: ").split()))

# f = Functions()
# h = HillClimb()
# sat = f.generate_sat(n,m,k)
# print("The generated 3-sat problem is: ", sat)

# state, boolval = h.hill_climbing(f, sat, initial_state, bits_changed, m)

# if boolval:
#     print("Found Solution: ", state)
# else:
#     print("No Solution: ", state)


#"(bVa)&(~aV~b)&(eV~b)&(~cVa)&(~eV~d)&(~dV~c)"