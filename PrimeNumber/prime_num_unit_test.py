from unittest import TestCase
from PrimeNumber.prime_number import prime_number

class PrimeNumberUt(TestCase):
    def test_case1(self):
        print("Running test_case1 ...")
        res = self.assertEqual(prime_number(5),'Prime Number')

    def test_case2(self):
        print("Running test_case2 ...")
        self.assertEqual(prime_number(8),'Not Prime')

    def test_case3(self):
        print("Running test_case3 ...")
        self.assertEqual(prime_number(60),'Not Prime')

    def test_case4(self):
        print("Running test_case4 ...")
        self.assertEqual(prime_number(-1),'negative input')

    def test_case5(self):
        print("Running test_case 5 ...")
        self.assertEqual(prime_number(-0),'negative input')