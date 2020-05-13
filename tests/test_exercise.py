import pytest
import os

def test_exercise():
    os.chdir('src')

    from health_station import HealthStation
    from person import Person
    station = HealthStation()

    james = Person("James", 1, 108, 8)
    grace = Person("Grace", 33, 172, 80)

    assert station.weigh(james) == 8
    assert station.weigh(grace) == 80

    station.feed(grace)

    assert station.weigh(grace) == 81

    assert station.weighings() == 3
