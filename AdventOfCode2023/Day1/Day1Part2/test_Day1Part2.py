import Day1Part2
import unittest

class Day1Tests(unittest.TestCase):
    def test_fullSample(self):
        self.assertEqual(Day1Part2.day1Part2Main("F:\Dev\Sandbox-Python\AdventOfCode2023\Day1\Day1Part2\Inputs\FullSample.txt"), 53340)

    def test_smallSample(self):
        self.assertEqual(Day1Part2.day1Part2Main("F:\Dev\Sandbox-Python\AdventOfCode2023\Day1\Day1Part2\Inputs\SmallSample.txt"), 281)

if __name__ == "__main__":
    unittest.main()