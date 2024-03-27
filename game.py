import random
import math
from typing import List, Union

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
                             PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)
    return stamps


def get_score(game_stamps: List[dict[str, Union[int, dict[str, int]]]], offset: int) -> str:
    if isinstance(offset, int) and offset > 0:
        score = next(
                (f"{item['score']['home']}:{item['score']['away']}" for item in game_stamps if item['offset'] == offset
                 if not check_offset(item['offset'], offset)), None)
        if score:
            return score
        else:
            return 'the score does not exist at the requested time'
    else:
        return 'the wrong data type has been entered. enter a int'


def check_offset(iterable_offset, default_offset):
    if iterable_offset > default_offset:
        raise StopIteration()
