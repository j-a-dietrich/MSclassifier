from msbuddy import Msbuddy


def initialize_msbuddy():
    """ initialize the msbuddy engine 

    Args:
        None

    Returns:
        engine: msbuddy engine 
    """
    engine = Msbuddy()

    return engine


def search_formulas(engine, top_n:int=5, mass:float=664.108283, mass_tol:float=1, ppm:bool=True) -> list:
    """ uses msbuddy engine to search plausible molecular formulas based on accurate mass. 
        The current settings are for Hectochlorin with a molecular formula of C27H34Cl2N2O9S2

    Args:
        top_n (int): number of returned formulas
        mass (float): accurate mass
        mass_tol: accurate mass tolerance
        ppm: unit

    Returns:
        formulas: top_n formulas found by msbuddy engine
    """

    formulas_search_summary = engine.mass_to_formula(mass=mass, mass_tol=mass_tol, ppm=ppm)

    top_n_formulas = []
    for formula_search_summary in formulas_search_summary[:top_n]:
        formula = formula_search_summary.formula

        top_n_formulas.append(formula)

    return top_n_formulas



if __name__ == "__main__":
    engine = initialize_msbuddy()
    top_n_formulas = search_formulas(engine)
    print(top_n_formulas)
    
        

