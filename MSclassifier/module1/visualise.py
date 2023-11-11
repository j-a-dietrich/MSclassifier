import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import Draw


def plot_pie_chart(distributed_results:dict):
    """ plots a pie chart for chemical classes

    Args:
        distributed_results (dict): dictionary with for example class results as key and count as value

    Returns:
        None
    """

    labels = []
    sizes = []

    for label, size in distributed_results.items():
        labels.append(label)
        sizes.append(size)

    plt.pie(sizes, labels=labels)

    plt.axis("equal")
    plt.show()


def draw_smiles(smiles_list:list):
    """ plots the 2D molecule structure from a list a SMILES

    Args:
        smiles_list (list(str)): list of SMILES

    Returns:
        None
    """

    for smiles in smiles_list:
        mol = Chem.MolFromSmiles(smiles)

        img = Draw.MolToImage(mol)
        
        plt.imshow(img)
        plt.axis('off') 
        plt.show()




if __name__ == "__main__":
    distributed_class_results = {'Cyclic peptides': 1, 'Depsipeptides': 1}
    plot_pie_chart(distributed_class_results)

    smiles_list = ["O=C1OC(C)(CC1)C2(C)CC=C(C)C(O)C2", "OC=1C=CC(=CC1O)C2=CC(OC)=C(O)C(OC)=C2"]
    draw_smiles(smiles_list)