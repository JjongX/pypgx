import sys

from ..api import plot

import fuc
import pysam

description = f"""
This command will plot read depth profile with BAM data.

Usage examples:
  $ pypgx {fuc.api.common._script_name()} CYP2D6 target.tsv
"""

def create_parser(subparsers):
    parser = fuc.api.common._add_parser(
        subparsers,
        fuc.api.common._script_name(),
        help='Plot read depth profile with BAM data.',
        description=description,
    )
    parser.add_argument(
        'gene',
        help='Target gene.'
    )
    parser.add_argument(
        'depth',
        help='Read depth file for the target gene.'
    )
    parser.add_argument(
        '--path',
        metavar='PATH',
        help='Create plots in this directory.'
    )
    parser.add_argument(
        '--samples',
        metavar='TEXT',
        nargs='+',
        help='Create plots only for these samples.'
    )
    parser.add_argument(
        '--ymin',
        metavar='FLOAT',
        type=float,
        help='Y-axis bottom.'
    )
    parser.add_argument(
        '--ymax',
        metavar='FLOAT',
        type=float,
        help='Y-axis top.'
    )

def main(args):
    plot.plot_bam_read_depth(
        args.gene, args.depth, path=args.path,
        samples=args.samples, ymin=args.ymin, ymax=args.ymax
    )
