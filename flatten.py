#!/usr/bin/env python

def flatten(array):
	flattened_array = []
	for element in array:
		if isinstance(element, int):
			flattened_array.append(element)
		else:
			for subelement in element:
				flattened_array.append(subelement)
	return flattened_array



def main():
	array = [1, [2,3], 4]
	return flatten(array)

if __name__ == "__main__":
	print(main())