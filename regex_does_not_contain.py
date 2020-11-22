"""
this example uses a negative look ahead (?!.*typedef) to
find a string that doesn't contain another string.

it helped me to parse a structure. it makes regex to be
not greedy.
"""
import re
import os

os.system("clear")

code = """
typedef struct {
    code1;
} name1;
typedef struct {
    code2;
} name2;
"""

#print(code)
match = re.search("typedef struct(?!.*typedef)(.*)name2;", code, re.DOTALL)
if match:
    print(match.group(0))
else:
    print("none")

"""
the result is

typedef struct {
    code2;
} name2;
"""
