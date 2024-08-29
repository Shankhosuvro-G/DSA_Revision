class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print("Graph_dict",self.graph_dict)
    def get_paths(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths=self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths
    # DFS approach
    def shortest_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []
        shortest_paths=None
        for node in self.graph_dict[start]:
            if node not in path:
                sp=self.shortest_path(node,end,path)
                if sp:
                    if shortest_paths is None or len(sp) < len(shortest_paths):
                        shortest_paths=sp
        return shortest_paths
    # BFS approach
    def shortestpath(self,edges,n,m,src):
        from collections import defaultdict
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=set([src])
        queue=[src]
        distances=[-1]*n
        current_distance=0
        while queue:
            next_queue=[]
            for node in queue:
                distances[node]=current_distance
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        next_queue.append(neighbour)
                        visited.add(neighbour)
            queue=next_queue
            current_distance+=1
        return distances


    




if __name__=="__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    route_graph=Graph(routes)
    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print(f"Shortest path between: {start} and {end}: ",route_graph.shortest_path(start,end))