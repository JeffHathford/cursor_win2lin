# 1. Read all files in input folder and build a key-side dictionary
# 2. Use mappings.txt to fill the values of the dictionary
# 3. Convert input folder using win2xcur (call win2xcur from terminal)
# 4. For every file in output folder as key, convert it to values from the dictionary
# 5. Convert 'default' or 'pointer' to thumbnail.png

import os
import sys
import shutil

def no_file_extension(str):
    return os.path.splitext(str)[0]

def get_file_list(folder_path):
    #return [no_file_extension(f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def load_mappings(mappings_file):
    mappings = {}
    with open(mappings_file, "r") as file:
        for line in file:

            try:
                [key, value] = line.split(sep="=")
            except ValueError:  # empty line
                continue

            key = key.strip()
            value = value.replace(" ", "").replace("\n","").split(sep=",")

            mappings[key] = value

    return mappings

def build_main_dictionary(file_list, template_mappings):
    dictionary = {}
    for file in file_list:
        try:
            dictionary[file] = template_mappings[file]
        except KeyError:
            pass

    return dictionary



[input_folder, output_folder] = [None, None]

try:
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
except IndexError:
    print("Error: Expected exactly 2 arguments: <input_folder> and <output_folder>")
    exit(1)


default_mappings_file = "mappings.txt"

input_files = get_file_list(input_folder)
template_mappings = load_mappings(default_mappings_file)
current_mappings = build_main_dictionary(input_files, template_mappings)

cursor_folder = f"{output_folder}/cursors"

if not os.path.exists(cursor_folder):
    try:
        os.makedirs(cursor_folder)
    except OSError as e:
        print(f"Error: Failed to create directory {cursor_folder}. {e.strerror}")
        exit(1)

for key, value in current_mappings.items():
    if value != "-" and value[0] != "-":

        win_name = key

        for xcur_name in value:
            shutil.copy2(f"{input_folder}/{win_name}", f"{output_folder}/cursors/{xcur_name}")

        if input_folder == output_folder:
            os.remove(f"{input_folder}/{win_name}")

cursor_name = input("\nName of the cursor pack?\n")

with open(f"{output_folder}/index.theme", "w") as index:
    index.writelines(["[Icon Theme]\n", f"Name={cursor_name}"])

with open(f"{output_folder}/cursor.theme", "w") as index:
    index.writelines(["[Icon Theme]\n", f"Inherits={cursor_name}"])

