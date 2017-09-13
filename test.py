import unittest

import Int_To_Roman


class TestSingleValues(unittest.TestCase):
    def test_encode_single_I(self):
        self.assertEqual(Int_To_Roman.encode_num(1), 'I')

    def test_encode_single_IV(self):
        self.assertEqual(Int_To_Roman.encode_num(4), 'IV')

    def test_encode_single_V(self):
        self.assertEqual(Int_To_Roman.encode_num(5), 'V')

    def test_encode_single_IX(self):
        self.assertEqual(Int_To_Roman.encode_num(9), 'IX')

    def test_encode_single_X(self):
        self.assertEqual(Int_To_Roman.encode_num(10), 'X')

    def test_encode_single_XL(self):
        self.assertEqual(Int_To_Roman.encode_num(40), 'XL')

    def test_encode_single_L(self):
        self.assertEqual(Int_To_Roman.encode_num(50), 'L')

    def test_encode_single_XC(self):
        self.assertEqual(Int_To_Roman.encode_num(90), 'XC')

    def test_encode_single_C(self):
        self.assertEqual(Int_To_Roman.encode_num(100), 'C')

    def test_encode_single_CD(self):
        self.assertEqual(Int_To_Roman.encode_num(400), 'CD')

    def test_encode_single_D(self):
        self.assertEqual(Int_To_Roman.encode_num(500), 'D')

    def test_encode_single_CM(self):
        self.assertEqual(Int_To_Roman.encode_num(900), 'CM')

    def test_encode_single_M(self):
        self.assertEqual(Int_To_Roman.encode_num(1000), 'M')

class TestMultiValue(unittest.TestCase):
    def test_encode_straight_no_duplicates_no_multivalues(self):
        self.assertEqual(Int_To_Roman.encode_num(1666), 'MDCLXVI')

    def test_encode_straight_no_duplicates(self):
        self.assertEqual(Int_To_Roman.encode_num(1999), 'MCMXCIX')

    def test_encode_straight_duplicates(self):
        self.assertEqual(Int_To_Roman.encode_num(1988), 'MCMLXXXVIII')


