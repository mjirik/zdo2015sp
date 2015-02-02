#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 mjirik <mjirik@hp-mjirik>
#
# Distributed under terms of the MIT license.

"""

"""

import logging
logger = logging.getLogger(__name__)
import argparse
import yaml
import numpy as np
import scipy
import scipy.misc


def format_generator():
    mask = np.zeros([30, 40])
    scipy.misc.imsave('f1.png', mask)
    mask[:10, 14:20] = 255
    scipy.misc.imsave('f2.png', mask)
    mask[:10, 14:20] = 0
    mask[5:15, 10:25] = 1
    scipy.misc.imsave('f3.png', mask)
    sp1 = {
        'name': 'M. Jirik',
        'data': [
            {'file': 'f1.jpg', 'start': 0, 'stop': 10},
            {'file': 'f2.jpg', 'start': 10, 'stop': 12.5},
            {'file': 'f3.jpg', 'start': 12.5, 'stop': 13}
        ]
    }
    with open('sp1.yml', 'w') as outfile:
        outfile.write(yaml.dump(sp1))  # , default_flow_style=True))


def format_checker(filename='sp1.yml', verbose=True):
    with open(filename, 'r') as f:
        ymldata = yaml.load(f)

    ymldata['name']

    for one in ymldata['data']:
        if set(['file', 'start', 'stop']).issubset(one.keys()):
            scipy.misc.imread(one['file'])
        else:
            logger.error('Some key is missing')
            return False

    if verbose:
        print "Format Ok"
    return True


def main():
    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    logger.addHandler(ch)

    # create file handler which logs even debug messages
    # fh = logging.FileHandler('log.txt')
    # fh.setLevel(logging.DEBUG)
    # formatter = logging.Formatter(
    #     '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # fh.setFormatter(formatter)
    # logger.addHandler(fh)
    # logger.debug('start')

    # input parser
    parser = argparse.ArgumentParser(
        description=__doc__
    )
    parser.add_argument(
        '-i', '--inputfile',
        default=None,
        # required=True,
        help='input file'
    )
    parser.add_argument(
        '-d', '--debug', action='store_true',
        help='Debug mode')
    parser.add_argument(
        '--generate-sp1-sample', action='store_true',
        help='Generate sample files')
    parser.add_argument(
        '--check-format', action='store_true',
        help='Generate sample files')
    args = parser.parse_args()

    if args.debug:
        ch.setLevel(logging.DEBUG)

    if args.generate_sp1_sample:
        format_generator()
    if args.check_format:
        format_checker()


if __name__ == "__main__":
    main()
