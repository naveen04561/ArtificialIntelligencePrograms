import random

class Functions:
    def eval_function(self, sat, state):
        clauses = sat.split("&")
        d = {}
        for i in range(len(state)):
            d[chr(ord('a')+i)] = state[i]
        value = 0
        for i in clauses:
            literals = i.split("V")
            boolval = 0
            if '~' in literals[0]:
                boolval = boolval or not(d[literals[0][2]])
            else:
                boolval = boolval or d[literals[0][1]]
            if '~' in literals[len(literals) - 1]:
                boolval = boolval or not(d[literals[len(literals) - 1][1]])
            else:
                boolval = boolval or d[literals[len(literals) - 1][0]]
            for j in range(1, len(literals)-1):
                if '~' in literals[j]:
                    boolval = boolval or not(d[literals[j][1]])
                else:
                    boolval = boolval or d[literals[j]]
            value += boolval
        return value


    def XOR(self, a, b):
        c = []
        for i in range(len(a)):
            c.append(a[i] ^ b[i])
        return c

    def revLexi(self, seq):
        max = True
        pos = len(seq)
        sett = 1 
        pos-=1
        while pos>=0 and (max or not(seq[pos])):
            if seq[pos]:
                sett += 1
            else:
                max = False
            pos-=1
        if pos<0:
            return False
        seq[pos] = 0
        pos+=1
        while pos < len(seq):
            seq[pos] = 1 if sett > 0 else 0
            sett -= 1
            pos+=1
        return True

    def generate_moves(self, state, bits_changed):
        state_len = len(state)
        candidate_solutions = []
        bits = [0 for i in range(state_len)]
        count = 0
        if bits_changed > state_len:
            bits_changed = state_len - (bits_changed - state_len) % 2
        while(bits_changed >= 0):
            for i in range(state_len):
                bits[i] = 1 if i < bits_changed else 0
            count+=1
            flip = self.XOR(state, bits)
            # print(state,bits,flip)
            candidate_solutions.append(flip)
            while self.revLexi(bits):
                count+=1
                flip = self.XOR(state, bits)
                # print(state,bits,flip)
                candidate_solutions.append(flip)
            bits_changed-=2
        if state in candidate_solutions:
            candidate_solutions.remove(state)
        return candidate_solutions

    def generate_sat(self,n,m,k):
        variables = ['a']
        for i in range(1,n):
            variables.append(chr(ord(variables[0])+i))

        for i in range(n):
            variables.append('~'+variables[i])

        sat = ''
        count=0
        while(True):
            clause = ''
            var = random.choice(variables)
            clause += (var+'V')
            exclude = [var]
            if '~' in var:
                exclude.append(var[1:])
            else:
                exclude.append('~'+var)
            for j in range(k-1):
                var2 = random.choice(list(filter(lambda literal: literal not in exclude, variables)))
                exclude.append(var2)
                if '~' in var2:
                    exclude.append(var2[1:])
                else:
                    exclude.append('~'+var2)
                clause+=var2
                if(j!=k-2):
                    clause+='V'
            clause = '('+clause+')'
            if clause not in sat:
                sat += clause
                count += 1
                if(count<m):
                    sat += '&'
            if count == m:
                break
        return sat


#"(bVc)&(cV~d)&(~bVa)&(~aV~e)&(eV~c)&(~cV~d)"