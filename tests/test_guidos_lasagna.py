from scripts.guidos_lasagna import *


def test_expected_baske_time_constant_returns_40():
    lasagna = Lasagna()
    assert lasagna.EXPECTED_BAKE_TIME == 40
