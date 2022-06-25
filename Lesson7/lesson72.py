import  unittest


class OurTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nSet up Class of", cls)
        print(type(cls))

    def setUp(self):
        print("\nSet up Class of", self)
        print(type(self))