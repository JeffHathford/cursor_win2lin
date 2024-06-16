how to convert a windows cursor to an xcursor format, step by step:

definitions:
    - <input_folder>    - folder with Windows cursor files (.ani and .cur)
    - <convert_folder>  - folder with files converted by win2xcur
    - <output_folder>   - folder with properly named Xcursor files

1. 'pip install win2xcur'
    - used to do the initial conversion between Windows and Xcursor file formats
    - can (and probably should) be used with a venv

2. 'win2xcur <input_folder>/*.{ani,cur} -o <conver_folder>'
    - the output folder must exist

3. 'python ./cursor_map.py <convert_folder> <output_folder>'
    - depending on your PATH entry use 'python' or 'python3'

4. open <output_folder>/cursors/default in an image editor and export to thumbnail.png,
   save in the same folder


once you have a folder with proper Xcursor files, move it to either:
- /usr/share/icons - makes cursor available for all users, requires root
- /home/<your_username>/.icons - makes it available only for you
