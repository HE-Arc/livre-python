import unittest
# definition
def carre(x):
    return x ** 2
# classTest
class Testeur(unittest.TestCase):
    testValues = {2:4, 0:0, -2:4}
    def testCarre(self):
        for i, a in self.testValues.items():
            self.assertEqual(carre(i),a)
#execution
if __name__ == '__main__':
    unittest.main()
