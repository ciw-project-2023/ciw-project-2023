from abc import abstractmethod, ABC
from dataclasses import dataclass
from rdkit.Chem import Mol


@dataclass
class AlignResult:
    pass


class Aligner(ABC):
    @abstractmethod
    def align(self, mols: list[Mol]) -> AlignResult:
        pass


class AlignerStub(Aligner):
    def align(self, mols: list[Mol]) -> AlignResult:
        return AlignResult()
