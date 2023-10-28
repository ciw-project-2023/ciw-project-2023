import csv
import requests
from rdkit.Chem import Mol, MolFromSmiles
from io import StringIO

def bioassay_url_builder(aid: int) -> str:
    return 'https://pubchem.ncbi.nlm.nih.gov/assay/pcget.cgi?query=download&record_type=datatable&actvty=active&response_type=save&aid={}'.format(aid)


def mols_from_csv_file(fileName: str) -> list[Mol]:
    mols = list[Mol]()

    with open(fileName) as file:
        for row in csv.DictReader(file):
            try:
                smiles = row['PUBCHEM_EXT_DATASOURCE_SMILES']
                mol = MolFromSmiles(smiles)
                mols.append(mol)
            except Exception as error:
                print(error)
                continue

    return mols


def mols_from_assay_id(aid: int, type='active') -> list[Mol]:
    mols = list[Mol]()

    url = bioassay_url_builder(aid)
    resp = requests.get(url)

    if resp.status_code == 200:
        content = resp.text
        data = StringIO(content)
        for row in csv.DictReader(data):
            smiles = row['PUBCHEM_EXT_DATASOURCE_SMILES']
            mols.append(MolFromSmiles(smiles))
    else:
        raise Exception("could not make pubchem request: received error {}: {}", resp.status_code, resp.text)

    return mols

