def validate_args(func):
	def helper(*args, **kwargs):
		new_args = [0,0]
		if len(args) != 2:
			raise Exception(f"divide function expects 2 arguments, {len(args)} were recieved.")
		try:
			new_args[0] = float(args[0])
		except:
			raise Exception(f"The parameter {args[0]} passed to divide function is not convertible to a number")
		try:
			new_args[1] = float(args[1])
		except:
			raise Exception(f"The parameter {args[1]} passed to divide function is not convertible to a number")
		if(new_args[1]==0):
			raise Exception(f"Cannot divide by zero!")
		return func(*new_args, **kwargs)

	return helper


@validate_args
def divide(a,b):
	return a/b


print(divide(11,"dfdf","l"))