import Day2Part1
import unittest

class Day2Tests(unittest.TestCase):
    def test_fullSample(self):
        self.assertEqual(Day2Part1.day2Part1Main("F:\Dev\Sandbox-Python\AdventOfCode2023\Day2\Part1\Inputs\FullSample.txt"), 2551)

    def test_smallSample(self):
        self.assertEqual(Day2Part1.day2Part1Main("F:\Dev\Sandbox-Python\AdventOfCode2023\Day2\Part1\Inputs\SmallSample.txt"), 7)

if __name__ == "__main__":
    unittest.main()