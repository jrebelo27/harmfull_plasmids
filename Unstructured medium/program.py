import variables
import cycles
import bacteria_distribution
import files_writing
import functions

quantity_donors = [99]*36
quantity_recipients = [9901]*36
adaptation_time_list = [200]*36
plasmid_cost_list = [0.2,0.4,0.6]*12
permanent_plasmid_cost_list = [0,0,0,0.05,0.05,0.05,0.1,0.1,0.1]*4
conjugation_rate_list = [0.001]*9+[0.01]*9+[0.1]*9+[1]*9
teta_one_list = [0.2]*36

for each_quantity in range(len(quantity_donors)):
    variables.donor_bacteria = quantity_donors[each_quantity]
    variables.number_plasmid_free_bacteria = quantity_recipients[each_quantity]
    variables.adaptation_time = adaptation_time_list[each_quantity]
    variables.initial_plasmid_cost = plasmid_cost_list[each_quantity]
    variables.permanent_plasmid_cost = permanent_plasmid_cost_list[each_quantity]
    variables.maximum_conjugation_rate = conjugation_rate_list[each_quantity]
    variables.teta_1 = teta_one_list[each_quantity]
    bacteria_list = bacteria_distribution.initial_bacteria()
    final_data = cycles.cycles(bacteria_list)

