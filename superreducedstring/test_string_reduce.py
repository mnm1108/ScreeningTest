import unittest
import superreducedstring as sr

class TestStringReduce(unittest.TestCase):
    def test_1(self):
        self.assertEqual('abd', sr.super_reduced_string('aaabbbddd'))
        self.assertNotEqual('fghr',sr.super_reduced_string('ffgggghhhr'))
        self.assertEqual('Empty String', sr.super_reduced_string('nnmm'))
        self.assertNotEqual('ab', sr.super_reduced_string('aabb'))
        self.assertEqual('m', sr.super_reduced_string('m'))

if __name__ == "__main__":
    unittest.main()
