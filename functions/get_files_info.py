import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir])
        if valid_target_dir == working_dir_abs:
            if os.path.isdir(target_dir):
                contents = os.listdir(target_dir)
                results = []
                for content in contents:
                    content_path = os.path.join(target_dir, content)
                    results.append(f"- {content}: file_size={os.path.getsize(content_path)} bytes, is_dir={os.path.isdir(content_path)}")
                return "\n".join(results)

            else: return f'Error: "{directory}" is not a directory'
        else: return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except  Exception as e:
        return f'Error: {e}'

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}





        
    
        
    
