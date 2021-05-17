import random
import variables
import math

def growth_rate_function(maximum_growth_rate, c):
    if c >= variables.teta:
        growth_probability = maximum_growth_rate
    else:
        growth_probability = maximum_growth_rate*(c/variables.teta)
    return growth_probability

def bacterial_growth (bacterium_position, list_all_bacteria):
    if list_all_bacteria[0][bacterium_position] == 1:
        cost = 0
    if list_all_bacteria[0][bacterium_position] == 2:
        cost = list_all_bacteria[1][bacterium_position]
    decreased_time = 0      
    if list_all_bacteria[0][bacterium_position] == 3:
        if list_all_bacteria[2][bacterium_position] != 0:
            decreased_time = list_all_bacteria[2][bacterium_position] - 1
            if decreased_time == 0:
                cost = variables.permanent_plasmid_cost
                variables.adaptations_number += 1
            else:
                cost = list_all_bacteria[1][bacterium_position]
        else:
            cost = list_all_bacteria[1][bacterium_position]
    list_all_bacteria[0].append(list_all_bacteria[0][bacterium_position])
    list_all_bacteria[1].append(cost)
    list_all_bacteria[2].append(decreased_time)
    list_all_bacteria[1][bacterium_position] = cost
    list_all_bacteria[2][bacterium_position] = decreased_time
    return list_all_bacteria

def conjugation_rate_function(c):
    if c >= variables.teta_2:
        conjugation_probability = variables.maximum_conjugation_rate
    elif c < variables.teta_1:
        conjugation_probability = 0
    else:
        conjugation_probability = variables.maximum_conjugation_rate*((c-variables.teta_1)/(variables.teta_2-variables.teta_1))
    return conjugation_probability

def conjugation(bacteria_to_conjugate, list_all_bacteria):
    variables.recipient_bacteria -= 1
    list_all_bacteria[0][bacteria_to_conjugate] = 3
    list_all_bacteria[1][bacteria_to_conjugate] = variables.initial_plasmid_cost
    list_all_bacteria[2][bacteria_to_conjugate] = variables.adaptation_time
    return list_all_bacteria


    





































    

