import argparse

def eval(first, second):
	choices = ["rock", "paper", "scissor", "r", "p", "s"]
	if first not in choices or second not in choices:
		raise ValueError("Invalid hand, has to be rock paper or scissor or their first letter")
	

	if first == "rock" or first == "r":
		

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--first", "-f", type = str, default = None, help = "First person's choice, can be a single choice or a text file")
	parser.add_argument("--second", "-s", type = str, default = None, help = "Second person's choice, can be a single choice or a text file")

	args = parser.parse_args()

	if args.first == None or args.second == None:
		raise ValueError("Both players required")
	else:
		first = args.first
		second = args.second

	choices = ["rock", "paper", "scissor", "r", "p", "s"]

	
