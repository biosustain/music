__author__ = 'kaizhuang & Shahaf Cohen'

####################
# Global Variables #
####################
from cobra import Model, Reaction
from collections import OrderedDict

# Define reactions
r_glc = Reaction('R_EX_glc_e')
r_glyc = Reaction('R_EX_glyc_e')
r_pdo = Reaction('R_EX_1_3_pdo_e')
r_3hp = Reaction('R_EX_3_hp_e')
r_o2 = Reaction('R_EX_o2_e')
r_3HPP = Reaction('R_EX_3HPP_e')
r_13PDO = Reaction('R_EX_13PDO_e')

# Define conditions
AEROBIC = 'aerobic'
ANAEROBIC = 'anaerobic'

conditions = [AEROBIC, ANAEROBIC]
substrates = [r_glc, r_glyc]
targets = [r_pdo, r_3hp]

# Define FBA constraints
fba_constraints = OrderedDict()

fba_constraints['ecoli', 'R_EX_glc_e', AEROBIC] = {r_glc.id: (-10, 0), r_glyc.id: (0, 0), r_o2.id: (-15, None)}
fba_constraints['ecoli', 'R_EX_glc_e', ANAEROBIC] = {r_glc.id: (-20, 0), r_glyc.id: (0, 0), r_o2.id: (0, None)}
fba_constraints['ecoli', 'R_EX_glyc_e', AEROBIC] = {r_glc.id: (0, 0), r_glyc.id: (-15, 0), r_o2.id: (-15, None)}
fba_constraints['ecoli', 'R_EX_glyc_e', ANAEROBIC] = {r_glc.id: (0, 0), r_glyc.id: (-15, 0), r_o2.id: (0, None)}

# B. Sonnleitner 1986
fba_constraints['scere', 'R_EX_glc_e', AEROBIC] = {r_glc.id: (-20, 0), r_glyc.id: (0, 0), r_o2.id: (-8, None)}
fba_constraints['scere', 'R_EX_glc_e', ANAEROBIC] = {r_glc.id: (-20, 0), r_glyc.id: (0, 0), r_o2.id: (-0.05, None)}
# Ocha-Estopier 2010
fba_constraints['scere', 'R_EX_glyc_e', AEROBIC] = {r_glc.id: (0, 0), r_glyc.id: (-4.5, 0), r_o2.id: (-8, None)}
