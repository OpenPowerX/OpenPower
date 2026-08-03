# Copyright (C) 2024-present The Package Authors
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Validation Software: PASS 2025 (Partially)
# Module: Two-Sample T-Tests for Equivalence Assuming Equal Variance
#         Two-Sample T-Tests for Equivalence Assuming Unequal Variance

from dataclasses import dataclass
from typing import Literal

import pytest

from ezpwr.mean.independent._verify import _verify_mean_and_get_diff
from ezpwr.mean.independent._verify import _verify_std_and_get_std
from ezpwr.mean.independent.equivalence import solve_power
from tests.models import BaseTestCase


@dataclass(kw_only=True)
class TestCase(BaseTestCase):
    treatment_mean: float | None = None
    reference_mean: float | None = None
    diff: float | None = None
    lower_margin: float
    upper_margin: float
    treatment_std: float | None = None
    reference_std: float | None = None
    std: float | None = None
    treatment_size: int
    reference_size: int
    alpha: float
    power: float
    actual_power: float
    dist: Literal["z", "t"]
    equal_var: bool
    approx_t_method: Literal["welch", "satterthwaite"] = "welch"

    def __post_init__(self) -> None:
        self.diff = _verify_mean_and_get_diff(self.treatment_mean, self.reference_mean, self.diff)
        self.std = _verify_std_and_get_std(self.treatment_std, self.reference_std, self.std, self.dist, self.equal_var)


case_group_z_equal_var = []

case_group_z_unequal_var = []

case_group_t_equal_var = [
    # diff = -9.5 to 9.5 by 0.5, lower_margin = -10, upper_margin = 10, std = 10, ratio = 2, alpha = 0.025, power = 0.80, dist = "t", equal_var = True
    TestCase(
        diff=diff,
        lower_margin=lower_margin,
        upper_margin=upper_margin,
        treatment_std=std,
        reference_std=std,
        treatment_size=treatment_size,
        reference_size=reference_size,
        alpha=0.025,
        power=0.80,
        actual_power=actual_power,
        dist="t",
        equal_var=True,
    )
    for diff, lower_margin, upper_margin, std, treatment_size, reference_size, actual_power in [
        (-9.50, -10, 10, 8, 6029, 3015, 0.800102468512394),
        (-9.00, -10, 10, 8, 1507, 754, 0.800137860801582),
        (-8.50, -10, 10, 8, 670, 335, 0.800045321053730),
        (-8.00, -10, 10, 8, 379, 190, 0.801694689262935),
        (-7.50, -10, 10, 8, 243, 122, 0.802039202564133),
        (-7.00, -10, 10, 8, 169, 85, 0.802168024442070),
        (-6.50, -10, 10, 8, 125, 63, 0.804260493647850),
        (-6.00, -10, 10, 8, 95, 48, 0.800730526546903),
        (-5.50, -10, 10, 8, 76, 38, 0.801465819333665),
        (-5.00, -10, 10, 8, 61, 31, 0.800451468943072),
        (-4.50, -10, 10, 8, 51, 26, 0.804086443160867),
        (-4.00, -10, 10, 8, 43, 22, 0.804380694541997),
        (-3.50, -10, 10, 8, 37, 19, 0.807054388993506),
        (-3.00, -10, 10, 8, 33, 17, 0.818703561367751),
        (-2.50, -10, 10, 8, 29, 15, 0.818881261302614),
        (-2.00, -10, 10, 8, 25, 13, 0.801586212163072),
        (-1.50, -10, 10, 8, 23, 12, 0.800135872244968),
        (-1.00, -10, 10, 8, 23, 12, 0.828646387332903),
        (-0.50, -10, 10, 8, 22, 11, 0.806752485991713),
        (0.00, -10, 10, 8, 21, 11, 0.802672612476682),
        (0.50, -10, 10, 8, 22, 11, 0.806752485991713),
        (1.00, -10, 10, 8, 23, 12, 0.828646387332903),
        (1.50, -10, 10, 8, 23, 12, 0.800135872244968),
        (2.00, -10, 10, 8, 25, 13, 0.801586212163072),
        (2.50, -10, 10, 8, 29, 15, 0.818881261302614),
        (3.00, -10, 10, 8, 33, 17, 0.818703561367751),
        (3.50, -10, 10, 8, 37, 19, 0.807054388993506),
        (4.00, -10, 10, 8, 43, 22, 0.804380694541998),
        (4.50, -10, 10, 8, 51, 26, 0.804086443160867),
        (5.00, -10, 10, 8, 61, 31, 0.800451468943072),
        (5.50, -10, 10, 8, 76, 38, 0.801465819333665),
        (6.00, -10, 10, 8, 95, 48, 0.800730526546903),
        (6.50, -10, 10, 8, 125, 63, 0.804260493647850),
        (7.00, -10, 10, 8, 169, 85, 0.802168024442070),
        (7.50, -10, 10, 8, 243, 122, 0.802039202564133),
        (8.00, -10, 10, 8, 379, 190, 0.801694689262935),
        (8.50, -10, 10, 8, 670, 335, 0.800045321053730),
        (9.00, -10, 10, 8, 1507, 754, 0.800137860801582),
        (9.50, -10, 10, 8, 6029, 3015, 0.800102468512394),
    ]
]

