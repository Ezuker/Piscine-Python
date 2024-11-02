def all_thing_is_obj(object: any) -> int:
	avalaible_type = {
		'list': 'List',
		'tuple': 'Tuple',
		'set': 'Set',
		'dict': 'Dict',
		'str': '%s is in the kitchen :'
	}
	object_type = avalaible_type.get(type(object).__name__)
	if (type(object).__name__ == 'str'):
		print(object_type % object, type(object))
	elif object_type is not None:
		print(object_type, ":", type(object))
	else:
		print("Type not found")
	return 42