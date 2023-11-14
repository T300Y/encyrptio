import main

assert main.arc_add(list("Vhfuhw phvvdjh"), 3) == "Secret message"


assert main.add(['a','b','c'],1) == 'bcd'
assert main.add(['a','b','c'],2) == 'cde'
assert main.add(['a','b','c'],3) == 'def'

assert main.reverse('abc') == 'cba'
assert main.reverse('abcd') =='dcba'

assert main.swap_pairs(['a','b','c','d']) == 'badc'
assert main.swap_pairs(['a','b','c','d','e']) == 'badce'

assert main.rotate_left(['a','b','c','d'],1) == 'bcda'
assert main.rotate_left(['a','b','c','d'],2) == 'cdab'

assert main.rotate_right(['a','b','c','d'],1) == 'dabc'
assert main.rotate_right(['a','b','c','d'],2) == 'cdab'

assert main.qwerty(['a','b','c','d']) == 'qwer'
assert main.qwerty(list("Secret message")) == 'Ltektz dtllqut'

