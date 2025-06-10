import argparse
from rdkit import Chem
from rdkit.Chem.SaltRemover import SaltRemover
import pubchempy as pcp

def name_to_smiles(name):
    try:
        compounds = pcp.get_compounds(name, 'name')
        if compounds:
            return compounds[0].isomeric_smiles
        else:
            return None
    except Exception as e:
        return None

def process_names_file(input_file, output_file):
    remover = SaltRemover()
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            name = line.strip()
            if not name:
                continue
            smiles = name_to_smiles(name)
            if not smiles:
                outfile.write(f"NOT_FOUND\t{name}\n")
                continue
            mol = Chem.MolFromSmiles(smiles)
            if mol:
                clean_mol = remover.StripMol(mol)
                canonical_smiles = Chem.MolToSmiles(
                    clean_mol, canonical=True, isomericSmiles=True
                )
                outfile.write(f"{canonical_smiles}\t{name}\n")
            else:
                outfile.write(f"INVALID_SMILES\t{name}\n")

    print(f"✅ Done! Cleaned output saved to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Retrieve, clean, and canonicalize SMILES from compound names."
    )
    parser.add_argument("-i", "--input", required=True, help="Input file with compound names (one per line)")
    parser.add_argument("-o", "--output", required=True, help="Output cleaned SMILES file")
    args = parser.parse_args()

    process_names_file(args.input, args.output)
