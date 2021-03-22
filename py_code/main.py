#! /usr/bin/python

import re
import argparse
import colorama

""""
Author - Adi Zavalkovsky

py_code scans files for a regex expression, and prints matches.

There are two high level functions - run(), main(), and one Class - Locator.
When main.py is ran through a cli, run() is the first function to run -
it's responsibility is to take in user input and pass it to main(),
which is responsible for initializing an instance of Locator, pass the user's arguments and run a scan.
Locator prints the scan's results to the screen.

The distinction between run() and main() is for testing purposes.
While run() is used for collecting user input, main() is responsible for using that input.
When testing the script - most tests will run on main().
"""


COLORS = {
    """
    Colors supported by the colorama module for printing.
    """
    'red':colorama.Fore.RED,
    'black':colorama.Fore.BLACK,
    'green':colorama.Fore.GREEN,
    'yellow':colorama.Fore.YELLOW,
    'blue':colorama.Fore.BLUE,
    'magneta':colorama.Fore.MAGENTA,
    'cyan':colorama.Fore.CYAN,
    'white':colorama.Style.RESET_ALL
}


class Locator:

    """
    This is the ptoject's main class,
    used for scanning files for a regex passed by the user.

    Attributes -
    exp - Regex expression to scan for.
    color - User selected color for highlighting regex matches.
    output - method chosen when an instance is initialized, based on a bool passed by the user.
    files - file_names that represent the files to be scanned.
    match_count - amount of matches found.

    Methods -
    machine_output, reg_output - Static methods, used for formatting the output.
    get_match_count - used for retrieving count of matches found in specified files. Mainly used for testing.
    analyze_files - runs through files submitted by user and looks for matches.
    """

    @staticmethod
    def machine_output(**kwargs):
        print(f'{kwargs["file_name"]}:{kwargs["line_num"]}:'
              f'{kwargs["match"].start()}:{kwargs["match"].group(0)}')

    @staticmethod
    def reg_output(**kwargs):
        print(f'Found match!\tFile name - {kwargs["file_name"]}\t Line num - {kwargs["line_num"]}\n'
                + kwargs["line"][:kwargs["match"].start()] + COLORS[kwargs["color"]] + kwargs["match"].group(0)
                + COLORS['white'] + kwargs["line"][kwargs["match"].end():].strip('\n'))

    def __init__(self, exp, color, machine, files):
        output_diff = {True: self.machine_output, False: self.reg_output}
        self.exp = exp
        if color:
            self.color = color
        else:
            self.color = 'white'
        self.output = output_diff[machine]
        self.files = files
        self.match_count = 0

    def get_match_count(self):
        return self.match_count

    def analyze_files(self):
        for file_name in self.files:
            try:
                with open(file_name, 'r') as file:
                    for line_num, line in enumerate(file):
                        for match in re.finditer(self.exp, line):
                            self.match_count += 1
                            self.output(**{"file_name": file_name, "line_num": line_num,
                                           "match": match, "line": line, "color": self.color})
            except FileNotFoundError as e:
                raise Exception(repr(e))


def main(**kwargs):

    colorama.init()  # Initialize coloring
    expression = kwargs['regex'][2:-1]  # Parse desired regex.

    locator = Locator(expression, kwargs['color'], kwargs['machine'], kwargs['files'])
    locator.analyze_files()

def run():

    """
    Collects user input using argparse, and passes it to main().
    Available arguments -
    regex - regex to be scanned for.
    files - files to scan.
    color - color to highlight matches with.
    machine - bool argument to determine output format.
        True - Locator.machine_output is used. False - Locator.reg_output is used.
    """

    parser = argparse.ArgumentParser(description='Locate regex in files.')

    parser.add_argument('regex',
                        help='Regex to scan for.', nargs=1)
    parser.add_argument('files',
                        help='Files to check for regex. Specify one or more.',
                        nargs='+')
    parser.add_argument('-c', '--color',
                        choices=COLORS.keys(),
                        help='Matching text color. Available colors: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE', )
    parser.add_argument('-m', '--machine',
                        help='Generate machine-readable output - file_name:no_line:start_pos:matched_text',
                        action='store_true')

    configs = parser.parse_args()
    configs.regex = configs.regex[0]
    main(**vars(configs))


if __name__ == '__main__':
    run()


