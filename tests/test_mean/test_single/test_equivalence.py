# Copyright (C) 2024-present The Package Authors
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Validation Software: PASS 2025
# Module: One-Sample Z-Tests for Equivalence
#         One-Sample T-Tests for Equivalence


from dataclasses import dataclass
from typing import Literal

import pytest

from ezpwr.mean.single.equivalence import solve_power
from ezpwr.mean.single.equivalence import solve_size
from tests.models import BaseTestCase

pytestmark = pytest.mark.filterwarnings("ignore")


@dataclass(kw_only=True)
class TestCase(BaseTestCase):
    mean: float
    lower_equivalence_limit: float
    upper_equivalence_limit: float
    std: float
    size: int
    alpha: float
    dist: Literal["z", "t"] = "t"
    power: float
    actual_power: float


case_group_z = [
    # mean = -9.5 to 9.5 by 0.5, lower_equivalence_limit = -10, upper_equivalence_limit = 10, std = 8, alpha = 0.025, power = 0.80, dist = "z"
    TestCase(
        mean=mean,
        lower_equivalence_limit=-10,
        upper_equivalence_limit=10,
        std=8,
        size=size,
        alpha=0.025,
        dist="z",
        power=0.80,
        actual_power=actual_power,
    )
    for mean, size, actual_power in [
        (-9.50, 2010, 0.800134005679517),
        (-9.00, 503, 0.800523806680340),
        (-8.50, 224, 0.801301455458812),
        (-8.00, 126, 0.801301455458812),
        (-7.50, 81, 0.803041670796890),
        (-7.00, 56, 0.801301455458812),
        (-6.50, 42, 0.809310990820385),
        (-6.00, 32, 0.807429578798748),
        (-5.50, 25, 0.803041670796885),
        (-5.00, 21, 0.817040958812648),
        (-4.50, 17, 0.809123546747609),
        (-4.00, 14, 0.801299217214459),
        (-3.50, 12, 0.803567814115675),
        (-3.00, 11, 0.826622561233369),
        (-2.50, 10, 0.841036330104459),
        (-2.00, 9, 0.845296363071353),
        (-1.50, 8, 0.834437412172604),
        (-1.00, 8, 0.862291534324123),
        (-0.50, 7, 0.816177899835210),
        (0.00, 7, 0.822092271055409),
        (0.50, 7, 0.816177899835210),
        (1.00, 8, 0.862291534324123),
        (1.50, 8, 0.834437412172604),
        (2.00, 9, 0.845296363071353),
        (2.50, 10, 0.841036330104459),
        (3.00, 11, 0.826622561233369),
        (3.50, 12, 0.803567814115675),
        (4.00, 14, 0.801299217214459),
        (4.50, 17, 0.809123546747609),
        (5.00, 21, 0.817040958812648),
        (5.50, 25, 0.803041670796885),
        (6.00, 32, 0.807429578798748),
        (6.50, 42, 0.809310990820385),
        (7.00, 56, 0.801301455458812),
        (7.50, 81, 0.803041670796890),
        (8.00, 126, 0.801301455458812),
        (8.50, 224, 0.801301455458812),
        (9.00, 503, 0.800523806680340),
        (9.50, 2010, 0.800134005679517),
    ]
]


case_group_t = [
    # mean = -9.5 to 9.5 by 0.5, lower_equivalence_limit = -10, upper_equivalence_limit = 10, std = 8, alpha = 0.025, power = 0.80, dist = "t"
    TestCase(
        mean=mean,
        lower_equivalence_limit=-10,
        upper_equivalence_limit=10,
        std=8,
        size=size,
        alpha=0.025,
        dist="t",
        power=0.80,
        actual_power=actual_power,
    )
    for mean, size, actual_power in [
        (-9.50, 2010, 0.800089668260651),
        (-9.00, 505, 0.800582923591184),
        (-8.50, 226, 0.801426727494326),
        (-8.00, 128, 0.801506202583638),
        (-7.50, 83, 0.803324143309034),
        (-7.00, 58, 0.801649745803992),
        (-6.50, 43, 0.800318375311827),
        (-6.00, 34, 0.807776685514229),
        (-5.50, 27, 0.803291821334251),
        (-5.00, 23, 0.817106721378511),
        (-4.50, 19, 0.808870924402315),
        (-4.00, 16, 0.800552852733734),
        (-3.50, 14, 0.802195964728655),
        (-3.00, 13, 0.824693686495979),
        (-2.50, 12, 0.838317335968932),
        (-2.00, 11, 0.841272069167847),
        (-1.50, 10, 0.828190875959079),
        (-1.00, 10, 0.855666442606739),
        (-0.50, 9, 0.806446587306201),
        (0.00, 9, 0.812214829444349),
        (0.50, 9, 0.806446587306201),
        (1.00, 10, 0.855666442606739),
        (1.50, 10, 0.828190875959079),
        (2.00, 11, 0.841272069167847),
        (2.50, 12, 0.838317335968933),
        (3.00, 13, 0.824693686495979),
        (3.50, 14, 0.802195964728655),
        (4.00, 16, 0.800552852733733),
        (4.50, 19, 0.808870924402315),
        (5.00, 23, 0.817106721378511),
        (5.50, 27, 0.803291821334251),
        (6.00, 34, 0.807776685514229),
        (6.50, 43, 0.800318375311827),
        (7.00, 58, 0.801649745803993),
        (7.50, 83, 0.803324143309034),
        (8.00, 128, 0.801506202583638),
        (8.50, 226, 0.801426727494326),
        (9.00, 505, 0.800582923591184),
        (9.50, 2010, 0.800089668260651),
    ]
]

case_group = case_group_z + case_group_t


def test_solve_power(case: TestCase, request: pytest.FixtureRequest) -> None:

    if case.mean in [-9.5, 9.5] and case.dist == "t":
        request.node.add_marker(
            pytest.mark.xfail(reason="Owen's Q function is not implemented, so the result differs from PASS.")
        )

    assert round(
        solve_power(
            mean=case.mean,
            lower_equivalence_limit=case.lower_equivalence_limit,
            upper_equivalence_limit=case.upper_equivalence_limit,
            std=case.std,
            size=case.size,
            alpha=case.alpha,
            dist=case.dist,
        ),
        6,
    ) == round(case.actual_power, 6)


def test_solve_size(case: TestCase, request: pytest.FixtureRequest) -> None:

    if case.mean in [-9.5, -9.0, -2.0, 1.5, 6.0, 9.5] and case.dist == "t":
        request.node.add_marker(
            pytest.mark.xfail(reason="Owen's Q function is not implemented, so the result differs from PASS.")
        )

    assert (
        solve_size(
            mean=case.mean,
            lower_equivalence_limit=case.lower_equivalence_limit,
            upper_equivalence_limit=case.upper_equivalence_limit,
            std=case.std,
            alpha=case.alpha,
            power=case.power,
            dist=case.dist,
        )
        == case.size
    )
