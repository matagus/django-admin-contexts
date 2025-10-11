# django-admin-contexts

![Python Compatibility](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue.svg)
![Django Compatibility](https://img.shields.io/badge/django-4.2%20|%205.0%20|%205.1%20|%205.2-%2344B78B?labelColor=%23092E20)
[![PyPi Version](https://img.shields.io/pypi/v/django-admin-contexts.svg)](https://pypi.python.org/pypi/django-admin-contexts)
![CI badge](https://github.com/matagus/django-admin-contexts/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/matagus/django-admin-contexts/graph/badge.svg?token=a64SxEDQk0)](https://codecov.io/gh/matagus/django-admin-contexts)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Display only a set of apps and models in the Django Admin homepage, based on the chosen context. This is useful when
you have a lot of apps and models and you want to focus on a specific set of them.

![Demo: selecting a context to display only a subset of models](https://raw.githubusercontent.com/matagus/django-admin-contexts/main/screenshots/demo.gif)


Installation
============

Via `pip` command:

```bash
pip install django-admin-contexts
```

...or you can clone the repo and install it using `pip` too:

```bash
git clone git://github.com/matagus/django-admin-contexts.git
cd django-admin-contexts
pip install -e .
```

then add `django_admin_contexts` to your `settings.py` **before** `django.contrib.admin`:

```python
INSTALLED_APPS = (
    # ...
    "django_admin_contexts",
    # ...
    "django.contrib.admin",
    # ...
)
```

then run the migrations:

```bash
python manage.py migrate
```

Usage
=====

Browse to the Django Admin and create some contexts in the "Django Admin Contexts" section, associating them with one
or more models.

Then, you can see the contexts in the Django Admin homepage.


Running Tests
=============

**Prerequisites:** Install Hatch if not already installed: `pip install hatch`

**List available test environments:**
```bash
hatch env show test
```

**Run all tests (all Python + Django combinations):**
```bash
hatch run test:test
```

**Run tests for specific Python/Django version:**
```bash
hatch run test.py3.14-5.2:test  # Python 3.14 + Django 5.2
hatch run test.py3.12-5.1:test  # Python 3.12 + Django 5.1
```

**Run specific test file:**
```bash
hatch run test.py3.12-5.2:test tests.test_models
```

**Coverage:**
```bash
hatch run test:cov  # Run tests with coverage report
```

**Troubleshooting:** If you encounter environment issues, clean and rebuild: `hatch env prune`


Contributing
============

Contributions are welcome! ❤️

Please read [Contributing.md](CONTRIBUTING.md) for detailed instructions on how to help.

License
=======

`django-admin-contexts` is released under a BSD License


Acknowledgements
================

Develop & built using [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch) [![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