# The non-inferior module of pass 15 does not support Welch's approx t-test. The test cases here are verified by AI.
case_group_t_unequal_var_welch = []

case_group_t_unequal_var_satterthwaite = [
    # diff = -9.5 to 9.5 by 0.5, lower_margin = -10, upper_margin = 10, treatment_std = 12, reference_std = 8, ratio = 2, alpha = 0.025, power = 0.80, dist = "t", equal_var = False, approx_t_method = "satterthwaite"
    TestCase(
        diff=diff,
        lower_margin=lower_margin,
        upper_margin=upper_margin,
        treatment_std=treatment_std,
        reference_std=reference_std,
        treatment_size=treatment_size,
        reference_size=reference_size,
        alpha=0.025,
        power=0.80,
        actual_power=actual_power,
        dist="t",
        equal_var=False,
        approx_t_method="satterthwaite",
    )
    for diff, lower_margin, upper_margin, treatment_std, reference_std, treatment_size, reference_size, actual_power in [
        (-9.50, -10, 10, 12, 8, 8540, 4270, 0.800004016596936),
        (-9.00, -10, 10, 12, 8, 2135, 1068, 0.800097189503495),
        (-8.50, -10, 10, 12, 8, 949, 475, 0.800246262272983),
        (-8.00, -10, 10, 12, 8, 535, 268, 0.801081605749021),
        (-7.50, -10, 10, 12, 8, 343, 172, 0.800738588032575),
        (-7.00, -10, 10, 12, 8, 239, 120, 0.801829354023686),
        (-6.50, -10, 10, 12, 8, 176, 88, 0.800878338473901),
        (-6.00, -10, 10, 12, 8, 135, 68, 0.802863835025869),
        (-5.50, -10, 10, 12, 8, 107, 54, 0.802283774643174),
        (-5.00, -10, 10, 12, 8, 87, 44, 0.803723659501946),
        (-4.50, -10, 10, 12, 8, 72, 36, 0.800953926412636),
        (-4.00, -10, 10, 12, 8, 61, 31, 0.806026359623751),
        (-3.50, -10, 10, 12, 8, 52, 26, 0.802890214892888),
        (-3.00, -10, 10, 12, 8, 45, 23, 0.804642649255705),
        (-2.50, -10, 10, 12, 8, 40, 20, 0.803499987468328),
        (-2.00, -10, 10, 12, 8, 36, 18, 0.806627960371765),
        (-1.50, -10, 10, 12, 8, 33, 17, 0.804454488710486),
        (-1.00, -10, 10, 12, 8, 31, 16, 0.809956812471172),
        (-0.50, -10, 10, 12, 8, 31, 16, 0.827278363298312),
        (0.00, -10, 10, 12, 8, 30, 15, 0.801177400393972),
        (0.50, -10, 10, 12, 8, 31, 16, 0.827278363298311),
        (1.00, -10, 10, 12, 8, 31, 16, 0.809956812471172),
        (1.50, -10, 10, 12, 8, 33, 17, 0.804454488710486),
        (2.00, -10, 10, 12, 8, 36, 18, 0.806627960371765),
        (2.50, -10, 10, 12, 8, 40, 20, 0.803499987468327),
        (3.00, -10, 10, 12, 8, 45, 23, 0.804642649255705),
        (3.50, -10, 10, 12, 8, 52, 26, 0.802890214892888),
        (4.00, -10, 10, 12, 8, 61, 31, 0.806026359623751),
        (4.50, -10, 10, 12, 8, 72, 36, 0.800953926412636),
        (5.00, -10, 10, 12, 8, 87, 44, 0.803723659501946),
        (5.50, -10, 10, 12, 8, 107, 54, 0.802283774643174),
        (6.00, -10, 10, 12, 8, 135, 68, 0.802863835025869),
        (6.50, -10, 10, 12, 8, 176, 88, 0.800878338473901),
        (7.00, -10, 10, 12, 8, 239, 120, 0.801829354023686),
        (7.50, -10, 10, 12, 8, 343, 172, 0.800738588032575),
        (8.00, -10, 10, 12, 8, 535, 268, 0.801081605749021),
        (8.50, -10, 10, 12, 8, 949, 475, 0.800246262272983),
        (9.00, -10, 10, 12, 8, 2135, 1068, 0.800097189503495),
        (9.50, -10, 10, 12, 8, 8540, 4270, 0.800004016596936),
    ]
]


