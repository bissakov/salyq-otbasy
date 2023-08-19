import sys

import json
import os
from shutil import copyfile

system_paths = ['C:\\Users\\robot.ad\\Desktop\\Salyk\\src', 'C:\\Users\\robot.ad\\Desktop\\Salyk', 'C:\\Program Files\\Python310\\python310.zip', 'C:\\Program Files\\Python310\\DLLs', 'C:\\Program Files\\Python310\\lib', 'C:\\Program Files\\Python310', 'C:\\Users\\robot.ad\\Desktop\\Salyk\\venv', 'C:\\Users\\robot.ad\\Desktop\\Salyk\\venv\\lib\\site-packages', 'C:\\Users\\robot.ad\\Desktop\\Salyk\\venv\\lib\\site-packages\\win32', 'C:\\Users\\robot.ad\\Desktop\\Salyk\\venv\\lib\\site-packages\\win32\\lib', 'C:\\Users\\robot.ad\\Desktop\\Salyk\\venv\\lib\\site-packages\\Pythonwin']


def get_params():
    data = sys.stdin
    params = json.load(data)
    return params


def print_params(params, path='params_print.txt'):
    with open(path, 'w') as file_write:
        file_write.write(json.dumps(params))


if __name__ == '__main__':
    with open(__file__) as f:
        lines = f.readlines()
    print(lines)

    for i in range(len(lines)):
        if 'system_paths =' in lines[i][0:15]:
            lines[i] = f'system_paths = {str(sys.path)}\n'
            break

    with open(__file__, 'w') as f:
        f.write(''.join(lines))

    for system_path in system_paths:
        if system_path.endswith(r'\site-packages'):
            copyfile(fr'{system_path}\pywin32_system32\pythoncom310.dll', fr'{system_path}\win32\lib\pythoncom310.dll')
            copyfile(fr'{system_path}\pywin32_system32\pywintypes310.dll', fr'{system_path}\win32\lib\pywintypes310.dll')

else:
    if not str(os.getcwd()).endswith('Core_Agent'):
        sys.path = system_paths
