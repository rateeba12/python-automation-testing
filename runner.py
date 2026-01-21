from log_read.log_reader import read_log_file
from run_tests.run_tests import run_tests
from write_reports.write_report import write_report

file_path = r"inputs\inputs.log"

log = read_log_file(file_path)

results = run_tests(log)
write_report(results)