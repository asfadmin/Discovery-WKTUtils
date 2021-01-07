import os, sys              # Generic imports
import geomet.wkt           # For comparing wkt's
import shapely

# Add the package to pythonpath before import:
root_dir = os.path.abspath(os.path.join(".."))
if root_dir not in sys.path:
    sys.path.append(root_dir)
from WKTUtils.FilesToWKT import filesToWKT

class test_filesToWKT_manager():
    def __init__(self, test_info, file_conf, cli_args, test_vars):
        # I replace '{0}' with itself, so that you can format that in later, and everything else is populated already:
        self.error_msg = "Reason: {0}\n - File: '{1}'\n - Test: '{2}'".format('{0}', file_conf["yml name"], test_info["title"])
        
        test_info = self.applyDefaultValues(test_info)
        wkt_json = filesToWKT(test_info["file wkt"]).getWKT()

        if test_info["print"] == True:
            print()
            print("Title: " + str(test_info["title"]))
            print("  -- Function returned:\n{0}".format(wkt_json))
            print()
            
        # Make sure the response matches what is expected from the test:
        self.runAssertTests(test_info, wkt_json)

    def applyDefaultValues(self, test_info):
        # Figure out what test is 'expected' to do:
        pass_assertions = ["parsed wkt"]
        fail_assertions = ["errors"]
        # True if at least one of the above is in the test, False otherwise:
        pass_assertions_used = len([k for (k, _) in test_info.items() if k in pass_assertions]) != 0
        fail_assertions_used = len([k for (k, _) in test_info.items() if k in fail_assertions]) != 0
        assertions_used = (pass_assertions_used or fail_assertions_used)

        # Default Print the result to screen if tester isn't asserting anything. Else just run the test:
        if "print" not in test_info:
            test_info["print"] = not assertions_used

        if not isinstance(test_info["file wkt"], type([])):
            test_info["file wkt"] = [test_info["file wkt"]]

        # If you should check errors. (Will check if you assert something will happen. Checks empty case by default then.)
        if "check errors" not in test_info:
            test_info["check errors"] = assertions_used
        # Setup errors:
        if "errors" not in test_info:
            test_info["errors"] = []
        if not isinstance(test_info["errors"], type([])):
            test_info["errors"] = [ test_info["errors"] ]

        # Load the files:
        resources_dir = os.path.join(os.path.realpath(os.path.dirname(__file__)), "Resources")
        files_that_exist = []
        for file in test_info["file wkt"]:
            file_path = os.path.join(resources_dir, file)
            if os.path.isfile(file_path):
                # Save it in the format FilesToWKT is expecting:
                files_that_exist.append(open(file_path, 'rb'))
            else:
                assert False, self.error_msg.format("File in 'file wkt' not found: {0}.")
        # Override with the new files:
        test_info["file wkt"] = files_that_exist
        return test_info

    def runAssertTests(self, test_info, wkt_json):
        if "parsed wkt" in test_info:
            if "parsed wkt" in wkt_json:
                lhs = shapely.wkt.loads(wkt_json["parsed wkt"])
                rhs = shapely.wkt.loads(test_info["parsed wkt"])
                assert lhs.almost_equals(rhs, decimal=8), self.error_msg.format("Parsed wkt returned from API did not match 'parsed wkt'.")
            else:
                # Here, I want content to be last. sometimes it explodes in length...                
                assert False, self.error_msg.format("API did not return a WKT.") + "\n - Content: "+str(wkt_json)
        if test_info["check errors"] == True:
            # Give errors a value to stop key-errors, and force the len() test to always happen:
            if "errors" not in wkt_json:
                wkt_json["errors"] = []
            for error in test_info["errors"]:
                assert str(error) in str(wkt_json["errors"]), self.error_msg.format("Response did not contain expected error.\nExpected: '{0}'\nNot found in:\n{1}\n".format(error, wkt_json["errors"]))
            assert len(test_info["errors"]) == len(wkt_json["errors"]), self.error_msg.format("Number of errors declared did not line up with number of expected errors.\nWarnings in response:\n{0}\n".format(wkt_json["errors"]))
