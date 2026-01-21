def read_log_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return True, f.read()
    except Exception as e:
        return False, str(e)