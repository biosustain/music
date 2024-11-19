__author__ = 'Shahaf Cohen'

# Global Variables #
from cobra import Model, Reaction

# Define reactions
r_glc = 'EX_glc_e'
r_glyc = 'EX_glyc_e'
r_pdo = 'EX_1_3_pdo_e'
r_3hp = 'EX_3_hp_e'
r_o2 = 'EX_o2_e'

# Define conditions
AEROBIC = 'aerobic'
ANAEROBIC = 'anaerobic'

conditions = [AEROBIC, ANAEROBIC]
substrates = [r_glc, r_glyc]
targets = [r_pdo, r_3hp]
