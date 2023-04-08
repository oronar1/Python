import re

def parse_bytes(input):
    bytes_ptr=re.compile(r'\b[01]{8}\b')
    result = bytes_ptr.findall(input)
    return result
