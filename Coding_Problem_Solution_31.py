# asked by AMAZON

# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding.
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
# You can assume the string to be decoded is valid.



def encoding(string):
    if not string:
        return ""
    coding=[]
    code=string[0]
    for char in string[1:]:
        if char!=code[-1]:
            coding.append(str(len(code))+code[-1])
            code=char
        else:
            code+=char

    if code:
        coding.append(str(len(code))+code[-1])

    return ''.join(coding)

def decoding(code):
    if not code:
        return ""

    decoding=[]
    while code:
        to_decode=code[:2]
        string=to_decode[1]*int(to_decode[0])
        decoding.append(string)
        code=code[2:] if len(code)>2 else []
    return ''.join(decoding)

def main():
    string=input("enter the string to be encoded:")
    print("encoding is: {0}".format(encoding(string)))

    code=input("enter the coded string: ")
    print("decoding of string is: {0}".format(decoding(code)))

if __name__=='__main__':
    main()
