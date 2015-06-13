import argparse
from flashcards import flashCreate, flashStudy

parser = argparse.ArgumentParser(description="Create a new flash card deck or open an existing deck to study.")

parser.add_argument('-n', '--new', type=str, help="Create a new flash card deck to save to the passed file.", required=False)
parser.add_argument('-s', '--study', type=str, help="Open the specified file to load a flash card deck to study.", required=False)

args = parser.parse_args()

#A new deck/file is to be created.
if args.new != None:
     flashCreate(args.new)

#Open an existing deck/file to study from.
if args.study != None:
     flashStudy(args.study)