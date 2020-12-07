import collections
import struct

packed_struct = struct.pack("cccc", b"z", b"a", b"c", b"h")
unpacked_struct = struct.unpack("cccc", packed_struct)

FourLetters = collections.namedtuple("FourLetters", "first second third fourth")
my_name = FourLetters(*unpacked_struct)

print(my_name.first, my_name.second, my_name.third)

# b'z' b'a' b'c'
