#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''{{cookiecutter.project_name}} - {{cookiecutter.project_short_description}}
'''

__author__ = '''{{cookiecutter.full_name}}'''
__email__ = '''{{cookiecutter.email}}'''
__version__ = '''{{cookiecutter.version}}'''


from argparse import ArgumentParser

parser = ArgumentParser(description='''{{cookiecutter.project_short_description}}''')
parser.add_argument('--version',
                    help='Print version number',
                    default=False,
                    action='store_true')


def main():
    args = parser.parse_args()
    if args.version:
        print('''{{cookiecutter.project_name}} ''' + __version__)


if __name__ == '__main__':
    main()