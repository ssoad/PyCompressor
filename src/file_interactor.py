import bitarray

class FileInteractor:

    def __init__(self):
        pass

    def read(self, path):
        with open(path, 'r') as f:
            data = f.read()
        return data
    
    def write(self, path, message):
        encoded_message = bitarray.bitarray(message[0])
        encoded_dictionary = bitarray.bitarray(message[1])

        output = open(path, "wb")
        output.write(encoded_message)
        output.write(encoded_dictionary)

        return encoded_message
        