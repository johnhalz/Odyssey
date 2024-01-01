import argparse
from pathlib import Path
import json


def parse_arguments():
    """Parse input arguments to app"""
    parser = argparse.ArgumentParser(
        prog='Setup Units',
        description='Setup units in database'
    )
    parser.add_argument(
        '--unit_types',
        dest='unit_types',
        type=Path,
        required=True,
        help='Unit types json file path'
    )
    parser.add_argument(
        '--units',
        dest='units',
        type=Path,
        required=True,
        help='Units json file path'
    )

    return parser.parse_args()


def evaluate_args():
    """Evaluate input arguments"""
    args = parse_arguments()

    if not args.unit_types.exists():
        raise ValueError(f'Unit types file does not exist: {args.unit_types.as_posix()}')

    if not args.unit_types.suffix == '.json':
        raise ValueError(f'Unit types file extension is not json: {args.unit_types.as_posix()}')

    if not args.units.exists():
        raise ValueError(f'Units file does not exist: {args.units.as_posix()}')

    if not args.units.suffix == '.json':
        raise ValueError(f'Units file extension is not json: {args.units.as_posix()}')

    return args.unit_types, args.units


def main(unit_types_path: Path, units_path: Path) -> None:
    with open(unit_types_path) as unit_types_file:
        unit_types = json.load(unit_types_file)

    with open(units_path) as units_file:
        units = json.load(units_file)

    # TODO: Write unit types into database
    # TODO: Parse unit dictionary
    # TODO: Write units into database


if __name__ == '__main__':
    main(*evaluate_args())
