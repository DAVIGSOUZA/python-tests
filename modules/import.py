# import statements
import export
# usage
export.add(1,2)
export.sub(2,1)

# import with a alias
import export as alias
alias.add(1,2)

# import a specific piece of code
from export import add
print(add(10,20))

# import everything from a module
from export import *
print(add(20,30))
print(sub(100,60))




