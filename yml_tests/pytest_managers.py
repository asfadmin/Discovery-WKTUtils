
from test_repairWKT import test_repairWKT_manager
from test_filesToWKT import test_filesToWKT_manager

def test_repairWKT(test_info, file_conf, cli_args, test_vars):
    test_repairWKT_manager(test_info, file_conf, cli_args, test_vars)

def test_filesToWKT(test_info, file_conf, cli_args, test_vars):
    test_filesToWKT_manager(test_info, file_conf, cli_args, test_vars)

