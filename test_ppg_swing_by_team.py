import unittest
import ppg_swing_by_team as ppg

class TestPpg(unittest.TestCase):

    def test_point_swings(self):
        self.assertEqual(len(ppg.point_swings()), 20)
        self.assertIsNotNone(ppg.point_swings()[0][1])
        self.assertIsNotNone(ppg.point_swings()[1][1])
        self.assertIsNotNone(ppg.point_swings()[2][1])
        self.assertIsNotNone(ppg.point_swings()[3][1])
        self.assertIsNotNone(ppg.point_swings()[4][1])
        self.assertIsNotNone(ppg.point_swings()[5][1])
        self.assertIsNotNone(ppg.point_swings()[6][1])
        self.assertIsNotNone(ppg.point_swings()[7][1])
        self.assertIsNotNone(ppg.point_swings()[8][1])
        self.assertIsNotNone(ppg.point_swings()[9][1])
        self.assertIsNotNone(ppg.point_swings()[10][1])
        self.assertIsNotNone(ppg.point_swings()[11][1])
        self.assertIsNotNone(ppg.point_swings()[12][1])
        self.assertIsNotNone(ppg.point_swings()[13][1])
        self.assertIsNotNone(ppg.point_swings()[14][1])
        self.assertIsNotNone(ppg.point_swings()[15][1])
        self.assertIsNotNone(ppg.point_swings()[16][1])
        self.assertIsNotNone(ppg.point_swings()[17][1])
        self.assertIsNotNone(ppg.point_swings()[18][1])
        self.assertIsNotNone(ppg.point_swings()[19][1])



if __name__ == '__main__':
    unittest.main()
