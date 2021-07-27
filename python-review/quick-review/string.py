# String
hello = 'hello'                         # String literals can use single quotes
world = "world"                         # or double quotes; it does not matter.
print(hello)                            # Prints hello
print(len(hello))                       # String length; Prints 5
hw = hello + ' ' + world                # String concatenation
print(hw)                               # Prints hello world
hw12 = '%s %s %d' % (hello, world, 12)  # sprintf style string formatting
print(hw12)                             # Prints hello world 12
hw13 = "제 이름은 %s입니다. 나이는 %d살 입니다." % ("ding-co", 27)
print(hw13)
hw14 = f"{hello} {world}, 14"
print(hw14)

s = "hello"
print(s.capitalize())                   # Capitalize a string; prints "Hello"
print(s.upper())                        # Convert a string to uppercase; Prints HELLO
print(s.rjust(7))                       # Right-justify a string, padding with spaces; Prints "  hello"
print(s.center(7))                      # Center a string, padding with spaces; Prints " hello "
print(s.replace('l', '(ell)'))          # Replace all instances of one substring with another;
                                        # Prints he(ell)(ell)o
print('  world '.strip())               # String leading and trailing whitespace; Prints world