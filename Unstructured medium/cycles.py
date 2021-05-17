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
    
    while number_times_full_grid <= 500:        
        
        each_cycle += 1
        position_focal_bacterium = random.sample(range(0,len(bacteria_list[0])), 1)[0]
        
        #check the amount of nutrients
        c = (grid_area-len(bacteria_list))/grid_area            

        growth_rate = variables.maximum_growth_rate-bacteria_list[1][position_focal_bacterium]
        growth_probability = functions.growth_rate_function(growth_rate, c)

        #bacterial growth
        if random.random() <= growth_probability:
            bacteria_list = functions.bacterial_growth(position_focal_bacterium, bacteria_list)
        
        #conjugation
        if bacteria_list[0][position_focal_bacterium] == 2 or bacteria_list[0][position_focal_bacterium] == 3:

            position_bacterium_to_conjugate = random.sample(range(0,len(bacteria_list)), 1)[0]

            if bacteria_list[0][position_bacterium_to_conjugate] == 1:
                number_conjugation_attempts += 1
                conjugation_probability = functions.conjugation_rate_function(c)
                if random.random() <= conjugation_probability:
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

            final_data.append([recipients, donors, transconjugants,variables.number_adaptations, each_cycle])        

            number_to_eliminate = int((variables.maximum_proportion_full_grid-variables.remaining_proportion_grid)*grid_area)
            
            remaining_positions = random.sample(range(0, len(bacteria_list[0])), (len(bacteria_list[0])-number_to_eliminate))

            new_list = [[],[],[]]
    
            for each_position in remaining_positions:
                new_list[0].append(bacteria_list[0][each_position])
                new_list[1].append(bacteria_list[1][each_position])
                new_list[2].append(bacteria_list[2][each_position])

                
            bacteria_list = copy.deepcopy(new_list)
            
            
            if recipients == 950000 or donors == 950000 or transconjugants == 950000:
                number_times_full_grid = 501
                       
                             
    files_writing.writing_final_data(final_data, number_times_full_grid)
    files_writing.writing_conjugation_data(conjugation_data, number_times_full_grid)
            
        
