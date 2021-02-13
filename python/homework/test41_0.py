class File:
    def __init__(self, filename = 'testing1.txt'):
        self.read_file = open(filename, 'r+')

    def __del__(self):
        self.read_file.close()
        del self.read_file