import unittest
from HtmlTestRunner import HTMLTestRunner

class OurTestCase(unittest.TestCase):
    def test_1(self):
        res = 2 + 2
        self.assertEqual(res, 4)

    def test_2(self):
        res = 2 + 1
        self.assertEqual(res, 4)


# test1 = OurTestCase("test_1")
# # result1 = test1.run()
# # print(result1)
#
# test2 = OurTestCase("test_2")
# # result2 = test2.run()
# # print(result2)
#
# test_suite = unittest.TestSuite([test1, test2])
test_suite = unittest.TestLoader().loadTestsFromTestCase(OurTestCase)
# test_suite.addTest(test1)

result = unittest.TestResult()


test_suite.run(result)
print(result)
