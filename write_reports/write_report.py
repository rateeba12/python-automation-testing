def write_report(results, report_path="test_report.txt"):
    try:
        with open(report_path, "w", encoding="utf-8") as f:
            for test_name, status in results:
                f.write(f"{status}: {test_name}\n")
    except Exception as e:
        print("Failed to write test report:", e)
