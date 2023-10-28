import unittest
import pubchem
from aligner import *


class TestPubchemBioAssays(unittest.TestCase):
    def test_success(self):
        al = AlignerStub()
        assay = pubchem.mols_from_assay_id(0)
        result = al.align(assay)

        self.assertEqual(result, AlignResult())


if __name__ == '__main__':
    unittest.main()
