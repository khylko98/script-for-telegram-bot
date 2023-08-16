# File Renamer Script

This script is designed to help you quickly rename files in a specified folder by adding a new number to the beginning of the file names. It's particularly useful for bulk renaming of files that have a common prefix and a numbering scheme.

## Usage

1. **Requirements**: This script requires Python to be installed on your system.

2. **Folder Path**: Replace `/path/to/file` in the `folder_path` variable with the path to the folder containing the files you want to rename.

3. **New Number**: Set the `new_number` variable to the desired number that you want to add at the beginning of the new file names.

4. **Running the Script**: Open a terminal/command prompt, navigate to the directory where the script is saved, and run the script using the command:

   ```bash
   python script_name.py
   ```

   Make sure to replace `script_name.py` with the actual name of the script file.

5. **Output**: The script will iterate through the files in the specified folder. If a file name starts with "0" or "1" and has the format "prefix - filename", the script will rename the file by replacing the prefix with the new number. The renamed files will be in the format "new_number filename". The original file names will be replaced, and the script will print a message for each renaming operation.

## Example

Let's say you have a folder with the following files:

- 01 - Document.txt
- 02 - Image.jpg
- 03 - Notes.txt
- 04 - Report.docx

If you set `new_number` to 100 and run the script, the files will be renamed as follows:

- 100 Document.txt
- 100 Image.jpg
- 100 Notes.txt
- 100 Report.docx

Remember to back up your files before running the script, as renaming files can't be undone.

## Note

- This script assumes that the files you want to rename follow a specific naming convention, where the file name starts with either "0" or "1", followed by a space, hyphen, and space.
- Make sure you have the necessary permissions to modify files in the specified folder.

**Use this script responsibly and always make sure to have backups of your data before performing bulk renaming operations.**
