import argparse


def main():
    args = parseArgs()

    # TODO
    # Import file at: args.input
    # Lex/Parse 
    # Save new notebook.py file


def parseArgs():
    parser = argparse.ArgumentParser(description='Convert a script into a notebook')
    parser.add_argument('input', type=str, help='Input script file to convert')
    return parser.parse_args()


if __name__ == '__main__':
    main()