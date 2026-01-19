from log_read.log_reader import read_log_file
from tests.test_system_boot_basic import test_system_boot_basic
from tests.test_link_status import test_link_status
from tests.test_config_applied import test_config_applied
from tests.test_no_errors import test_no_errors

file_path = r"inputs\inputs.log"

log = read_log_file(file_path)

tests = [test_system_boot_basic,test_link_status, test_config_applied, test_no_errors]

with open("test_report.txt", "w", encoding="utf-8") as result_file:
 for test in tests:
    try:
        test(log)
        print(f"PASS: {test.__name__}")
        result_file.write(f"PASS: {test.__name__}\n")

    except AssertionError as e:
        print(f"FAIL: {test.__name__}")
        result_file.write(f"FAIL: {test.__name__}\n")

