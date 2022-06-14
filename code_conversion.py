
from difflib import SequenceMatcher

def similarity(a, b):
	sequence = SequenceMatcher(a, b)  # comparing both the strings
	return sequence.ratio()

class Translation:
	OPS = {'=', '==',
		   '←', '=',
		   'DIV', '//'
		   'MOD', '%',
		   }

	def __init__(self):
		self.names = {}



def run_tests():

	from json import load

	with open("test_data/pseudocode_examples.json", "r", encoding="utf-8") as f:
		test_suite = load(f)


	for test_name, test_data in test_suite.items():
		print(f"Performing test: {test_name}")

		result = convert(test_data['input'])
		expected = test_data['expected']

		match = similarity(expected, result)

		if match == 1:
			print("Tests passed.")
		else:
			print(f"{round(match * 100, 2)}% successful:")

			print(f"""Expected:

{expected}

Received:

{result}
""")





if __name__ == "__main__":

	run_tests()