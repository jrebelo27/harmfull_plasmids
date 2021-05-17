import functions
import random
import variables

def initial_bacteria():
    bacteria_list = [[],[],[]]
    for each_donor_bacterium in range(0, variables.donor_bacteria):
        bacteria_list[0].append(2)
        bacteria_list[1].append(variables.permanent_plasmid_cost)
        bacteria_list[2].append(0)
    for each_plasmid_free_bacterium in range(0, variables.number_plasmid_free_bacteria):
        bacteria_list[0].append(1)
        bacteria_list[1].append(0)
        bacteria_list[2].append(0)
    return bacteria_list
            
