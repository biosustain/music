__author__ = 'kaizhuang'

### Agricultural Sector Reaction Stoichiometries ###
stoichiometry = {}
reversibility = {}

### Energy Production ###

# Ref: BREW Report

# Primary Energy Production
energy_mix = {}

# EU Energy Mix, Chemical Industry, BREW Report
#energy_mix['petroleum'] = 0.25
#energy_mix['natural_gas'] = 0.7
#energy_mix['coal'] = 0.05
#stoichiometry['EU_energy_production'] = {}
#reversibility['EU_energy_production'] = False
#stoichiometry['EU_energy_production']['petroleum'] = -1/42.5*energy_mix['petroleum']
#stoichiometry['EU_energy_production']['natural_gas'] = -1/53.6*energy_mix['natural_gas']
#stoichiometry['EU_energy_production']['coal'] = -1/24.0*energy_mix['coal']# kg
#stoichiometry['EU_energy_production']['co2e'] = 0.075*energy_mix['petroleum'] + 0.057*energy_mix['natural_gas'] + 0.095*energy_mix['coal']#kg CO2 equivalents
#stoichiometry['EU_energy_production']['energy'] = energy_mix['petroleum'] + energy_mix['natural_gas'] + energy_mix['coal']# MJ

stoichiometry['energy_from_petroleum'] = {}
reversibility['energy_from_petroleum'] = False
stoichiometry['energy_from_petroleum']['petroleum'] = -1/42.5 # kg
stoichiometry['energy_from_petroleum']['co2e'] = 0.075 #kg CO2 equivalents
stoichiometry['energy_from_petroleum']['energy'] = 1 # MJ

stoichiometry['energy_from_natural_gas'] = {}
reversibility['energy_from_natural_gas'] = False
stoichiometry['energy_from_natural_gas']['natural_gas'] = -1/53.6 # kg
stoichiometry['energy_from_natural_gas']['co2e'] = 0.057 #kg CO2 equivalents
stoichiometry['energy_from_natural_gas']['energy'] = 1 # MJ

stoichiometry['energy_from_coal'] = {}
reversibility['energy_from_coal'] = False
stoichiometry['energy_from_coal']['coal'] = -1/24.0 # kg
stoichiometry['energy_from_coal']['co2e'] = 0.095 #kg CO2 equivalents
stoichiometry['energy_from_coal']['energy'] = 1 # MJ


# biodiesel
    # Ref: Hill 2006
stoichiometry['energy_from_biodiesel'] = {}
reversibility['energy_from_biodiesel'] = False
stoichiometry['energy_from_biodiesel']['biodiesel'] = -1/37.8 # kg
stoichiometry['energy_from_biodiesel']['co2e'] = 0.049 # no CO2 is released during burning
stoichiometry['energy_from_biodiesel']['energy'] = 1 # MJ

# Electricity and Steam Production Efficiency
eff_electricity = 0.4
eff_steam = 0.77
