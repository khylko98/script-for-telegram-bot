import os


def rename_files(folder_path, new_number):
    for filename in os.listdir(folder_path):
        if filename.startswith("0") or filename.startswith("1"):
            parts = filename.split(" - ", 1)
            if len(parts) == 2:
                new_filename = f"{new_number} {parts[1]}"
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed {filename} to {new_filename}")


folder_path = "/path/to/file"
new_number = 1

rename_files(folder_path, new_number)
