
class Default(dict):
    def __missing__(self, key):
        return key
    
result = '{name} was born is {country}'.format_map(Default(name="Gallibo"))

print(result)