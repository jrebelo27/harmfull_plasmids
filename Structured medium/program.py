import variables
import cycles
import bacteria_distribution
import files_writing
import functions

quantity_donors = [9901]
quantity_recipients = [99]
adaptation_time_list = [210]
plasmid_cost_list = [0.6]
permanent_plasmid_cost_list = [0.05]
conjugation_rate_list = [0.01]
teta_one_list = [0]

for each_quantity in range(len(quantity_donors)):
    variables.donor_bacteria = quantity_donors[each_quantity]
    variables.number_plasmid_free_bacteria = quantity_recipients[each_quantity]
    variables.adaptation_time = adaptation_time_list[each_quantity]
    variables.initial_plasmid_cost = plasmid_cost_list[each_quantity]
    variables.permanent_plasmid_cost = permanent_plasmid_cost_list[each_quantity]
    variables.maximum_conjugation_rate = conjugation_rate_list[each_quantity]
    variables.teta_1 = teta_one_list[each_quantity]
    list_spaces = functions.initial_positions()
    list_spaces, filled_spaces = bacteria_distribution.initial_bacteria(list_spaces)
    final_data = cycles.cycles(list_spaces, filled_spaces)

