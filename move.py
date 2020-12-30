import json
import pathlib


with open("report.json", "r") as read_file:
    filedict = json.load(read_file)

print(f'Do you want to move {len(filedict)}  files as defined in report.json?')
print(f'Type "move" if you want to move this files or "copy" if you want to copy them.')
print(f'WARNING: Move can´t be undone!')

input = input()



if input == "move":
    print('Start moving.')

elif input == "copy":
    print('Start copying. This can take a while.')

else:
    print('Nothing happens. Good bye.')


print(input)