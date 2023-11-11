#import requests # maybe for pubchem
from pymongo import MongoClient
import pandas as pd

def open_COCONUT():
    """ initializes the coconut database as a data frame

    Args:
        None

    Returns:
        coconut_db (data frame): coconut data base unique natural product collection in a data frame
    """

    client = MongoClient("localhost",27017)
    db = client.COCONUTlatest
    collection = db.uniqueNaturalProduct

    coconut_db = pd.DataFrame(list(collection.find()))

    return coconut_db

def get_smiles_from_formula(coconut_db, formula:str="C27H34Cl2N2O9S2"):
    """ retrieves smiles from a given molecular formula from the coconut database

    Args:
        coconut_db (data frame): coconut database in from of a pandas data frame (other databases will have other column names)
        formula (str): molecular formula that should be searched for

    Returns:
        smiles (list of str): list of smiles with the desired molecular formula found in the coconut db
    """

    isomers = coconut_db.loc[coconut_db.molecular_formula == formula]

    smiles = isomers.smiles.to_list()

    return smiles
    


if __name__ == "__main__":
    coconut_db = open_COCONUT()
    smiles = get_smiles_from_formula(coconut_db)
    print(smiles)