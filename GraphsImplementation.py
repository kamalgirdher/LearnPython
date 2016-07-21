class graphs:

    def __init__(self):
        self.nodelist = {}

    def addNodes(self, *nodes):
        for node in nodes:
            if node not in self.nodelist:
                self.nodelist[node] = {}

    def getNodes(self):
        return self.nodelist

    def deleteNodes(self, *nodes):
        for node in nodes:
            var = 'N'
            if node in self.nodelist:
                for knode in self.nodelist.keys():
                    if node in self.nodelist[knode].keys():
                        if var.upper() == 'Y':
                            del self.nodelist[knode][node]
                        else:
                            var = input(
                                'Node is connected. To delete type Y.')
                del self.nodelist[node]

    def addEdge(self, start, end, weight):
        if start not in self.nodelist:
            self.nodelist[start] = {}
        if end not in self.nodelist:
            self.nodelist[end] = {}
        if end not in self.nodelist[start].keys():
            self.nodelist[start][end] = weight
        else:
            var = input(
                'Already connected. Type Y to overwrite and N otherwise.')
            if var.upper() == 'Y':
                self.nodelist[start][end] = weight
            else:
                print ('Operation canceled.')

    def removeEdge(self, start, end):
        if end in self.nodelist[start].keys():
            del self.nodelist[start][end]

    def findpath(self, start, end, path=[]):
        path = path + [start]
        if start not in self.nodelist:
            return None
        if start == end:
            return path
        for node in self.nodelist[start].keys():
            if node not in path:
                newpath = self.findpath(node, end, path)
                if newpath:
                    return newpath
        return None

    def findshortestpath(self, start, end, path=[]):

        if start not in self.nodelist:
            return None

        path = path + [start]
        if start == end:
            return path

        shortestpath = None
        for node in self.nodelist[start].keys():
            if node not in path:
                newpath = self.findpath(node, end, path)
                if newpath:
                    if (not(shortestpath) or len(shortestpath) > len(newpath)):
                        shortestpath = newpath
        if shortestpath:
            return shortestpath
        return None
