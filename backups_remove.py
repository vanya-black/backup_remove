import os
from datetime import datetime
import argparse


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


parser = argparse.ArgumentParser(description='This utility removed backup files from folder.' +
                                             'Backups file name must be start with datetime in %y%m%d_%H%M%S format' +
                                             'You can specify the number of days')
parser.add_argument('path', type=dir_path, default='.')
parser.add_argument('-d', '--days', type=int, default=100,
                    help='Number of days after which backups will be deleted')


args = parser.parse_args()

filenames = [f for f in os.listdir(args.path) if os.path.isfile(os.path.join(args.path, f))]
timestamps = [datetime.strptime(ts[:13], '%y%m%d_%H%M%S') for ts in filenames]

for filename, timestamp in zip(filenames, timestamps):
    if (datetime.now()-timestamp).days > args.days:
        os.remove(os.path.join(args.path, filename))
