from rdkit.Chem import Mol
from rdkit.Chem.rdFMCS import MCSResult, FindMCS
from utils import *


def find_largest_mcs(mols: list[Mol]) -> tuple[list[Mol], MCSResult | None]:
    """Finds the first existing MCS in the list of molecules, by calculating the MCS for all
    combinations of sublists, beginning by the longest."""
    lists = generate_sublists_largest(mols)

    mcs: MCSResult | None = None
    sub = list[Mol]()
    while mcs is None or mcs.numAtoms == 0:
        sub = next(lists)
        mcs = FindMCS(sub)

    return sub, mcs
