import numpy as np
import hashlib
def hashKeyInt(input_string):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    # Update the hash object with the input string
    sha256_hash.update(input_string.encode('utf-8'))
    # Get the hexadecimal representation of the hash (64 character long)
    hash_key = sha256_hash.hexdigest()
    # Convert the hash portion to an integer
    hash_integer = int(hash_key, 16)
    return hash_integer

def Hash0to1(HashInt, target_range=(0, 1)):
    # Convert muFloat to float number betwee 0 - 1
    # Largest 77 digit number ==> 10**78-1
    hash_float = HashInt / (10**78-1)
    return hash_float

def muFloatRange(hashFloat, target_range=(3.5699456, 4.0)):
    # hashFloat = Hash0to1(hashInt)
    mapped_float = (target_range[1] - target_range[0]) * hashFloat + target_range[0]
    return mapped_float

def xFloatrange(hashFloat, target_range=(0, 1)):    
    return Hash0to1(hashFloat)

# K should be >= 2; choosing 2-9 limit arbitrarily.
def kFloatRange(hash_0to1, target_range =(2,9)):
    # hash_float = x0 / float(target_range[1])
    mapped_float = (target_range[1] - target_range[0]) * hash_0to1 + target_range[0]
    return mapped_float

def convert2Int(floatVal):
    #accurate to 10 digits after decimal.
    floatVal=floatVal*1E10
    return int(round(floatVal,0))

def convertBack(intVal):
    return float(intVal/1E10)