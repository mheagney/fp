import argparse
import os
import sys
import requests


# Globals

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
APP_DIR = 'app'
APP_FILES = ['__init__.py', 'config.py', 'run.py', 'create_db.py', 'shell.py']
STATIC_DIR = 'static'
STATIC_SUBDIRS = ['css', 'fonts', 'img', 'js']
TEMPLATE_DIR = 'templates'
TEMPLATE_FILES = ['base.html', 'macros.html']
VIEWS_DIR = 'views'

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--init",
                    help="Initialize a project", action="store_true")
parser.add_argument("-n", "--name",
                    help="Project Name", nargs='+')
parser.add_argument("-u", "--ui",
                    help="UI Library")
parser.add_argument("-a", "--auth",
                    help="Authentication System")
parser.add_argument("-d", "--db",
                    help="Database Backend")
args = parser.parse_args()


# Create a new project
if args.init:
    if not args.name:
        sys.exit('You must have a project name')
    project_dir = '{}/{}'.format(BASE_DIR, '-'.join(args.name))
    if os.path.exists(project_dir):
        sys.exit('Project Directory already exists')
    else:
        os.makedirs(project_dir)
        os.makedirs('/'.join([project_dir, APP_DIR]))
        os.makedirs('/'.join([project_dir, APP_DIR, TEMPLATE_DIR]))
        os.makedirs('/'.join([project_dir, APP_DIR, VIEWS_DIR]))
        os.makedirs('/'.join([project_dir, APP_DIR, STATIC_DIR]))
        for sub in STATIC_SUBDIRS:
            os.makedirs('/'.join([project_dir, APP_DIR, STATIC_DIR, sub]))
