import cProfile, pstats, io



def profile(fnc):
    
    """A decorator that uses cProfile to profile a function"""
    
    def inner(*args, **kwargs):
        
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

#before profiling - runtime: 10.585 seconds
# def read_file():
#   with open('names.txt') as my_file:
#     read_data = my_file.read()
#     return read_data.splitlines() #split by line

# #suboptimal
# def is_duplicate(current, names):
#   for name in names:
#     if current.lower() == name.lower():
#       return True

# @profile
# def find_duplicates():
#   names = read_file()
#   duplicates = []
#   for name in names:
#     name = names.pop()
#     if is_duplicate(name, names):
#       duplicates.append(name)
#   print(duplicates)

# find_duplicates()

#after profiling - runtime: .668 seconds
def read_file():
  with open('names.txt') as my_file:
    read_data = my_file.read()
    return read_data.splitlines() #split by line

@profile
def find_duplicates():
  names = read_file()
  names = [name.lower() for name in names]
  duplicates = []
  for index in range(0, len(names)):
    if names[index] in names[index+1:]:
      duplicates.append(names[index])
  print(duplicates)

find_duplicates()