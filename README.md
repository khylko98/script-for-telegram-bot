# File Renamer Script

This script is designed to help you quickly rename files in a specified folder by adding a new number to the beginning of the file names. It's particularly useful for bulk renaming of files that have a common prefix and a numbering scheme.

## Usage

1. **Requirements**: This script requires Python to be installed on your system.

2. **Folder Path**: Replace `/path/to/file` in the `folder_path` variable with the path to the folder containing the files you want to rename.

3. **New Number**: Set the `new_number` variable to the desired number that you want to add at the beginning of the new file names.

4. **Running the Script**: Open a terminal/command prompt, navigate to the directory where the script is saved, and run the script using the command:

   ```bash
   python files_rename_script.py
   ```

   Make sure to replace `files_rename_script.py` with the actual name of the script file.

5. **Output**: The script will iterate through the files in the specified folder. If a file name starts with "0" or "1" and has the format "prefix - filename", the script will rename the file by replacing the prefix with the new number. The renamed files will be in the format "new_number filename". The original file names will be replaced, and the script will print a message for each renaming operation.
