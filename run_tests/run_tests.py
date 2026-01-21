from tests.test_system_boot_basic import test_system_boot_basic
from tests.test_link_status import test_link_status
from tests.test_config_applied import test_config_applied
from tests.test_no_errors import test_no_errors

tests = [test_system_boot_basic,test_link_status, test_config_applied, test_no_errors]

def run_tests(log):
    results = []
    for test in tests:
        try:
            test(log)
            results.append((test.__name__, "PASS"))
        except AssertionError:
            results.append((test.__name__, "FAIL"))

    return results
