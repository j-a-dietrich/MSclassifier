import requests
from collections import Counter


def request_classyfire(smiles_list: list):
    """ calls the NPClassifier API from GNPS for SMILES input and retrieves the predicted class

    Args:
        smiles_list: list of SMILES

    Returns:
        classyfire_kingdom (str): 
    """
    ClassyfireClasses = {}
    for smiles in smiles_list:
        url = f"https://structure.gnps2.org/classyfire?smiles={smiles}"

        classes = requests.get(url)
        classes_json = classes.json()

        ClassyfireClasses[smiles] = {"superclass_results": [classes_json["kingdom"]["name"]], "class_results": [classes_json["class"]["name"]]} # to create a similar dict as from npclassifier

    return ClassyfireClasses




def request_npclassifier(smiles_list: list):
    """ calls the NPClassifier API from GNPS for SMILES input and retrieves the predicted class

    Args:
        smiles_list: list of SMILES

    Returns:
        np_results: nested dictionary with a classification for each smiles
    """

    np_results = {}
    for smiles in smiles_list:
        url = f"https://npclassifier.gnps2.org/classify?smiles={smiles}"

        classes = requests.get(url)
        classes_json = classes.json()

        np_results[smiles] = classes_json

    return np_results


def results_aggregation(np_results:dict):
    """ aggregates the classes predicted by NPclassifier in four different lists (class, superclass, pathway, isgly_coside)

    Args:
        np_results (dict): json output from NPclassifier GNPS server

    Returns:
        class_results (list): class results for all molecules
        superclass_results (list): superclass results for all molecules
        pathway_results (list): pathway results for all molecules
        isgly_coside (list): isgly coside for all molecules
    """

    flatten_list = lambda l: [item for sublist in l for item in sublist] 

    class_results = []
    superclass_results = []
    pathway_results = []
    isgly_coside = []

    for results in np_results.values():
        class_results.append(results["class_results"])
        superclass_results.append(results["superclass_results"])
        #pathway_results.append(results["pathway_results"])
        #class_results.append(results["class_results"])

    class_results = flatten_list(class_results)
    superclass_results = flatten_list(superclass_results)
    pathway_results = flatten_list(pathway_results)
    isgly_coside = flatten_list(isgly_coside)

    return class_results, superclass_results, pathway_results, isgly_coside


def results_distribution(aggregated_results:list):
    """ uses Counter functionality to count item appearances in one result category

    Args:
        aggregated_results (list): list of for example all predicted classes for all molecules

    Returns:
        distributed_results (dict): dictionary with item and its count in the given list
    """

    distributed_results = Counter()

    for result in aggregated_results:
        distributed_results[result] += 1

    return distributed_results


if __name__ == "__main__":
    smiles_list = ["[H]OC(C1([H])OC(=O)C([H])(C([H])(OC(=O)C=2N=C(SC2[H])C([H])(OC(=O)C([H])([H])[H])C(OC(=O)C=3N=C1SC3[H])(C([H])([H])[H])C([H])([H])[H])C([H])([H])C([H])([H])C([H])([H])C(Cl)(Cl)C([H])([H])[H])C([H])([H])[H])(C([H])([H])[H])C([H])([H])[H]"]

    print("NPclassifier ...")
    np_results = request_npclassifier(smiles_list)
    class_results, superclass_results, pathway_results, isgly_coside = results_aggregation(np_results)
    print(class_results)
    distributed_class_results = results_distribution(class_results)
    print(distributed_class_results)

    print("Classifyre ...")
    classyfire_results = request_classyfire(smiles_list)
    print(classyfire_results)
    class_results, superclass_results, pathway_results, isgly_coside = results_aggregation(classyfire_results)
    print(class_results)
    distributed_class_results = results_distribution(class_results)
    print(distributed_class_results)

    