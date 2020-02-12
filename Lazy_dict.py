class LazyDict(dict):
	def __delitem__(self, key):
		super().pop(key, None) 
	def __getitem__(self, key):
		return super().get(key)


ld = LazyDict()
ld[1] = 'x'
ld[2] = 'y'
del ld[1]
del ld[3]
assert(len(ld) == 1)
assert(ld[2] == 'y')
print("OK")

ld[2] = 'x'
assert(ld[1] == None)
assert(ld[2] == 'x')
print("OK")