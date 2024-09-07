class TestIsValid(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print(f'Setting up {cls.__name__}')

    ...

    	'''#Logic

	- To check if a string consisting of parentheses is balenced, we 
	need to start from the innermost nested parentheses and combine
	them, and continue like so outwards until we find a parentheses
	combination which cannot be combined due to mismatching brackets
	in which case we return False, or we combine every pair of 
	parentheses in which case we return True
    
	#Plan

	1. Initialize variables:
		- A stack variable of list[str] type to store the previously encountered
		open parentheses, i.e '(', '{' or '['
		- A helper lookup table, to quickly identify which closing parentheses
		matches which opening parentheses, closers: dict[str, str]

		Input - s = '({[]]())})'
		Output - stack: list[str] = [] and closers: dict[str, str] = {'(': ')', ...}

	2. Iterate over the string and for each bracket do the following:
		- if its an opening bracket, then simply push it to the stack
		- else its a closing bracket so:
			- check if the stack is empty, in which case return False, as this
			cannot find an opening parentheses to its left
			- if stack is non empty then top of the stack must be the opening
			matching parentheses for this closing parentheses:
			  - if it is then remove the top most element of the stack and continue
			to the next iteration
			  - else this closing parentheses cannot be matched with its appropriate
			opening parentheses, hence return False
		Input - s = '({[]]))})'
		Output - either return False or the result of the processed s in stack
		-> For this custom test case, output will be False (due to inmatched ']' at s[4])

	3. Finally check if the stack is empty, if it is then return True as we have
	successfully combined all the parentheses, else return False
	Input - stack
	Output - return len(stack) == 0
	'''