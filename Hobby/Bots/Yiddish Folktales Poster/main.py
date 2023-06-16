import argparse


def get_args() -> argparse.Namespace:
    """Get command-line arguments, or raise an error if they're missing."""
    parser = argparse.ArgumentParser(
        prog='hw5',
        description='[LING 571, HW 5]',
        epilog='Author: Cat Ball <catball at uw dot edu>, 2022-02-08',
    )
    # parser.add_argument('input_dependency_parse_filename', type=str)
    # parser.add_argument('output_dependency_filename', type=str)
    # parser.add_argument('output_sequence_filename', type=str)

    return parser.parse_args()


def main():
    pass
