from k_sat import Functions


class TabuSearch:
    def tabu(self, f, sat, state, bits_changed, tabu_tenure, number_clauses, m):
        global max_value
        if number_clauses == f.eval_function(sat, state):
            return state, True
        else:
            value = f.eval_function(sat, state)
            l = []
            for i in range(len(state)):
                if m[i] == 0:
                    l.append(state[i])
            cs = f.generate_moves(l, bits_changed)
            next_candidates = []
            eval_values = []
            for j in cs:
                state_copy = state.copy()
                p = 0
                for i in range(len(state)):
                    if m[i] == 0:
                        state_copy[i] = j[p]
                        p += 1
                eval_values.append([f.eval_function(sat, state_copy),state_copy])
            eval_values.sort()
            for i in eval_values:
                if i[0] > value:
                    next_candidates.append(i[1])
            # print("Next Candidates ",next_candidates)
            if len(next_candidates) == 0:
                evalcand = [x[1] for x in eval_values]
                # print("evalcand",evalcand)
                candidates = f.generate_moves(state, bits_changed)
                # print("candidates",candidates)
                cand = list(filter(lambda st: st not in evalcand, candidates))
                # print("cand",cand)
                cand_eval = []
                for i in cand:
                    cand_eval.append([f.eval_function(sat, i),i])
                # cand_eval.sort()
                for i in cand_eval:
                    if i[0] > max_value:
                        next_candidates.append(i[1])
                        max_value = i[0]
                if len(next_candidates) == 0:
                    return [], False
                else:
                    fc = []
                    for i in next_candidates:
                        for j in m:
                            j = 0
                        c1,c2 = self.tabu(f, sat, i, bits_changed, tabu_tenure, number_clauses, m)
                        fc.append(c1)
                    return fc,True
            else:
                max_value = eval_values[len(eval_values)-1][0]
                fc1 = []
                for i in next_candidates:
                    for j in range(len(state)):
                        if state[j] != i[j]:
                            m[j] = tabu_tenure
                        else:
                            m[j] -= 1
                    d1,d2 = self.tabu(f, sat, i, bits_changed, tabu_tenure, number_clauses, m)
                    fc1.append(d1)
                return fc1,True

    def tabu_search(self, f, sat, state, bits_changed, tabu_tenure, number_clauses):
        global max_value
        if number_clauses == f.eval_function(sat, state):
            return [state], True
        else:
            candidate_solutions = f.generate_moves(state, bits_changed)
            max_value = f.eval_function(sat, state)
            next_candidates = []
            eval_values = []
            for i in candidate_solutions:
                eval_values.append([f.eval_function(sat, i),i])
            eval_values.sort()
            for i in eval_values:
                if i[0] > max_value:
                    next_candidates.append(i[1])
                    max_value = i[0]
            if len(next_candidates) == 0:
                return [], False
            # print("Next Candidates ",next_candidates)
            m = [0 for x in range(len(state))]
            fc = []
            for i in next_candidates:
                for j in range(len(state)):
                    if i[j] != state[j]:
                        m[j] = tabu_tenure
                # print(i,"m", m)
                c1, c2 = self.tabu(f, sat, i, bits_changed, tabu_tenure, number_clauses, m)
                fc.append(c1)
            return fc, True
max_value = 0
# n = int(input("Enter the number of variables: "))
# m = int(input("Enter the number of clauses: "))
# k = int(input("Enter the length of each clause: "))
# bits_changed = int(input("Enter the no. of bits to be changed: "))
# initial_state = list(map(int,input("Enter the initial state: ").split()))
# tabu_tenure = int(input("Enter the tabu tenure: "))


# f = Functions()
# ts = TabuSearch()
# sat = f.generate_sat(n,m,k)
# print(sat)

# max_value = f.eval_function(sat, initial_state)

# state, boolval = ts.tabu_search(f, sat, initial_state, bits_changed, tabu_tenure, m)

# if boolval:
#     print("Found Solution: ", state)
# else:
    # print("No Solution: ", state)

















#"(~dVcVb)&(dVcVb)&(~dV~bV~c)&(eV~bV~d)&(eVaVb)&(dVaV~b)"

#"(bVa)&(~aV~b)&(eV~b)&(~cVa)&(~eV~d)&(~dV~c)" no solution

#"(bVc)&(cV~d)&(~bVa)&(~aV~e)&(eV~c)&(~cV~d)" no solution

#"(~aV~b)&(~cVb)&(cVd)&(~dVb)&(aVd)"


   # return self.tabu(f, sat, state, bits_changed, tabu_tenure, number_clauses)
            # M = []
            # for i in range(len(state)):
            #     M.append(0)
            # candidate_solutions = f.generate_moves(state, bits_changed)
            # for i in candidate_solutions:
            #     if number_clauses == f.eval_function(sat, i):
            #         return state, True
            #     for j in range(len(i)):
            #         if i[j] != state[j]:
            #             M[j] = tabu_tenure
            #     l = []
            #     for j in range(len(i)):
            #         if(M[j] == 0):
            #             l.append(i[j])
            #     cs = f.generate_moves(l, bits_changed)
            #     for k in cs:
            #         p = 0
            #         for j in range(len(i)):
            #             if M[j] == 0 and i[j] != k[p]:
            #                 p += 1
            #                 M[j] = tabu_tenure
            #                 i[j] = k[p]
            #             else:
            #                 M[j] -= 1
            #         if number_clauses == f.eval_function(sat, i):
            #             return state, True