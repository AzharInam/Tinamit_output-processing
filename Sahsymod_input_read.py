from tinamit.EnvolturasBF.SAHYSMOD._sahysmodIE import leer_info_dic_paráms
from envoltura import ModeloSAHYSMOD
import process_excel
import csv
import os
Mars_simulation = process_excel.data_process(nombre='Mars_sim')
directory = 'C:\\Users\\Azhar Inam\\Documents\\Mars\\CSVtoINP'
CSV_file = os.path.join(directory, 'SSDATA1.csv')
initial_data = os.path.join(directory, 'Mars.inp')
Sahysmod_vars = [
    'LC', 'IAA', 'IAB', 'GW', 'EPA', 'EPB', 'FSA', 'FW', 'PP', 'KAQ1', 'KAQ2', 'KAQ3', 'KAQ4'
]
Envoltura = ModeloSAHYSMOD(datos_iniciales=initial_data)
dic_ingr = leer_info_dic_paráms(archivo_fnt=initial_data)
Mars_comb = Mars_simulation.read_excel(CSV_file)
for run_no in range(Mars_simulation.row_count):
    for var in Sahysmod_vars:
        dic_ingr[var][0:] = Mars_comb[run_no][var]
    #write file with new inputfile location, sahysmod.inp template and param_ent
    #simulate model
    #read output
    #write output values in csv

print(Mars_comb)
