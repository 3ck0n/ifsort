import json
import pathlib


with open("report.json", "r") as json_file:
    filedict = json.load(json_file)

print(f'Do you want to move {len(filedict)}  files as defined in report.json?')
print(f'Type "move" if you want to move this files or "copy" if you want to copy them.')
print(f'WARNING: Move can´t be undone!')

input = input()
i = 0


if input == "move":
    print('Start moving.')
    i = 0
    len = len(filedict)

    for item in filedict:
        print('.', end='')
        
        target = item['move']
        source = item['file']

        pathlib.Path(target).parent.mkdir(parents=True, exist_ok=True)

        pathlib.Path(source).rename(target)
        item['state'] = 'moved'
        filedict[i] = item

        i = i + 1
        if i % 10 == 0:
            print(f' {round((i/len)*100, 3)}%')



elif input == "copy":
    print('Start copying. This can take a while.')

else:
    print('Nothing happens. Good bye.')


with open("report.json", "w") as write_file:
    json.dump(filedict, write_file, indent=4, sort_keys=True,)

print('! Done')
print('State change saved in report.json.')
