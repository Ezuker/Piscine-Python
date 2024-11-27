from math import isnan

def print_obj(object_type, object) -> int:
	print(object_type, type(object))
	return 0

def NULL_not_found(object: any) -> int:
	avalaible_type = {
		'NoneType': 'Nothing: None',
		'float': 'Cheese: nan',
		'int': 'Zero: 0',
		'str': 'Empty: ',
		'bool': 'Fake: False'
	}
	object_type = avalaible_type.get(type(object).__name__)
	if object_type is not None:
		if type(object).__name__ == 'int' and object == 0:
			return print_obj(object_type, object)
		if type(object).__name__ == 'float' and isnan(object):
			return print_obj(object_type, object)
		if type(object).__name__ == 'str' and object == "":
			return print_obj(object_type, object)
		if type(object).__name__ == 'NoneType' and object is None:
			return print_obj(object_type, object)
		if type(object).__name__ == 'bool' and object == False:
			return print_obj(object_type, object)
	print("Type not found")
	return 1