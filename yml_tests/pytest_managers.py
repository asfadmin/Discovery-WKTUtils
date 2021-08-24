import os
import sys

# Add the package to pythonpath before import:
root_dir = os.path.abspath(os.path.join(__file__,"..",".."))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from test_repairWKT import test_repairWKT_manager
from test_filesToWKT import test_filesToWKT_manager
from test_validateWKT import test_validateWKT_manager

def test_repairWKT(**args):
    test_repairWKT_manager(**args)

def test_filesToWKT(**args):
    test_filesToWKT_manager(**args)

def test_validateWKT(**args):
    test_validateWKT_manager(**args)

