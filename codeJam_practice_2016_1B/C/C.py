__author__ = 'pretymoon'

# import collections
matches = []
##############################
#This class represents a directed graph using adjacency matrix representation
class Graph:

    def __init__(self,graph):
        self.graph = graph # residual graph
        self. ROW = len(graph)
        #self.COL = len(gr[0])


    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
    def BFS(self,s, t, parent):

        # Mark all the vertices as not visited
        visited =[False]*(self.ROW)

        # Create a queue for BFS
        queue=[]

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            #Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices's of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False


    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)

        max_flow = 0 # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):
            print(parent)

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow +=  path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow
##############################

ff = open("\\Mahnaz\\PycharmProjects\\codeJam_practice_2016_1B\\C\\C-small.in", "r")
numOfCases = int(ff.readline())

for case in range(1, numOfCases+1):
    print("Case #{}: ".format(case), end='')

    strLine = ff.readline()
    n = int(strLine)
    w1_set = set([])
    w2_set = set([])
    topics = []
    for l in range(n):
        strLine = ff.readline()
        a = strLine.split(" ")
        w1, w2 = [x.strip() for x in a]
        topics.append((w1, w2))
        w1_set.add(w1)
        w2_set.add(w2)
    w1_list = list(w1_set)
    w2_list = list(w2_set)
    w_list = list(w1_set | w2_set)
    w_list.sort()
    v_size = len(w_list) + 2  # add source and sink to the vertices
    g = [[0 for i in range(v_size)] for j in range(v_size)]
    for i in range(len(w1_list)):
        g[0][w_list.index(w1_list[i]) + 1] = 1
    for i in range(len(w2_list)):
        g[w_list.index(w2_list[i]) + 1][-1] = 1
    for w1, w2 in topics:
        g[w_list.index(w1) + 1][w_list.index(w2) + 1] = 1

    print("---g---")
    print("s", w_list, "t")
    for t in g:
        print(t)

    print("---path---")
    my_graph = Graph(g)
    print(my_graph.FordFulkerson(0, len(g)-1))


    # orig = []
    # w1_cnt = collections.Counter()
    # w2_cnt = collections.Counter()
    # real_topic = []
    # for l in range(n):
    #     strLine = ff.readline()
    #     a = strLine.split(" ")
    #     w1, w2 = [x.strip() for x in a]
    #     orig.append((w1,w2))
    #     w1_cnt[w1] += 1
    #     w2_cnt[w2] += 1
    #
    # cnt = 0
    # print("\n--fake---")
    # for w1,w2 in orig:
    #     if w1_cnt[w1] > 1 and w2_cnt[w2] > 1:
    #         print(w1, w2)
    #         cnt += 1
    #         w1_cnt[w1] -= 1
    #         w2_cnt[w2] -= 1
    #     else:
    #         real_topic.append((w1,w2))
    #
    # print(cnt)
    # print("---real---")
    # print(real_topic)
    # print("---orig---")
    # for o in orig:
    #     print(o)