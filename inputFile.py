x = 1 # 1: comment
"""
2: comment
"""
'''
3: comment
'''
"4: not comment, even if ignored by compiler"
'5: not comment, even if ignored by compiler'
x = """6: not comment, because used as string value"""
x = \
\
"""
7: not comment, because used as string value
"""
"'''8: not comment''' because is part of string"
x = "9: # not comment because is part of string so we ignore the '#'"
"""
10: comment \
\"""
continues because the first '"' in the line above is escaped with backslash (\")
"""

"""
11: comment \
\ """
print("Hello")

#this is a comment, there is no exit when u comment \

y = \
\
\
\
\
\
\
\
"""not comment """