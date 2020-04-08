import unittest
from pair_programe import tax, Separate, joint, MPF

class TestStringMethods(unittest.TestCase):

    def testcase1(self):
        
        husband_income = 300000
        wife_income = 0
        husband_tax = tax(Separate(husband_income))
        wife_tax = tax(Separate(wife_income))
        joint_tax = tax(joint(husband_income,wife_income))

        self.assertEqual(wife_tax, 0)
        self.assertEqual(husband_tax, 9420)
        self.assertEqual(joint_tax, 420)

    def testcase2(self):
        
        husband_income = 0
        wife_income = 500000
        husband_tax = tax(Separate(husband_income))
        wife_tax = tax(Separate(wife_income))
        joint_tax = tax(joint(husband_income,wife_income))

        self.assertEqual(wife_tax, 41500)
        self.assertEqual(husband_tax, 0)
        self.assertEqual(joint_tax, 19060)

if __name__ == '__main__':
    unittest.main()