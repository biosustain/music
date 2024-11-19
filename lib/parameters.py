__author__ = 'kaizhuang'


# Energy intensities of bioprocesses
# converted to MJ per unit of operation scale

Ei = {}   # energy intensities of bioprocesses

# fermentation
Ei['sterilization'] = 0.244 # MJ/L of media
Ei['agitation'] = 0.0018 #MJ/L/hr
Ei['aeration'] = 0.009 #MJ/L/hr, applicable only in aerobic environments

# separation of biomass
Ei['centrifugation_bacteria'] = 0.0252 # MJ/L
Ei['centrifugation_yeast'] = 0.0054 # MJ/L

# purification of product
Ei['evaporation_single_stage'] = 3.072   # MJ/L
Ei['evaporation_multi_stage'] = 1.238   # MJ/L

# efficiency at which primary energy is used by the chemical industry
E_efficiency = 0.4 # 40%, BREW report


