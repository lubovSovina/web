import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--name')
parser.add_argument('-up', '--up_case', action='store_true',
                    help='convert name to upper register')
parser.add_argument('--number', choices=[0, 1, 2], type=int,
                    default=0, help='select number', required=True)
parser.add_argument('--no_name', action='store_const', const='no',
                    dest='name')
args = parser.parse_args()

name = args.name
if args.up_case and name is not None:
    name = name.upper()
print(f'The name is {name}. And the number = {args.number}')