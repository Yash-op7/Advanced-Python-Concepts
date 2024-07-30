
#! 1. Any line cannot be more than 80 characters long, use auto formatter -> pip install black

#! 2. Naming Convention -> for variables and functions use snake_case, not camelCase or PascalCase, for constants use CAPITAL_SNAKE_CASE and put it at the top of the file below import statements
#!                      -> for classes and exceptinons(because they are built-in classes in python) use PascalCase example: class BaseClass:

#! 3. module names -> single word.py is preferred but multiple words can use snake_case also use lowercase only

#! 4. in OOPs first parameters of instance methods should be named `self`, first parameter of a @classmethod should be named `cls`

#! 5. Global functions/classes/code blocks should be seperated with 2 blank lines and any functions not in global scope should be seperated by one blank line

#! 6. All the imports at the top and in different lines, not `import os, sys` but `import os and import sys`
#!    But when important multiple things from a module you should doL `from os import path, start`
#!    Also avoid wildcard import statements: from os import *

#! 7. The only time imports aren't at the very top is when you have module docstring, which define whats inside the module using """ information """ \n \n import ...

#! 8. String always use only single quotations or only double quotation marks, just be consistent, but in docstrings you should always use """ """ not ''' '''

#! 9. Whitespaces use: 
#!  Correct: spam(ham[1], {eggs: 2})          ✅
#!  Incorrect: spam( ham[ 1 ], { eggs: 2 } )  ❌
#! foo =(0,) is ✅ but bar = (0, ) is ❌
#! when using +, - or = use spaces on both side, when using * and / dont use spaces on either side unless in (a+b) * (c-d)
#! func(name='bob', age=30) is ✅ but func(name = 'bob', age = 30) is ❌

#! 10. Inline Comments must have at least 2 spaces fromo the code and should always be same

#! 11. except a specific exception and if you need to except multiple exceptions then do multiple specific exeption blocks

#! 12. use foo.startswith("pre") and .endswith() methods for checking prefixes and suffixes of strings instead of slicing