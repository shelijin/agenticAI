import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([working_dir_abs, target_file])
        if valid_target_file == working_dir_abs:
            if not os.path.isdir(target_file):
                os.makedirs(os.path.dirname(target_file), exist_ok=True)
                with open(target_file, "w") as contents:
                    contents.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
            else: return f'Error: Cannot write to "{file_path}" as it is a directory'
        else: return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    except  Exception as e:
        return f'Error: {e}'
        
        
schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Opens file in a specified directory relative to the working directory, writing the contents onto it",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "tpe": "string",
                    "description": "string to write onto the file"
                }
            },
        },
    },
}