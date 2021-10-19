import variables
import cycles
import bacteria_distribution
import files_writing
import functions

quantity_donors = [9901]*36+[5000]*36+[99]*36+[10]*36+[9901]*36+[5000]*36+[99]*36+[10]*36
quantity_recipients = [99]*36+[5000]*36+[9901]*36+[9990]*36+[99]*36+[5000]*36+[9901]*36+[9990]*36
adaptation_time_list = [400]*144+[70]*144
plasmid_cost_list = [0.2,0.4,0.6]*96
permanent_plasmid_cost_list = ([0]*3+[0.05]*3+[0.1]*3)*32
conjugation_rate_list = ([0.001]*9+[0.01]*9+[0.1]*9+[1]*9)*8
teta_one_list = [0.2]*288

for each_quantity in range(0,288):
    variables.donors = 0
    variables.recipients = 0
    variables.transconjugants = 0
    variables.segregants = 0
    variables.number_type4 = 0
    variables.number_type5 = 0
    variables.number_type6 = 0    
    variables.n_bacteria_with_plasmid = quantity_donors[each_quantity]
    variables.n_bacteria_without_plasmid = quantity_recipients[each_quantity]
    variables.adaptation_time = adaptation_time_list[each_quantity]
    variables.initial_plasmid_cost = plasmid_cost_list[each_quantity]
    variables.permanent_plasmid_cost = permanent_plasmid_cost_list[each_quantity]
    variables.maximum_conjugation_rate = conjugation_rate_list[each_quantity]
    variables.teta_1 = teta_one_list[each_quantity]
    variables.donors = quantity_donors[each_quantity]
    variables.recipients = quantity_recipients[each_quantity]
    bacteria_list = bacteria_distribution.initial_bacteria()
    final_data = cycles.cycles(bacteria_list)

