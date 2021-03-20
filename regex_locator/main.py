#! /usr/bin/python

import argparse
import re
import colorama







class Locator:

    @staticmethod
    def machine_output(**kwargs):
        print('{}:{}:{}:{}'.format(kwargs["file_name"], kwargs["line_num"],
                                   kwargs["match"].start(), kwargs["match"].group(0)))

    @staticmethod
    def reg_output(**kwargs):
        print('Found match!\tFile name - {}\t Line num - {}\n'.format(kwargs["file_name"], kwargs["line_num"])
                + kwargs["line"][:kwargs["match"].start()] + COLORS[kwargs["color"]] + kwargs["match"].group(0)
                + COLORS['white'] + kwargs["line"][kwargs["match"].end():].strip('\n'))

    def __init__(self, exp, color, machine, files):
        output_diff = {True: self.machine_output, False: self.reg_output}
        self.exp = exp
        if color:
            self.color = color
        else:
            self.color = 'white'
        self.machine = machine
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


COLORS = {
    'red':colorama.Fore.RED,
    'black':colorama.Fore.BLACK,
    'green':colorama.Fore.GREEN,
    'yellow':colorama.Fore.YELLOW,
    'blue':colorama.Fore.BLUE,
    'magneta':colorama.Fore.MAGENTA,
    'cyan':colorama.Fore.CYAN,
    'white':colorama.Style.RESET_ALL
}




def main(**kwargs):


    print(kwargs['machine'])
    # Initialize terminal coloring
    colorama.init()

    # Initialize regex
    expression = kwargs['regex'][2:-1]

    locator = Locator(expression, kwargs['color'], kwargs['machine'], kwargs['files'])

    locator.analyze_files()

def run():
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


    # Initialize argument parser
    configs = parser.parse_args()
    configs.regex = configs.regex[0]
    main(**vars(configs))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()


