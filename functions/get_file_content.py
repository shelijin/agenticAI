import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([working_dir_abs, target_file])
        if valid_target_file == working_dir_abs:
            if os.path.isfile(target_file):
                with open(target_file, "r") as contents:
                    file_content_string = contents.read(MAX_CHARS)
                    if contents.read(1):
                        file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return file_content_string
            else: return f'Error: File not found or is not a regular file: "{file_path}"'
        else: return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    except  Exception as e:
        return f'Error: {e}'

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Opens file in a specified directory relative to the working directory, providing its contents as a string",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}