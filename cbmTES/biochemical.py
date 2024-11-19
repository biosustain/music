import cobra
from cobra import Model, Reaction, Metabolite
import energy

# Define energy intensities for bioprocesses
Ei = {
    'sterilization': 0.244 / energy.eff_steam,  # MJ/L of media
    'agitation': 0.0018 / energy.eff_electricity,  # MJ/L/hr
    'aeration': 0.009 / energy.eff_electricity,  # MJ/L/hr (aerobic)
    'centrifugation_bacteria': 0.0252 / energy.eff_electricity,  # MJ/L
    'centrifugation_yeast': 0.0054 / energy.eff_electricity,  # MJ/L
    'evaporation_single_stage': 1.2 * 2.44 / energy.eff_steam + 0.04 * 3.6 / energy.eff_electricity,  # MJ/L
    'evaporation_multi_stage': 0.3 * 2.44 / energy.eff_steam + 0.005 * 3.6 / energy.eff_electricity,  # MJ/L
}

def add_bioprocess_reaction(
    model, A, B, strain, fermentation, separation, purification,
    purification_efficiency, neutralization=None, strain_id=None, 
    process_energy_intensity=None, compartment="c"
):
    """
    Add a bioprocess reaction A + E -> B + X + W to the COBRApy model.

    Parameters:
        - model: COBRApy model object.
        - A, B: Substrate and product IDs.
        - strain: Dictionary with strain data (yields, titer, etc.).
        - fermentation, separation, purification: Process types.
        - purification_efficiency: Efficiency of purification.
        - neutralization: Optional neutralization reaction.
        - strain_id: Identifier for the strain.
        - process_energy_intensity: Optional energy intensity data.
        - compartment: Cellular compartment (default "c").
    """
    # Extract strain data
    Y_B = strain['product_yield']  # kg/kg
    Y_X = strain['biomass_yield']  # kg/kg
    T = strain['product_titer'] / 1000.0  # kg/L
    P = strain['productivity'] / 1000.0  # kg/L/hr
    R_B = purification_efficiency

    if process_energy_intensity:
        global Ei
        Ei.update(process_energy_intensity)

    if not strain_id:
        strain_id = strain['strain_id']

    # Calculate energy cost yield
    if fermentation == 'aeroFB':
        Y_E_fermentation = Ei['sterilization'] * Y_B / T + Ei['agitation'] * Y_B / P + Ei['aeration'] * Y_B / P
    elif fermentation == 'anaeFB':
        Y_E_fermentation = Ei['sterilization'] * Y_B / T + Ei['agitation'] * Y_B / P

    if separation == 'ctrf':
        if 'ecoli' in strain_id:
            Y_E_separation = Ei['centrifugation_bacteria'] * Y_B / T
        elif 'scere' in strain_id:
            Y_E_separation = Ei['centrifugation_yeast'] * Y_B / T

    if purification == 'evapS':
        Y_E_purification = Ei['evaporation_single_stage'] * Y_B / T
    elif purification == 'evapM':
        Y_E_purification = Ei['evaporation_multi_stage'] * Y_B / T

    Y_E_overall = Y_E_fermentation + Y_E_separation + Y_E_purification

    # Calculate waste and overall product yields
    Y_W = 1 - Y_B - Y_X
    Y_B_overall = Y_B * R_B
    Y_W_overall = Y_W + (1 - R_B) * Y_B

    # Create the reaction
    rxn_id = f"BPR_{A}_{B}_{strain_id}_{fermentation}_{separation}_{purification}"
    reaction = Reaction(rxn_id)
    reaction.name = f"Bioprocess for {B}"
    reaction.lower_bound = 0
    reaction.upper_bound = 1000  # Arbitrary high value

    # Add metabolites to the reaction
    reaction.add_metabolites({
        f"{A}_{compartment}": -1,
        f"energy_{compartment}": -Y_E_overall,
        f"{B}_{compartment}": Y_B_overall,
        f"biomass_{compartment}": Y_X,
        f"waste_organic_{compartment}": Y_W_overall,
    })

    # Neutralization (specific for 3HP neutralization with lime)
    if neutralization == '3hp_lime':
        reaction.add_metabolites({
            f"lime_{compartment}": -0.4113 * Y_B,
            f"sulfuric_acid_{compartment}": -0.5444 * Y_B,
            f"gypsum_{compartment}": 0.7557 * Y_B,
        })

    # Add reaction to the model
    model.add_reactions([reaction])

# Example usage
model = Model("Bioprocess_Model")
add_bioprocess_reaction(
    model, A="glucose", B="lactate",
    strain={
        'product_yield': 0.5, 'biomass_yield': 0.1, 
        'product_titer': 50, 'productivity': 2, 'strain_id': 'ecoli_1'
    },
    fermentation="aeroFB", separation="ctrf", purification="evapS",
    purification_efficiency=0.9, compartment="c"
)

print(f"Reactions in the model: {[rxn.id for rxn in model.reactions]}")
