"""Main module of your code

Author(s): Arjan Draisma, Mitja Zdouc

This code is covered under the GNU General Public License v3.0.
Please refer to the LICENSE located in the root of this repository.
"""

# imports are always at the top of your file
# they are sorted first by standard library
import sys

from module1.visualise import plot_pie_chart, draw_smiles
from module1.classification import results_aggregation, results_distribution, request_npclassifier, request_classyfire
from module1.database_search import get_smiles_from_formula, open_COCONUT
from module1.formula_search import initialize_msbuddy, search_formulas



if __name__ == "__main__":
    #file_name = sys.argv[0]

    engine = initialize_msbuddy()
    #top_5_formulas = search_formulas(engine, top_n=5, mass=180.063390)
    #top_5_formulas = search_formulas(engine, top_n=5, mass=224.141245)
    top_5_formulas = search_formulas(engine, top_n=5, mass=378.073955)
    print(top_5_formulas)
    top_1_formula = top_5_formulas[0]
    print(top_1_formula)

    feasibility_score = engine.predict_formula_feasibility(top_1_formula)
    print("feasibility score for formula prediction: ", feasibility_score)

    coconut_db = open_COCONUT()
    print("COCONUT DB loaded ...")
    smiles = get_smiles_from_formula(coconut_db, top_1_formula)
    print(len(smiles))

    np_results = request_npclassifier(smiles)
    class_results, superclass_results, pathway_results, isgly_coside = results_aggregation(np_results)
    distributed_class_results = results_distribution(superclass_results)
    
    plot_pie_chart(distributed_class_results)
   
    classyfire_results = request_classyfire(smiles)
    class_results, superclass_results, pathway_results, isgly_coside = results_aggregation(classyfire_results)
    distributed_class_results = results_distribution(class_results)
    
    plot_pie_chart(distributed_class_results)

