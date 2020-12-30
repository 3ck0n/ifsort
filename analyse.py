import os
import json
import pathlib
import datetime


"""
Analyse.py

Generate a proposal to refactor a recursive file structure.
Idea is to sort a chaotic file structure to a scheme like
- Archivename YYYY
  - MM Month
     - DD name of series
       - Original files
"""

source = pathlib.Path.cwd() / 'sample' # source directory
target = pathlib.Path.cwd() / 'target' # target directory
filedict = [] # List with files


def get_modified_datetime(file: pathlib):
    """
    Returns a datetime with modified date of a given file.
    """
    modified_timestamp = file.stat().st_mtime
    modified = datetime.datetime.fromtimestamp(modified_timestamp)
    return modified

def gen_folder_name(day, rpath: pathlib):
    """
    Generates a target folder nape for a relative part and a day.
    Scheme is 'DD relative-path_separated_by_underscore'
    """
    sday = str(day).zfill(2)
    spath = str(rpath)
    spath = spath.replace(' ', '-')
    spath = spath.replace('\\', '_')
    spath = spath.lower()
    if spath == '.':
        spath = 'Day'
    return f"{sday} {spath}"

def gen_relativ_path(modified, folder, file):
    str = f"Rohdaten {modified.year}\\{modified.strftime('%m %B')}\\{folder}\\{file.name}"
    return str

def analyse(source_directory, target_directory = '.'):
    """
    Analysis a source_directory by creating a folder structure proposal for every file.
    Sourcefile and moved file are documented in filedict global array to support analysis before
    start moving them.
    """
    for file in source_directory.rglob('*'):
        filson = {}
        print('.', end='')
        if not file.is_dir():
            rpath = file.parent.relative_to(source_directory)
            modified = get_modified_datetime(file)

            target_folder_name = gen_folder_name(modified.day, rpath)

            filson['file'] = str(file)
            filson['move'] = str(target_directory.joinpath(gen_relativ_path(modified, target_folder_name, file)))

            filedict.append(filson)

    print('!')



print(f'Analyse {source} recursive')
analyse(source, target)

print(f'Found {len(filedict)} files.')

with open("report.json", "w") as write_file:
    json.dump(filedict, write_file, indent=4, sort_keys=True,)

print('Proposal saved in report.json.')