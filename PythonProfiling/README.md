Overview
===

This is a brief demonstration of profiling in Python using the cProfile library

* **main.py**  
  Read names from names.txt and find any duplicates in the list neglecting case
  sensativity.

* **names.txt**  
  List of 5000 names

Sample output
---

Before profiling  
```
['joni', 'Addy']
         18344839 function calls in 10.585 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.008    0.008   10.585   10.585 main.py:35(find_duplicates)
     2474    6.788    0.003   10.574    0.004 main.py:30(is_duplicate)
 18339876    3.786    0.000    3.786    0.000 {method 'lower' of 'str' objects}
     2474    0.003    0.000    0.003    0.000 {method 'pop' of 'list' objects}
        1    0.000    0.000    0.000    0.000 main.py:24(read_file)
        1    0.000    0.000    0.000    0.000 {method 'splitlines' of 'str'objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 /usr/local/lib/python3.6/codecs.py:318(decode)
        1    0.000    0.000    0.000    0.000 /usr/local/lib/python3.6/_bootlocale.py:23(getpreferredencoding)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 /usr/local/lib/python3.6/codecs.py:308(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _locale.nl_langinfo}
        1    0.000    0.000    0.000    0.000 /usr/local/lib/python3.6/codecs.py:259(__init__)
        2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

After Profiling  
```
['addy', 'joni']
         4964 function calls in 0.668 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.665    0.665    0.668    0.668 main.py:54(find_duplicates)
        1    0.001    0.001    0.002    0.002 main.py:57(<listcomp>)
     4947    0.001    0.000    0.001    0.000 {method 'lower' of 'str' objects}
        1    0.000    0.000    0.001    0.001 main.py:49(read_file)
        1    0.000    0.000    0.000    0.000 {method 'splitlines' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 /usr/local/lib/python3.6/codecs.py:318(decode)
        1    0.000    0.000    0.000    0.000 /usr/local/lib/python3.6/_bootlocale.py:23(getpreferredencoding)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 /usr/local/lib/python3.6/codecs.py:308(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _locale.nl_langinfo}
        2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 /usr/local/lib/python3.6/codecs.py:259(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```