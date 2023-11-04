"""
Flag            - Will mark a location
None            - Value doesn't exist or is null
is and is not   - is or is not a Type, Value or Identity
id              - Identity
"""

condition = False
flag = None

if condition:
    print('Print line 11')
    flag = True
else:
    print('Print line 13')

print(flag, flag is None)
print(flag, flag is not None)
