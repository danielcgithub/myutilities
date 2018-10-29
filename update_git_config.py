#!/usr/bin/python
import getopt
import sys
from subprocess import call

import configparser


work = 'work'
personal = 'personal'

def main(argv):
    inputfile = ''
    config = ''
    try:
        opts, args = getopt.getopt(argv, "hri:c:", ["ifile=", "config="])
        if not opts:
            print('Parameters Required!')
            help_info()
            sys.exit(2)
    except getopt.GetoptError:
        print('Error, please use the following info to call the script correctly:')
        help_info()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            help_info()
        elif opt in ('-r'):
            read_settings()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-c", "--config"):
            config = arg
    print('Input file is ', inputfile)
    print('Config selected is ', config)
    update_settings(inputfile, config)


def update_settings(inputfile, specconfig):
    config = configparser.ConfigParser()
    config.sections()

    config.read(inputfile)

    if work in specconfig:
        set_configuration(config, work)
    elif personal in specconfig:
        set_configuration(config, personal)


def set_configuration(config, option):
    username = config[option]['user']
    email = config[option]['email']
    print('Username that will be set = '+username)
    print('E-mail that will be set = '+email)
    call(["git", "config", "--global", "user.name", username])
    call(["git", "config", "--global", "user.email", email])


def help_info():
    print('\n\tpython ./update_git_config.py -i <inputfile> -c <config>')
    print('\tFor example:')
    print('\tTo set work config.:')
    print('\t\tpython ./update_git_config.py -i ../git.cfg -c work')
    print('\tor')
    print('\tTo set personal config.:')
    print('\t\tpython ./update_git_config.py -i ../git.cfg -c personal')
    print('\tor')
    print('\tTo read current config.:')
    print('\t\tpython ./update_git_config.py -r')
    sys.exit()


def read_settings():
    call(["git", "config", "user.name"])
    call(["git", "config", "user.email"])
    print('Current user.name and user.email settings')
    sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
