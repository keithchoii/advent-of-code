# script for creating a new folder system
# change year as needed

import os

CURR_YEAR = '2023'

def directories() -> None:
    try:
        os.makedirs(CURR_YEAR)
        print(f'folder created for {CURR_YEAR}')
    except FileExistsError:
        print(f'FileExistsError: folder for {CURR_YEAR} already exists')

    for i in range(1,26):
        try:
            path = os.path.join(CURR_YEAR, str(i))
            os.makedirs(path)
            print(f'folder created for {path}')
        except FileExistsError:
            print(f'FileExistsError: folder for {path} already exists')

        python_file = 'day' + str(i) + '.py'
        create_file(path, python_file)

        input_file = str(i) + '.txt'
        create_file(path, input_file)

def create_file(path: str, file_name: str) -> None:
    new_path = os.path.join(path, file_name)
    if os.path.isfile(new_path):
        print(f'FileExistsError: {file_name} already exists in {path}')
        return
    
    match file_name.split('.')[1]:
        case 'py':
            with open(new_path, 'a') as f:
                f.write(("# day " + file_name.split('.')[0][-1] + " solution\n"
                         "# Title\n"
                         "\n"
                         "input_file = '" + path + "\\" + file_name.split('.')[0][-1] + ".txt'\n"
                         "with open(input_file) as f:\n"
                         "\tdata = f.read()\n"
                         "\n"
                         "if __name__ == '__main__':\n"
                         "\tprint(f'part 1: ')\n"
                         "\tprint(f'part 2: ')\n"
                ))
                print(f'{file_name} created in {path}')
        case 'txt':
            open(new_path, 'a').close()
            print(f'{file_name} created in {path}')
        case _:
            print(f"{file_name}'s file type '{_}' not supported")


if __name__ == '__main__':
    directories()
