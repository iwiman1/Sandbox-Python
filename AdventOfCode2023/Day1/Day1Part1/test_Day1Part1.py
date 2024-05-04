import Day1Part1
import unittest

class Day1Tests(unittest.TestCase):
    def test_fullSample(self):
        self.assertEqual(Day1Part1.day1Part1Main("F:\Dev\Sandbox-Python\AdventOfCode2023\Day1\Day1Part1\Inputs\FullSample.txt"), 52974)

    def test_smallSample(self):
        self.assertEqual(Day1Part1.day1Part1Main("F:\Dev\Sandbox-Python\AdventOfCode2023\Day1\Day1Part1\Inputs\SmallSample.txt"), 142)

if __name__ == "__main__":
    unittest.main()