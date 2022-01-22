from scripts.guidos_lasagna import *


def test_expected_baske_time_constant_returns_40():
    lasagna = Lasagna()
    assert lasagna.EXPECTED_BAKE_TIME == 40


def test_bake_time_remaining_returs_10():
    l = Lasagna()
    assert l.bake_time_remaining(30) == 10


def test_preparation_time_in_minutes_returns_4():
    l = Lasagna()
    assert l.preparation_time_in_minutes(2) == 4
