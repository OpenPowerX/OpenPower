# Ezpwr

[![PyPI - Version](https://img.shields.io/pypi/v/ezpwr)](https://badge.fury.io/py/ezpwr)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ezpwr)
![GitHub License](https://img.shields.io/github/license/Snoopy1866/ezpwr)
![PyPI - Status](https://img.shields.io/pypi/status/ezpwr)
[![PyPI Downloads](https://static.pepy.tech/badge/ezpwr)](https://pepy.tech/projects/ezpwr)

[![Build Status](https://img.shields.io/github/actions/workflow/status/Snoopy1866/ezpwr/release.yml)](https://github.com/Snoopy1866/ezpwr/actions/workflows/release.yml?query=branch:main)
[![Test Status](https://img.shields.io/github/actions/workflow/status/Snoopy1866/ezpwr/pytest.yml?branch=main&label=test)](https://github.com/Snoopy1866/ezpwr/actions/workflows/pytest.yml?query=branch:main)
[![Documentation Status](https://readthedocs.org/projects/ezpwr/badge/?version=latest)](https://ezpwr.readthedocs.io/zh-cn/latest/?badge=latest)
[![codecov](https://codecov.io/gh/Snoopy1866/ezpwr/graph/badge.svg?token=P9UWC8Q4P6)](https://codecov.io/gh/Snoopy1866/ezpwr)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Snoopy1866/ezpwr/main.svg)](https://results.pre-commit.ci/latest/github/Snoopy1866/ezpwr/main)

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pytest](https://img.shields.io/badge/logo-pytest-blue?logo=pytest&labelColor=5c5c5c&label=%20)](https://github.com/pytest-dev/pytest)

Ezpwr is a Python package for statistical power analysis that allows users to estimate sample size, test power, and effect size.

[简体中文](README-zh.md) | English

> 🗺️ **Feature List & Roadmap**: To see currently supported statistical models and planned features, check out [roadmap](docs/roadmap.md).

## 📦 Installation

**Prerequisites**: Python 3.10+

```bash
pip install ezpwr
```

## 🚀 Usage Examples

### Sample Size Estimation

- Single Proportion Confidence Interval

  ```python
  from ezpwr import proportion

  size = proportion.single.ci.solve_size(
      proportion=0.9,
      distance=0.10,
      conf_level=0.95,
      interval_type="two-sided",
  )
  print(size)

  # output: 158
  ```

- Single Proportion Inequality Test

  ```python
  from ezpwr import proportion

  size = proportion.single.inequality.solve_size(
      null_proportion=0.80,
      proportion=0.95,
      alternative="greater",
      alpha=0.025,
      power=0.8,
  )
  print(size)

  # output: 41
  ```

- Two Independent Proportions Non-Inferiority Test

  ```python
  from ezpwr import proportion

  size = proportion.independent.noninferiority.solve_size(
      treatment_proportion=0.95,
      reference_proportion=0.90,
      margin=-0.10,
      alternative="greater",
      ratio=1,
      alpha=0.025,
      power=0.8,
  )
  print(size)

  # output: (48, 48)
  ```

- Two Independent Means Superiority Test

  ```python
  from ezpwr import mean

  size = mean.independent.superiority.solve_size(
      diff=0.5,
      margin=0.1,
      alternative="greater",
      treatment_std=1.2,
      reference_std=1.2,
      ratio=2,
      alpha=0.025,
      power=0.8,
  )
  print(size)

  # output: (214, 107)
  ```

### Statistical Power Calculation

```python
from ezpwr import proportion

power = proportion.independent.noninferiority.solve_power(
    treatment_proportion=0.95,
    reference_proportion=0.90,
    margin=-0.10,
    alternative="greater",
    treatment_size=48,
    reference_size=48,
    alpha=0.025,
)
print(power)

# output: 0.8002829157189179
```

### Effect Size Solving

```python
from ezpwr import proportion

treatment_proportion = proportion.independent.noninferiority.solve_treatment_proportion(
    reference_proportion=0.90,
    margin=-0.10,
    alternative="greater",
    treatment_size=48,
    reference_size=48,
    alpha=0.025,
    power=0.8,
)
print(treatment_proportion)

# output: 0.9499637015276099
```

## 🧪 Compatibility Matrix

[![Test Status](https://img.shields.io/github/actions/workflow/status/Snoopy1866/ezpwr/pytest_full.yml?branch=main&label=test)](https://github.com/Snoopy1866/ezpwr/actions/workflows/pytest_full.yml?query=branch:main)

|            | 🐍 3.10 | 🐍 3.11 | 🐍 3.12 | 🐍 3.13 | 🐍 3.14 |
| ---------- | ------- | ------- | ------- | ------- | ------- |
| SciPy 1.7  | ✅      | -       | -       | -       | -       |
| SciPy 1.8  | ✅      | -       | -       | -       | -       |
| SciPy 1.9  | ✅      | -       | -       | -       | -       |
| SciPy 1.10 | ✅      | ✅      | -       | -       | -       |
| SciPy 1.11 | ✅      | ✅      | ✅      | -       | -       |
| SciPy 1.12 | ✅      | ✅      | ✅      | -       | -       |
| SciPy 1.13 | ✅      | ✅      | ✅      | -       | -       |
| SciPy 1.14 | ✅      | ✅      | ✅      | -       | -       |
| SciPy 1.15 | ✅      | ✅      | ✅      | ✅      | -       |
| SciPy 1.16 | -       | ✅      | ✅      | ✅      | ✅      |
| SciPy 1.17 | -       | ✅      | ✅      | ✅      | ✅      |
| SciPy 1.18 | -       | -       | ✅      | ✅      | ✅      |

> [!NOTE]
>
> `-` : This combination of Python and SciPy does not exist.

## ✨ Contributing

Issues and pull requests are welcome and highly appreciated. To get started, check out the [contributing guidelines](CONTRIBUTING.md).

## 🤝 Acknowledgments

- [scipy](https://github.com/scipy/scipy)
- [pingouin](https://github.com/raphaelvallat/pingouin)
