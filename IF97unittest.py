import unittest
import IF97


class First_test(unittest.TestCase):

    def setUp(self):
        self.data1 = [[3, 300, 0.0010021516796866943, 115.3312730214384, 112.32481798237833, 0.39229479240262427, 4.173012184067783, 1507.7392096690312],
                      [80, 300, 0.0009711808940216297, 184.14282773425438, 106.44835621252402,
                       0.36856385239848066, 4.010089869646331, 1634.6905431116586],
                      [3, 500, 0.001202418003378339, 975.5422390972251, 971.9349850870901, 2.58041912005181, 4.6558068221112086, 1240.7133731017252]]

    def test_Volume(self):
        for item in self.data1:
            self.assertAlmostEqual(IF97.Volume(item[0], item[1]), item[2])

    def test_Enthalpy(self):
        for item in self.data1:
            self.assertAlmostEqual(IF97.Enthalpy(item[0], item[1]), item[3])

    def test_InternalEnergy(self):
        for item in self.data1:
            self.assertAlmostEqual(IF97.InternalEnergy(item[0], item[1]), item[4])

    def test_Entropy(self):
        for item in self.data1:
            self.assertEqual(IF97.Entropy(item[0], item[1]), item[5])

    def test_IHCapacity(self):
        for item in self.data1:
            self.assertEqual(IF97.IHCapacity(item[0], item[1]), item[6])

    def test_Sound(self):
        for item in self.data1:
            self.assertEqual(IF97.Sound(item[0], item[1]), item[7])


class Second_test(unittest.TestCase):

    def setUp(self):
        self.data2 = [[50, 2000, 690.5721252159439],
                      [100, 2100, 733.9305075450569]]
        self.data3 = [[50, 2400, 735.1848617922307],
                      [100, 2700, 842.046087633262]]

    def test_Buchong_BE3a(self):
        for item in self.data2:
            self.assertEqual(IF97.Buchong_BE3a(item[0], item[1]), item[2])

    def test_Buchong_BE3b(self):
        for item in self.data3:
            self.assertEqual(IF97.buchong_BE3b(item[0], item[1]), item[2])


def suitetext():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(First_test))
    suite.addTest(unittest.makeSuite(Second_test))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suitetext')
