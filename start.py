#  This file is part of OctoBot (https://github.com/Drakkar-Software/OctoBot)
#  Copyright (c) 2023 Drakkar-Software, All rights reserved.
#
#  OctoBot is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  OctoBot is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with OctoBot. If not, see <https://www.gnu.org/licenses/>.
import sys
import os

# Use os.path to dynamically calculate the project root
# Going one level up from the current file (start.py) to the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# List of subdirectories you want to add to PYTHONPATH (adjusted for correct structure)
directories = [
    'OctoBot',
    'Async-Channel',
    'OctoBot-Backtesting',
    'OctoBot-Commons',
    'OctoBot-Evaluators',
    'OctoBot-Script',
    'OctoBot-Services',
    'OctoBot-Tentacles',
    'OctoBot-Tentacles-Manager'
    'OctoBot-Trading',
    'OctoBot-trading-backend',
]

# Debug: Print the root project directory
print(f"Project root directory: {project_root}")

# Add each directory to sys.path and debug
for directory in directories:
    dir_path = os.path.join(project_root, directory)
    if os.path.exists(dir_path):
        sys.path.append(dir_path)
        print(f"Added to sys.path: {dir_path}")  # Debug print for added directories
    else:
        print(f"Directory not found: {dir_path}")  # Debug print if directory is not found

# Debug: Print the current sys.path after adding directories
print("\nCurrent sys.path:")
for path in sys.path:
    print(path)

# Try to import the required module and debug
try:
    from octobot.cli import main
    print("\nSuccessfully imported 'octobot.cli.main'")  # Debug print if import is successful
except ModuleNotFoundError as e:
    print(f"\nERROR: {e}")  # Debug print if there is an error importing the module

# Ensure that the main function is called if the import is successful
if __name__ == '__main__':
    main(sys.argv[1:])