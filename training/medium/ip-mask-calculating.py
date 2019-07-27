import sys
import math

def groupby(arr, s=8):
    while len(arr) > 0:
        yield [str(x) for x in arr[:8]]
        arr = arr[8:]

def binary_to_ip(binary_ip):
    ip = []
    for g in groupby(binary_ip):
        decimal = int("".join(g), 2)
        ip.append( str(decimal) )
    return ".".join(ip)


def ip_to_binary(ip):
    chunk = [int(x) for x in ip.split(".")]
    binary_ip = ["{0:08b}".format(x) for x in chunk]
    binary_array = [int(y) for x in binary_ip for y in x]
    return binary_array
  
def mask_to_binary(mask):
    mask = int(mask)
    binary_mask = [1] * mask + [0] * (32 - mask)
    return binary_mask 

ip, mask = input().split("/")

binary_ip = ip_to_binary(ip)
binary_mask = mask_to_binary(mask)

print(binary_ip, file=sys.stderr)
print(binary_mask, file=sys.stderr)

# "network address"
network_binary = [value * mask for value, mask in zip(binary_ip, binary_mask)]
broadcast_binary = [value if mask == 1 else 1 for value, mask in zip(binary_ip, binary_mask)]

print(network_binary, file=sys.stderr)
print(broadcast_binary, file=sys.stderr)

network_address = binary_to_ip(network_binary)
broadcast_address = binary_to_ip(broadcast_binary)

print(network_address)
print(broadcast_address)



