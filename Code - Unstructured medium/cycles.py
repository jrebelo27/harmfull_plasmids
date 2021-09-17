import random
import variables
import functions
import time
import files_writing
import time
import numpy
import copy

def cycles (bacteria_list):
    duplications = 0
    final_data = []
    conjugation_data = []
    grid_area = variables.grid_edge*variables.grid_edge    
    number_times_full_grid = 0
    each_cycle = 0
    counter = 0
    number_conjugation_attempts = 0
    number_conjugations = 0
    counter = 0
    while number_times_full_grid <= 1073:        
        each_cycle += 1
        position_focal_bacterium = random.sample(range(0,len(bacteria_list[0])), 1)[0]   
        c = (grid_area-len(bacteria_list))/grid_area            
        growth_rate = variables.maximum_growth_rate-bacteria_list[1][position_focal_bacterium]
        growth_probability = functions.growth_rate_function(growth_rate, c)
        #bacterial growth
        if random.random() <= growth_probability:
            bacteria_list = functions.bacterial_growth(position_focal_bacterium, bacteria_list)   
        #conjugation
        if variables.recipients > 0 or variables.segregants > 0:
            if bacteria_list[0][position_focal_bacterium] == 2 or bacteria_list[0][position_focal_bacterium] == 3:            
                encounter_probability = ((variables.donors+variables.transconjugants)/len(bacteria_list[0]))*((variables.recipients+variables.segregants)/len(bacteria_list[0]))
                if random.random() <= encounter_probability:
                    number_conjugation_attempts += 1
                    conjugation_probability = functions.conjugation_rate_function(c)
                    if random.random() <= conjugation_probability:
                        proportion_recipients_segregants = variables.recipients/(variables.recipients+variables.segregants)
                        if random.random()<= proportion_recipients_segregants:
                            position_bacterium_to_conjugate = bacteria_list[0].index(1)
                        else:
                            if variables.number_type4 > 0 and variables.number_type5 > 0 and variables.number_type6 > 0:
                                proportion_type4 = variables.number_type4/(variables.number_type4+variables.number_type5+variables.number_type6)
                                proportion_type5 = (variables.number_type4+variables.number_type5)/(variables.number_type4+variables.number_type5+variables.number_type6)
                                if random.random() <= proportion_type4:
                                    position_bacterium_to_conjugate = bacteria_list[0].index(4)
                                elif random.random() > proportion_type4 and random.random() < proportion_type5:
                                    position_bacterium_to_conjugate = bacteria_list[0].index(5)
                                else:
                                    position_bacterium_to_conjugate = bacteria_list[0].index(6)
                            elif variables.number_type4 == 0:
                                 proportion_type5 = variables.number_type5/(variables.number_type4+variables.number_type5+variables.number_type6)
                                 if random.random() < proportion_type5:
                                     try:
                                         position_bacterium_to_conjugate = bacteria_list[0].index(5)
                                     except:
                                         print("counter: ", variables.number_type5)
                                         print("Real: ", bacteria_list[0].count(5))
                                         position_bacterium_to_conjugate = bacteria_list[0].index(5)
                                 else:
                                     try:
                                         position_bacterium_to_conjugate = bacteria_list[0].index(6)
                                     except:
                                         print("counter: ", variables.number_type6)
                                         print("Real: ", bacteria_list[0].count(6))
                                         position_bacterium_to_conjugate = bacteria_list[0].index(6)      
                            elif variables.number_type5 == 0:
                                 proportion_type4 = variables.number_type4/(variables.number_type4+variables.number_type5+variables.number_type6)
                                 if random.random() < proportion_type4:
                                     position_bacterium_to_conjugate = bacteria_list[0].index(4)
                                 else:
                                     position_bacterium_to_conjugate = bacteria_list[0].index(6)
                            elif variables.number_type6 == 0:
                                 proportion_type4 = variables.number_type4/(variables.number_type4+variables.number_type5+variables.number_type6)
                                 if random.random() < proportion_type4:
                                     position_bacterium_to_conjugate = bacteria_list[0].index(4)
                                 else:
                                     position_bacterium_to_conjugate = bacteria_list[0].index(5)
                        number_conjugations += 1
                        bacteria_list = functions.conjugation(position_bacterium_to_conjugate,bacteria_list)
        if len(bacteria_list[0])/grid_area >= variables.maximum_proportion_full_grid:
            counter = 0
            number_times_full_grid += 1
            print(number_times_full_grid)
            conjugation_data.append([number_conjugation_attempts, number_conjugations,number_times_full_grid])
            number_conjugation_attempts = 0
            number_conjugations = 0
            recipients = bacteria_list[0].count(1)
            donors = bacteria_list[0].count(2)
            transconjugants = bacteria_list[0].count(3)
            segregants = bacteria_list[0].count(4)+bacteria_list[0].count(5)+bacteria_list[0].count(6)
            final_data.append([recipients, donors, transconjugants,segregants,variables.number_adaptations, each_cycle])        
            number_to_eliminate = int((variables.maximum_proportion_full_grid-variables.remaining_proportion_grid)*grid_area)
            remaining_positions = random.sample(range(0, len(bacteria_list[0])), (len(bacteria_list[0])-number_to_eliminate))
            new_list = [[],[],[]]
            for each_position in remaining_positions:
                new_list[0].append(bacteria_list[0][each_position])
                new_list[1].append(bacteria_list[1][each_position])
                new_list[2].append(bacteria_list[2][each_position])  
            bacteria_list = copy.deepcopy(new_list)
            if (recipients+segregants) == 950000 or (donors+segregants) == 950000 or (transconjugants+segregants) == 950000:
                number_times_full_grid = 1074
            recipients = bacteria_list[0].count(1)
            donors = bacteria_list[0].count(2)
            transconjugants = bacteria_list[0].count(3)
            segregants = bacteria_list[0].count(4)+bacteria_list[0].count(5)+bacteria_list[0].count(6)
            type4 = bacteria_list[0].count(4)
            type5 = bacteria_list[0].count(5)
            type6 = bacteria_list[0].count(6)
            variables.recipients = recipients
            variables.donors = donors
            variables.tranconjugantes = transconjugants
            variables.segregants = segregants
            variables.number_type4 = type4
            variables.number_type5 = type5
            variables.number_type6 = type6                 
    files_writing.writing_final_data(final_data, number_times_full_grid)
    files_writing.writing_conjugation_data(conjugation_data, number_times_full_grid)
