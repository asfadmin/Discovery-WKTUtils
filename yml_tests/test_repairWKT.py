import os, sys           # Generic imports
import shapely.wkt, geomet.wkt      # For comparing wkt's

# Add the package to pythonpath before import:
root_dir = os.path.abspath(os.path.join(".."))
if root_dir not in sys.path:
    sys.path.append(root_dir)
from WKTUtils.RepairWKT import repairWKT

class test_repairWKT_manager():
    def __init__(self, test_info, file_conf, cli_args, test_vars):
        self.error_msg = "Reason: {0}\n - File: '{1}'\n - Test: '{2}'".format('{0}', file_conf["yml name"], test_info["title"])

        test_info = self.applyDefaultValues(test_info)
        # Make a request, and turn it into json. Helpers should handle if something goes wrong:
        
        if "from_crs" in test_info:
            repaired_wkt_json = repairWKT(test_info["test wkt"], default_crs=test_info["from_crs"])
        else:
            repaired_wkt_json = repairWKT(test_info["test wkt"])
        # Make sure the response matches what is expected from the test:
        self.runAssertTests(test_info, repaired_wkt_json)
        if test_info["print"] == True:
            print(test_info["title"])
            print("  -- Returned: {0}".format(repaired_wkt_json))

    def applyDefaultValues(self, test_info):
        # Copy 'repaired wkt' to the wrapped/unwrapped versions if used:
        if "repaired wkt" in test_info:
            for i in ["repaired wkt wrapped", "repaired wkt unwrapped"]:
                if i not in test_info:
                    test_info[i] = test_info["repaired wkt"]
            del test_info["repaired wkt"]
    
        # Figure out what test is 'expected' to do:
        pass_assertions = ["repaired wkt wrapped", "repaired wkt unwrapped", "repair"]
        fail_assertions = ["repaired error msg"]
        # True if at least one of the above is used, False otherwise:
        pass_assertions_used = 0 != len([k for k,_ in test_info.items() if k in pass_assertions])
        fail_assertions_used = 0 != len([k for k,_ in test_info.items() if k in fail_assertions])

        # Default Print the result to screen if tester isn't asserting anything:
        if "print" not in test_info:
            test_info["print"] = False if (pass_assertions_used or fail_assertions_used) else True
        # If they expect something to pass, check if it needed repairing too:
        if "check repair" not in test_info:
            test_info["check repair"] = pass_assertions_used

        # Add the repair if needed. Make sure it's a list:
        if "repair" not in test_info:
            test_info["repair"] = []
        elif not isinstance(test_info["repair"], type([])):
            test_info["repair"] = [test_info["repair"]]
        
        # If they passed more than one wkt, combine them:
        if isinstance(test_info["test wkt"], type([])):
            test_info["test wkt"] = "GEOMETRYCOLLECTION({0})".format(",".join(test_info['test wkt']))
        return test_info

    def runAssertTests(self, test_info, response_json):
        if "repaired wkt wrapped" in test_info:
            if "wkt" in response_json:
                responce = shapely.wkt.loads(response_json["wkt"]["wrapped"])
                expected = shapely.wkt.loads(test_info["repaired wkt wrapped"])
                assert responce.almost_equals(expected, decimal=8) , self.error_msg.format("WKT wrapped failed to match the result.\nExpected: {0}\nActual: {1}\n".format(test_info["repaired wkt wrapped"], response_json["wkt"]["wrapped"]))
            else:
                assert False, "WKT not found in response from API. Test: '{0}'. Response: {1}.".format(test_info["title"], response_json)
        if "repaired wkt unwrapped" in test_info:
            if "wkt" in response_json:
                responce = shapely.wkt.loads(response_json["wkt"]["unwrapped"])
                expected = shapely.wkt.loads(test_info["repaired wkt wrapped"])
                assert responce.almost_equals(expected, decimal=8), self.error_msg.format("WKT unwrapped failed to match the result.\nExpected: {0}\nActual: {1}\n".format(test_info["repaired wkt wrapped"], response_json["wkt"]["wrapped"]))
            else:
                assert False, self.error_msg.format("WKT not found in response from API. Response: {0}.".format(response_json))

        if test_info["check repair"]:
            if "repairs" in response_json:
                for repair in test_info["repair"]:
                    assert repair in str(response_json["repairs"]), self.error_msg.format("Expected repair was not found in results. Repairs done: {0}".format(response_json["repairs"]))
                assert len(response_json["repairs"]) == len(test_info["repair"]), self.error_msg.format("Number of repairs doesn't equal number of repaired repairs. Repairs done: {0}.".format(response_json["repairs"]))
            else:
                assert False, "Unexpected WKT returned: {0}. Test: '{1}'".format(response_json, test_info["title"])
        if "repaired error msg" in test_info:
            if "error" in response_json:
                assert test_info["repaired error msg"] in response_json["error"]["report"], self.error_msg.format("Got different error message than expected. Error returned: {0}".format(response_json["error"]["report"]))
            else:
                assert False, self.error_msg.format("Unexpected WKT returned. Response: {0}.".format(response_json))

