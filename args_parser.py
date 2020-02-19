import argparse

parser = argparse.ArgumentParser()
parser.add_argument("run_time_variable")
args = parser.parse_args()

if args.run_time_variable == 'Python is bae!':
    print('You made it!')
else:
    print("Didn't make it!")