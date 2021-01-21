.. include:: ../_resources.rst

.. _setup-python-package:

####################################
Setup using Python package from PyPI
####################################


*****
Intro
*****
Kotori can be installed in different variants.

Setting up Kotori as Python package is suitable for general
:ref:`kotori-hacking` or for installing on platforms where
there's no native distribution package available yet.

Python Eggs can be installed into virtualenvs and into the
system, both in editable and non-editable modes.


*********
Get ready
*********

Prerequisites
=============
::

    # Prepare system
    apt install build-essential libffi-dev libssl-dev python-dev python-pip python-virtualenv


.. _setup-python-virtualenv:

virtualenv
==========
We definitively recommend to install Kotori inside
a Python virtualenv in order to isolate the installation
from the local Python environment on your machine to
protect against dependency woes.

Your installation will not require root permissions and
the Python libraries of your system distribution will stay
completely untouched.

See next section for how to setup a Python *virtulenv* environment.
See also :ref:`kotori-hacking` for getting hold of the git repository
when installing from source.
::

    # Create virtualenv
    make setup-virtualenv

    # Activate virtualenv
    source .venv/bin/activate


*****
Setup
*****

Install from package repository
===============================

Install Kotori::

    # Install latest Kotori release with extra feature "daq"
    pip install kotori[daq]

    # Install more extra features
    pip install kotori[daq,daq_geospatial,export,plotting,scientific]

    # Install particular version
    pip install kotori[daq,export]==0.15.0


Install directly from git repository
====================================
::

    pip install --editable git+https://github.com/daq-tools/kotori.git#egg=kotori[daq]

.. seealso:: https://pip.pypa.io/en/stable/reference/pip_install/#examples
