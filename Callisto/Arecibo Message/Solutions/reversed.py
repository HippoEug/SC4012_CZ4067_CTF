import base64, zlib, array

def full_decode(earth):
    # answer = jupiter(neptune(earth))
    answer = jupiter(neptune(saturn(earth)))
    # answer = print(jupiter(neptune(saturn(uranus(earth)))))
    print("\nFINAL OUTPUT!", answer)

def uranus(cordelia):
    ophelia = f"{int(cordelia, 2):X}"
    print("checking uranus; got ophelia:", ophelia)
    return ophelia

def reverse_uranus(encoded_message):
    # Convert the hexadecimal string to an integer
    binary_string = int(encoded_message, 16)
    # Convert the integer to a binary string
    original_cordelia = bin(binary_string)[2:]
    print("decoded uranus; got cordelia:", original_cordelia)

def saturn(titan):
    mimas = True
    if isinstance(titan, str):
        mimas = True
        titan = titan.encode()
    enceladus = array.array("H", titan)
    enceladus.reverse()
    tethys = enceladus.tobytes()
    if mimas:
        print("checking saturn (1); got tethys:", tethys)
        return tethys.decode()
    print("checking saturn (2); got tethys:", tethys)
    return tethys

def reverse_saturn(encoded_message):
    # Convert the string to bytes
    titan = encoded_message.encode()
    # Create an array of unsigned short integers from the bytes
    enceladus = array.array("H", titan)
    # Reverse the array
    enceladus.reverse()
    # Convert the array back to bytes
    original_titan = enceladus.tobytes()
    # Decode the bytes to obtain the original string
    original_message = original_titan.decode()
    print("decoded saturn; got titan:", original_message)

def neptune(naiad):
    thalassa = str.encode(naiad)
    despina = base64.b64encode(zlib.compress(thalassa, 9))

    print("checking neptune; got despina:", despina)
    return despina

def reverse_neptune(encoded_message):
    # Decode the base64-encoded, compressed string
    compressed_data = base64.b64decode(encoded_message)
    # Decompress the data using zlib
    decompressed_data = zlib.decompress(compressed_data)
    # Convert the decompressed data to a string
    original_message = decompressed_data.decode("utf-8")
    print("decoded neptune; got despina:", original_message)

def jupiter(europa):
    metis = europa.decode("utf-8")
    adrastea = len(metis)
    amalthea = ""
    for io in range(adrastea):
        amalthea = amalthea + metis[adrastea - io - 1]

    print("checking jupiter; got amalthea:", amalthea)
    return amalthea

def reverse_jupiter(encoded_message):
    # Reverse the characters in the string
    reversed_amalthea = encoded_message[::-1]
    # Convert from UTF-8 encoding to obtain the original 'metis' string
    original_metis = reversed_amalthea.encode("utf-8")
    print("decoded jupiter; got metis:", original_metis)


print("\n")
amalthea = "==Q0utZNHMev+LPB1KbUKEWLi5QhvFSp0GM1A/ZNKsvfZOVGMJup1t7dkdw57aorSXYTwYNWZF4D8SgS1ogBRJ9X2/Mx4k9wyrFxMECARk7jNrNe"
reverse_jupiter(amalthea)
europa = b'eNrNj7kRACEMxFryw9k4xM/2X9JRBgo1SgS8D4FZWNYwTYXSroa75wdkd7t1puJMGVOZfvsKNZ/A1MG0pSFvhQ5iLWEKUbK1BPL+veMHNZtu0Q=='
jupiter(europa)

print("\n")
reverse_neptune(europa)
naiad = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0F112124E10EC9308CDF777B5FFBDDD76DBB3FAEC610C63586DB367E9FECAFED6B6FB76DFD9013C21092306442F2FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF7F"
neptune(naiad)

print("\n")
reverse_saturn(naiad)
titan = "7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF24264309210C21390FD6DB76F6BEDAFEC9F7E36DB8635C610C6AE3FBB6DD7DDFB5F7B77DF8C30C90EE12421110FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
saturn(titan)

print("\n")
reverse_uranus(titan)
