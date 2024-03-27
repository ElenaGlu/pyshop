import unittest

from pyshop.game import get_score


class GetScoreTest(unittest.TestCase):

    def test_wrong_type_offset(self):
        response = get_score(
            [
                {
                    'offset': 99841,
                    'score':
                    {
                        'home': 2,
                        'away': 0
                    }
                },
                {
                    'offset': 99844,
                    'score':
                    {
                        'home': 2,
                        'away': 0
                    }
                }
            ],
            -6579
        )
        self.assertEqual(response, 'the wrong data type has been entered. enter a int')

    def test_offset_not_exist(self):
        response = get_score(
            [
                {
                    'offset': 99841,
                    'score':
                    {
                        'home': 2,
                        'away': 0
                    }
                },
                {
                    'offset': 99844,
                    'score':
                    {
                        'home': 2,
                        'away': 0
                    }
                }
            ],
            99845
        )
        self.assertEqual(response, 'the score does not exist at the requested time')

    def test_get_score_success(self):
        response = get_score(
            [
                {
                    'offset': 99841,
                    'score':
                    {
                        'home': 2,
                        'away': 0
                    }
                },
                {
                    'offset': 99844,
                    'score':
                    {
                        'home': 2,
                        'away': 0
                    }
                }
            ],
            99844
        )
        self.assertEqual(response, '2:0')


if __name__ == '__main__':
    unittest.main()
