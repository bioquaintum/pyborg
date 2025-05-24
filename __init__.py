# pybrainorg/__init__.py

"""
pybrainorg: A Python Brain Organoid Simulator using Brian2.

This package provides tools to model, simulate, and analyze brain organoids.
It allows users to define neuronal populations, synaptic connections, spatial
arrangements, and simulate their activity using the Brian2 engine. Features
include MEA interaction, calcium imaging simulation, network plasticity,
and data analysis tools.
"""

# Define the package version
# This should match the version in your setup.py
__version__ = "0.1.0"

# --- Import key classes and functions for top-level access ---
# This allows users to import them directly from the 'pybrainorg' package.
# Example: from pybrainorg import Organoid, Simulator

# From the organoid module
from .organoid.organoid import Organoid
# Users will access spatial functions via: from pybrainorg.organoid import spatial

# From the simulation module
from .simulation.simulator import Simulator

# From the mea module
from .mea.mea import MEA

# (Optional) Define __all__ to control what 'from pybrainorg import *' imports.
# Using 'import *' is generally discouraged in production code for clarity.
# If you choose to define it, it would look something like this:
# __all__ = [
#     "Organoid",
#     "Simulator",
#     "MEA",
#     "__version__",
#     # Add other names intended for 'import *'
# ]

# You could also expose some core model functions or spatial functions here if desired,
# but it's often cleaner to keep them namespaced, e.g.:
# from pybrainorg.core import neuron_models
# from pybrainorg.organoid import spatial

# Minimal initialization, if any, should go here.
# Avoid print statements or heavy computation in __init__.py for libraries.