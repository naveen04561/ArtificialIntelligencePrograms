from k_sat import Functions
from hill_climb import HillClimb
from beam_search import BeamSearch
from var_neigh import VarNeigh
from tabu import TabuSearch

def printS(state,boolval):
    if boolval:
        print("Found Solution: ", state)
    else:
        print("No Solution: ", state)

n = int(input("Enter the number of variables: "))
m = int(input("Enter the number of clauses: "))
k = int(input("Enter the length of each clause: "))
bits_changed = int(input("Enter the no. of bits to be changed: "))
initial_state = list(map(int,input("Enter the initial state: ").split()))

pf = [0,0,0,0,0]

beam_widths = [3,4]
var_functions = [1,2,3]
tabu_tenure = 4

f = Functions()
hc = HillClimb()
bs = BeamSearch()
vn = VarNeigh()
ts = TabuSearch()

for i in range(100):
    sat = f.generate_sat(n,m,k)
    # print("\nThe generated 3-sat problem is: ", sat)

    # Hill Climbing
    # print("\nHill Climbing")
    state, boolval = hc.hill_climbing(f, sat, initial_state, bits_changed, m)
    # printS(state,boolval)
    if boolval:
        pf[0]+=1
    # pf.append(boolval)

    #Beam Search
    # print("\nBeam Search - 3")
    state, boolval = bs.beam_search(f, sat, initial_state, bits_changed, m, beam_widths[0])
    # printS(state,boolval)
    if boolval:
        pf[1]+=1
    # pf.append(boolval)
    # print("\nBeam Search - 4")
    state, boolval = bs.beam_search(f, sat, initial_state, bits_changed, m, beam_widths[1])
    # printS(state,boolval)
    if boolval:
        pf[2]+=1
    # pf.append(boolval)

    # Variable Neighbourhood Descent
    # print("\nVariable Neighbourhood Descent")
    state, boolval = vn.var_neigh(f, sat, initial_state, var_functions, m)
    # printS(state,boolval)
    if boolval:
        pf[3]+=1
    # pf.append(boolval)

    #Tabu Search
    # print("\nTabu Search")
    state, boolval = ts.tabu_search(f, sat, initial_state, bits_changed, tabu_tenure, m)
    # printS(state,boolval)
    if boolval:
        pf[4]+=1
    # pf.append(boolval)

names = ["Hill Climbing","Beam Search - 3","Beam Search - 4","Variable Neighbourhood Descent","Tabu Search"]
# print("\nScores : ",pf)
for i in range(5):
    print(names[i],"=",pf[i])

    