case_group = (
    case_group_z_equal_var
    + case_group_z_unequal_var
    + case_group_t_equal_var
    + case_group_t_unequal_var_welch
    + case_group_t_unequal_var_satterthwaite
)


def test_solve_power(case: TestCase, request: pytest.FixtureRequest) -> None:

    if case.diff in [-9.5, -9.0, -8.5, 8.5, 9.0, 9.5] and case.dist == "t" and case.equal_var:
        request.node.add_marker(pytest.mark.xfail(reason="The algorithm of PASS 2025 is unknown."))

    if case.dist == "t" and not case.equal_var and case.approx_t_method == "satterthwaite":
        request.node.add_marker(pytest.mark.xfail(reason="The algorithm of PASS 2025 is unknown."))

    assert round(
        solve_power(
            treatment_mean=case.treatment_mean,
            reference_mean=case.reference_mean,
            diff=case.diff,
            lower_margin=case.lower_margin,
            upper_margin=case.upper_margin,
            treatment_std=case.treatment_std,
            reference_std=case.reference_std,
            std=case.std,
            treatment_size=case.treatment_size,
            reference_size=case.reference_size,
            alpha=case.alpha,
            dist=case.dist,
            equal_var=case.equal_var,
            approx_t_method=case.approx_t_method,
        ),
        6,
    ) == round(case.actual_power, 6)


# def test_solve_size(case: TestCase, request: pytest.FixtureRequest) -> None:

#     ratio = case.treatment_size / case.reference_size
#     assert solve_size(
#         treatment_mean=case.treatment_mean,
#         reference_mean=case.reference_mean,
#         diff=case.diff,
#         lower_margin=case.lower_margin,
#         upper_margin=case.upper_margin,
#         treatment_std=case.treatment_std,
#         reference_std=case.reference_std,
#         std=case.std,
#         ratio=ratio,
#         alpha=case.alpha,
#         power=case.power,
#         dist=case.dist,
#         equal_var=case.equal_var,
#         approx_t_method=case.approx_t_method,
#     ) == (case.treatment_size, case.reference_size)
