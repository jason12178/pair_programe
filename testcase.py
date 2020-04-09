import unittest
from pair_programe import tax, Separate, joint, MPF

class TestStringMethods(unittest.TestCase):

    def testcase1(self):
        
        husband_income = 300000
        wife_income = 0
        husband_tax = tax(Separate(husband_income))
        wife_tax = tax(Separate(wife_income))
        joint_tax = tax(joint(husband_income,wife_income))
        husband_MPF=MPF(husband_income)
        wife_MPF=MPF(wife_income)
        
        self.assertEqual(husband_MPF,15000,"should be 15000")
        self.assertEqual(wife_MPF,0, "should be 0")
        self.assertEqual(wife_tax, 0, "should be 0")
        self.assertEqual(husband_tax, 9420, "should be 9420")
        self.assertEqual(joint_tax, 420, "should be 420")

    def testcase2(self):
        
        husband_income = 0
        wife_income = 500000
        husband_tax = tax(Separate(husband_income))
        wife_tax = tax(Separate(wife_income))
        joint_tax = tax(joint(husband_income,wife_income))
        husband_MPF=MPF(husband_income)
        wife_MPF=MPF(wife_income)

        self.assertEqual(husband_MPF,0, "should be 0")
        self.assertEqual(wife_MPF,18000, "should be 18000")
        self.assertEqual(wife_tax, 41500, "should be 41500")
        self.assertEqual(husband_tax, 0, "should be 0")
        self.assertEqual(joint_tax, 19060, "should be 19060")

    def testcase3(self):
        
        husband_income = 500000
        wife_income = 500000
        husband_tax = tax(Separate(husband_income))
        wife_tax = tax(Separate(wife_income))
        joint_tax = tax(joint(husband_income,wife_income))
        husband_MPF=MPF(husband_income)
        wife_MPF=MPF(wife_income)

        self.assertEqual(husband_MPF,18000, "should be 18000")
        self.assertEqual(wife_MPF,18000, "should be 18000")
        self.assertEqual(wife_tax, 41500, "should be 41500")
        self.assertEqual(husband_tax, 41500, "should be 41500")
        self.assertEqual(joint_tax, 101000, "should be 101000")

    def testcase4(self):
        
        husband_income = 100000
        wife_income = 200000
        husband_tax = tax(Separate(husband_income))
        wife_tax = tax(Separate(wife_income))
        joint_tax = tax(joint(husband_income,wife_income))
        husband_MPF=MPF(husband_income)
        wife_MPF=MPF(wife_income)

        self.assertEqual(husband_MPF,5000, "should be 5000")
        self.assertEqual(wife_MPF,10000, "should be 10000")
        self.assertEqual(wife_tax, 1480, "should be 1480")
        self.assertEqual(husband_tax, 0, "should be 0")
        self.assertEqual(joint_tax, 420, "should be 420")

if __name__ == '__main__':
    unittest.main()