import platform
import subprocess
import sys
import inquirer
from colorama import Fore, Style
import os

def check_installation(program_name, check_command, project_name):
    if program_name == "Python":
        version = platform.python_version()
        print(f"{Fore.GREEN}✓{Style.RESET_ALL} {program_name} version detected: {version}")
        return True
    else:
        check_command = check_command.split()  # split the command into a list
        check_command = ' '.join(check_command)
        try:
            result = subprocess.run(check_command, capture_output=True, text=True, shell=True)
        except subprocess.SubprocessError:
            print(f"{Fore.RED}✗{Style.RESET_ALL} An error occurred while checking the {program_name} version.")
            return False
        output = result.stdout.strip() if result.stdout.strip() else result.stderr.strip()
        if result.returncode != 0:
            return False
        else:
            print(f"{Fore.GREEN}✓{Style.RESET_ALL} {program_name} version detected: {output}")
            return True

def check_installations(project_name):
    programs = [
        {"name": "Python", "command": ""},
        {"name": "pip", "command": "pip --version"},
        {"name": "Node.js", "command": "node --version", "install_url": "https://nodejs.org/en/download/"},
    ]

    for program in programs:
        if not check_installation(program["name"], program["command"], project_name):
            print(f"{Fore.RED}✗{Style.RESET_ALL} {program['name']} not found. Please install it from {program.get('install_url', 'the official website')}.")
            return False  # return False instead of exiting the program
    return True