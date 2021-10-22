import sys
from file_interactor import FileInteractor
from encoder import Encoder

def main(*argv):
    interactor = FileInteractor()
    message = interactor.read("message/notcoded.txt")

    enc = Encoder()
    compressed_message = enc.encode(message)
    
    message_before = interactor.write("message/encoded.txt", compressed_message)

main(sys.argv)

# *args - you can give to your method any number of arguments including 0
# **kwargs