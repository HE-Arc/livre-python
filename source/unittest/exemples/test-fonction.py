import unittest


# definition
def carre(x):
    """Return x**2"""
    return x ** 2


# classTest
class Testeur(unittest.TestCase):
    """Class with one test"""
    testValues = {2: 4, 0: 0, -2: 4}

    def testCarre(self):
        """Test the function carre"""
        for i, a in self.testValues.items():
            self.assertEqual(carre(i), a)


# execution
if __name__ == '__main__':
    unittest.main()
