a = 2
b = 3
print('--Before Swap--')
print('a :'+str(a))
print('b :'+str(b))

# Method 1:
# temp = a
# a = b
# b = temp
# print('--After Swap--')
# print('a :'+str(a))
# print('b :'+str(b))

# Method 2:
# a = a + b
# b = a - b
# a = a - b
# print('--After Swap--')
# print('a :'+str(a))
# print('b :'+str(b))

# Method 3:
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print('--After Swap--')
# print('a :'+str(a))
# print('b :'+str(b))

# Method 4:
# a,b = b,a
# print('--After Swap--')
# print('a :'+str(a))
# print('b :'+str(b))

# Internal implementation for Method 4:
import dis
def swap():
    a = 2
    b = 3
    a, b = b, a
dis.dis(swap)
# Output of method 4 will be below:
# 2           0 LOAD_CONST    1 (2)    # Push 2 onto stack
#             2 STORE_FAST    0 (a)    # Store in 'a'

# 3           4 LOAD_CONST    2 (3)    # Push 3 onto stack
#             6 STORE_FAST    1 (b)    # Store in 'b'

# 4           8 LOAD_FAST     1 (b)    # Load b (3)
#            10 LOAD_FAST     0 (a)    # Load a (2)
#            12 ROT_TWO                # Swap top two stack items
#            14 STORE_FAST    0 (a)    # Store into a
#            16 STORE_FAST    1 (b)    # Store into b