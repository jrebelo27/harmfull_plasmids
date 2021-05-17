import csv
import variables

def writing_final_data (final_data, number_times_full_grid):
    name = "density_data_unstructured_medium_".strip()+str(number_times_full_grid).strip()+"remaining_proportion".strip()+str(variables.remaining_proportion_grid).strip()+"teta_one".strip()+str(variables.teta_1).strip()+"initial_plasmid_cost".strip()+str(variables.initial_plasmid_cost).strip()+"permanent_plasmid_cost".strip()+str(variables.permanent_plasmid_cost).strip()+"adaptation_time".strip()+str(variables.adaptation_time).strip()+"conjugation_rate".strip()+str(variables.maximum_conjugation_rate).strip()+"D_R".strip()+str(variables.donor_bacteria).strip()+"_".strip()+str(variables.number_plasmid_free_bacteria).strip()+".csv".strip()
    with open(name, 'w', newline='') as csvfile:
        ficheiro = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        ficheiro.writerow(["recipients".strip()+','.strip()+ "donors".strip()+','.strip()+ "transconjugants".strip()+','.strip()+ "adaptations_number".strip()+','.strip()+ "cycle".strip()])
        for each_line in range(0, len(final_data)):
            ficheiro.writerow([str(final_data[each_line][0]).strip()+','.strip()+str(final_data[each_line][1]).strip()+','.strip()+str(final_data[each_line][2]).strip()+','.strip()+str(final_data[each_line][3]).strip()+','.strip()+str(final_data[each_line][4]).strip()])

def writing_conjugation_data (conjugation_data, number_times_full_grid):
    name = "conjugation_data_unstructured_medium_".strip()+str(number_times_full_grid).strip()+"remaining_proportion".strip()+str(variables.remaining_proportion_grid).strip()+"teta_one".strip()+str(variables.teta_1).strip()+"initial_plasmid_cost".strip()+str(variables.initial_plasmid_cost).strip()+"permanent_plasmid_cost".strip()+str(variables.permanent_plasmid_cost).strip()+"adaptation_time".strip()+str(variables.adaptation_time).strip()+"conjugation_rate".strip()+str(variables.maximum_conjugation_rate).strip()+"D_R".strip()+str(variables.donor_bacteria).strip()+"_".strip()+str(variables.number_plasmid_free_bacteria).strip()+".csv".strip()
    with open(name, 'w', newline='') as csvfile:
        ficheiro = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        ficheiro.writerow(["attempts".strip()+','.strip()+ "conjugation_events".strip()+','.strip()+"cycle".strip()])
        for each_line in range(0, len(conjugation_data)):
            ficheiro.writerow([str(conjugation_data[each_line][0]).strip()+','.strip()+str(conjugation_data[each_line][1]).strip()+','.strip()+str(conjugation_data[each_line][2]).strip()])



