# hippoeug@hippoeug-MacBook-Pro Desktop % uncompyle6 arecibo.cpython-37.pyc 
# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.11.6 (main, Oct  2 2023, 13:45:54) [Clang 15.0.0 (clang-1500.0.40.1)]
# Embedded file name: .\arecibo.py
# Compiled at: 2021-08-22 20:30:09
# Size of source mod 2**32: 937 bytes

# Workflow:
# 1. The user inputs a binary string.
# 2. This string is converted to hexadecimal (uranus).
# 3. It's then encoded to bytes, the bytes are reversed, and it's decoded back to a string (saturn).
# 4. The string is reversed (jupiter).
# 5. Finally, the reversed string is compressed and encoded in base64 format (neptune).

# Purpose:
# The script appears to be a form of data encoding or obfuscation tool. 
# It takes a binary input, performs several transformations (format conversion, reversal, compression, and encoding), 
# and outputs a base64-encoded string that is compressed and highly obfuscated compared to the original input. 
# This could be used for a variety of purposes, including making the data harder to read without the decoding process or simply compacting the data for storage or transmission.


import array, base64, zlib

def main():
    earth = input("Enter the message:")
    print(jupiter(neptune(saturn(uranus(earth)))))

# Converts the input cordelia (a binary string, judging by how it's used) into hexadecimal format.
def uranus(cordelia):
    ophelia = f"{int(cordelia, 2):X}"
    return ophelia

# This function checks if the input titan is a string. If it is, it encodes the string into bytes.
# It then creates an array of type "H" (unsigned short, 2 bytes) from the bytes, reverses the array, and converts it back to bytes.
# If the input was initially a string, it decodes the bytes back into a string before returning them; otherwise, it returns the bytes as they are.
def saturn(titan):
    mimas = True
    if isinstance(titan, str):
        mimas = True
        titan = titan.encode()
    enceladus = array.array("H", titan)
    enceladus.reverse()
    tethys = enceladus.tobytes()
    if mimas:
        return tethys.decode()
    return tethys

# Decodes the input bytes europa into a UTF-8 string.
# It then reverses the string character by character and returns the reversed string.
def jupiter(europa):
    metis = europa.decode("utf-8")
    adrastea = len(metis)
    amalthea = ""
    for io in range(adrastea):
        amalthea += metis[adrastea - io - 1]

    return amalthea

# Encodes the input string naiad into bytes, compresses these bytes using zlib with a compression level of 9 (which is the highest level of compression), 
# and then encodes the compressed data into base64 format. This function returns the base64-encoded, compressed string.
def neptune(naiad):
    thalassa = str.encode(naiad)
    despina = base64.b64encode(zlib.compress(thalassa, 9))
    return despina


if __name__ == "__main__":
    # main()
    print("==Q0utZNHMev+LPB1KbUKEWLi5QhvFSp0GM1A/ZNKsvfZOVGMJup1t7dkdw57aorSXYTwYNWZF4D8SgS1ogBRJ9X2/Mx4k9wyrFxMECARk7jNrNe")
    # print(jupiter(b'eNrNj7kRACEMxFryw9k4xM/2X9JRBgo1SgS8D4FZWNYwTYXSroa75wdkd7t1puJMGVOZfvsKNZ/A1MG0pSFvhQ5iLWEKUbK1BPL+veMHNZtu0Q=='))
    # print(jupiter(neptune("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0F112124E10EC9308CDF777B5FFBDDD76DBB3FAEC610C63586DB367E9FECAFED6B6FB76DFD9013C21092306442F2FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF7F")))
    # print(jupiter(neptune(saturn("7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF24264309210C21390FD6DB76F6BEDAFEC9F7E36DB8635C610C6AE3FBB6DD7DDFB5F7B77DF8C30C90EE12421110FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"))))
    print(jupiter(neptune(saturn(uranus("11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111001001000010011001000011000010010010000100001100001000010011100100001111110101101101101101110110111101101011111011011010111111101100100111110111111000110110110110111000011000110101110001100001000011000110101011100011111110111011011011011101011111011101111110110101111101111011011101111101111110001100001100001100100100001110111000010010010000100001000100010000111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")))))
# okay decompiling arecibo.cpython-37.pyc