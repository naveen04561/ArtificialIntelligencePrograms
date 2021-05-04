from k_sat import Functions

class BeamSearch:
    # Beam Search
    def beam_search_width(self, func, sat, candidates, bits_changed, number_clauses, beam_width):
        candidates_eval_values = []
        for i in candidates:
            candidates_eval_values.append(func.eval_function(sat, i))
            if number_clauses == func.eval_function(sat, i):
                return i, True
        candidate_solutions = []
        for i in candidates:
            l = func.generate_moves(i, bits_changed)
            for j in l:
                candidate_solutions.append(j)
        # print("Current states: ",candidates,"Candidates: ",candidate_solutions, "\n")
        next_candidates = []
        eval_values = []
        for i in candidate_solutions:
            eval_values.append([func.eval_function(sat, i),i])
        eval_values.sort()
        # for i in range(beam_width):
        #     if all(eval_values[i][0] > x for x in candidates_eval_values):
        #         next_candidates.append(eval_values[len(eval_values)-i-1][1])

        for i in eval_values:
            if any(i[0] > x for x in candidates_eval_values):
                next_candidates.append(i[1])
        # print("Next candidates: ",next_candidates, "\n")
        if len(next_candidates) == 0: 
            return next_candidates, False
        else:
            return self.beam_search_width(func, sat, next_candidates, bits_changed, number_clauses, beam_width)


    def beam_search(self,func, sat, state, bits_changed, number_clauses, beam_width):
        if number_clauses == func.eval_function(sat, state):
                return state, True
        value = func.eval_function(sat, state)
        candidate_solutions = func.generate_moves(state, bits_changed)
        # print("Current state: ",state,"Candidates: ",candidate_solutions, "\n")
        next_candidates = []
        eval_values = []
        for i in candidate_solutions:
            eval_values.append([func.eval_function(sat, i),i])
        eval_values.sort()
        for i in eval_values:
            if len(next_candidates) == beam_width:
                break
            if i[0] > value:
                next_candidates.append(i[1])
        
        if len(next_candidates) == 0:
            return [], False
            
        # for i in range(beam_width):
        #     if eval_values[len(eval_values)-i-1][0] > value:
        #         next_candidates.append(eval_values[len(eval_values)-i-1][1])
        #     else:
        #         break
        # print("Next candidates: ",next_candidates, "\n")
        return self.beam_search_width(func, sat, next_candidates, bits_changed, number_clauses, beam_width)

# n = int(input("Enter the number of variables: "))
# m = int(input("Enter the number of clauses: "))
# k = int(input("Enter the length of each clause: "))
# bits_changed = int(input("Enter the no. of bits to be changed: "))
# initial_state = list(map(int,input("Enter the initial state: ").split()))
# beam_width = int(input("Enter the beam width: "))

# f = Functions()
# bs = BeamSearch()
# sat = f.generate_sat(n,m,k)
# print("The generated 3-sat problem is: ", sat)

# state, boolval = bs.beam_search(f, sat, initial_state, bits_changed, m, beam_width)

# if boolval:
#     print("Found Solution: ", state)
# else:
#     print("No Solution: ", state)



#"(bVa)&(~aV~b)&(eV~b)&(~cVa)&(~eV~d)&(~dV~c)"

#"(bVc)&(cV~d)&(~bVa)&(~aV~e)&(eV~c)&(~cV~d)" beamwidth = 4, bits to be changed = 3

# Enter the number of variables: 8
# Enter the number of clauses: 5
# Enter the length of each clause: 2
# Enter the no. of bits to be changed: 4
# Enter the initial state: 1 1 1 1 1 1 1 1
# Enter the beam width: 4
# The generated 3-sat problem is:  (~bV~e)&(cV~d)&(bV~f)&(~fV~a)&(aVg)