from check_installations import check_installations
from create_project_folder import create_project_folder
from create_virtual_env import create_virtual_env
from ask_test_framework import ask_test_framework
from ask_target_platform import ask_target_platform
from colorama import Fore, Style

framework_choice = ask_test_framework()

if framework_choice == 'Robot Framework':
    platform_choice = ask_target_platform()
    if platform_choice == 'Web':
        check_installations()
        project_name = create_project_folder()
        create_virtual_env(project_name)
    else:
        print(f"{Fore.RED}✗{Style.RESET_ALL} The selected platform is not yet supported.")
else:
    print(f"{Fore.RED}✗{Style.RESET_ALL} The selected framework is not yet supported.")