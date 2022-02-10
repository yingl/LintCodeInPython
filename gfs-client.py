'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''


class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """
    def __init__(self, chunkSize):
        # do intialization if necessary
        self.chunkSize = chunkSize
        super(GFSClient,self).__init__()

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    def read(self, filename):
        # write your code here
        if filename + '-0' not in self.chunks:
            return None
        data = ''
        i = 0
        while True:
            d = self.readChunk(filename, i)
            if not d:
                break
            i += 1
            data += d
        return data

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    def write(self, filename, content):
        # write your code here
        if filename + '-0' in self.chunks:
            i = 0
            while True:
                f = filename + '-' + str(i)
                if f in self.chunks:
                    del self.chunks[f]
                    i += 1
                else:
                    break
        bytes = len(content)
        chunks = int(bytes / self.chunkSize)
        if (chunks * self.chunkSize) < bytes:
            chunks += 1
        for i in range(chunks):
            begin = i * self.chunkSize
            end = begin + self.chunkSize
            if end > bytes:
                end = bytes
            self.writeChunk(filename, i, content[begin:end])
