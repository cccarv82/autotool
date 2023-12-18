# check_for_updates.py

import pkg_resources
import subprocess
import sys

import requests

from colorama import Fore, Style
import inquirer

def check_for_updates():
    # Get the current version of the package
    try:
        current_version = pkg_resources.get_distribution('automation-fw-setup').version
    except pkg_resources.DistributionNotFound:
        current_version = 'local'

    # Skip update check for local development version
    if current_version == 'local':
        return

    # Get the latest version available on PyPI
    response = requests.get('https://pypi.org/pypi/automation-fw-setup/json')
    releases = response.json()['releases']
    latest_version = sorted(releases.keys(), key=pkg_resources.parse_version, reverse=True)[0]

    # Check if the current version is the latest version
    if current_version != latest_version:
        print(f"{Fore.RED}✗{Style.RESET_ALL} {Style.BRIGHT}A new version of automation-fw-setup is available: {Fore.GREEN}{latest_version}{Style.RESET_ALL}. You are currently using version {Fore.RED}{current_version}{Style.RESET_ALL}.")

        questions = [
            inquirer.Confirm('update',
                             message=f"{Fore.YELLOW}[?]{Style.RESET_ALL} Do you want to update now?",
                             default=True),
        ]

        answers = inquirer.prompt(questions)

        if answers['update']:
            subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'automation-fw-setup'])
            print(f"{Fore.GREEN}✓{Style.RESET_ALL} {Style.BRIGHT}Updated to version {Fore.GREEN}{latest_version}{Style.RESET_ALL}. Please restart the program to use the new version.")
            sys.exit(0)  # Exit the program