import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
    ) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([working_dir_abs, target_file])
        if valid_target_file == working_dir_abs:
            if os.path.isfile(target_file):
                if target_file.endswith('.py'):
                    command = ["python", target_file]
                    if args is not None:
                        command.extend(args)
                    completedprocess = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)
                    output = []
                    if completedprocess.returncode != 0:
                        output.append(f'Process exited with code {completedprocess.returncode}')
                    if completedprocess.stdout == "" and completedprocess.stderr == "":
                        return f'No output produced'
                    else: 
                        output.append(f'STDOUT: {completedprocess.stdout}')
                        output.append(f'STDERR: {completedprocess.stderr}')
                    return "\n".join(output)
                else: return f'Error: "{file_path}" is not a Python file'
            else: return f'Error: "{file_path}" does not exist or is not a regular file'
        else: return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f'Error: {e}'

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a file in a specified file_path relative to the working directory, using args as arguments and returning the output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to run file from, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "description": "Arguments to run the file with",
                },
            },
        },
    },
}