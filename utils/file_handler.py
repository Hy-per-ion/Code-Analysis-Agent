def read_code_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        return None