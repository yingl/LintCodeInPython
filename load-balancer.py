import random

class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.di = {}
        self.servers = []
        self.n = 0

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        self.di[server_id] = self.n
        self.servers.append(server_id)
        self.n += 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        i = self.di[server_id]
        if i != (self.n - 1):
            last_server_id = self.servers[-1]
            self.servers[i] = last_server_id
            self.di[last_server_id] = i
        del self.di[server_id]
        self.servers.pop()
        self.n -= 1

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        return self.servers[random.randint(0, len(self.servers) - 1)]
