import os
import unittest

class TestChallenge(unittest.TestCase):
    def setUp(self):
        self.training_accident_count = len([name for name in os.listdir("dataset/training/accident")])
        self.training_non_accident_count = len([name for name in os.listdir("dataset/training/non-accident")])

        self.validation_accident_count = len([name for name in os.listdir("dataset/validation/accident")])
        self.validation_non_accident_count = len([name for name in os.listdir("dataset/validation/non-accident")])

        self.testing_accident_count = len([name for name in os.listdir("dataset/testing/accident")])
        self.testing_non_accident_count = len([name for name in os.listdir("dataset/testing/non-accident")])

    def test_training_set(self):
        self.assertAlmostEqual(self.training_accident_count, 1679, delta=5)
        self.assertEqual(self.training_non_accident_count, 1750)
        
    def test_validation_set(self):
        self.assertAlmostEqual(self.validation_accident_count, 240, delta=5)
        self.assertEqual(self.validation_non_accident_count, 250)

    def test_testing_set(self):
        self.assertAlmostEqual(self.testing_accident_count, 480, delta=5)
        self.assertEqual(self.testing_non_accident_count, 500)

if __name__ == '__main__':
    unittest.main()