from collections import defaultdict, deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        # Step 1: Calculate out-degrees and build the reversed graph.
        out_degree = [0] * n
        reversed_graph = defaultdict(list)
        for i in range(n):
            out_degree[i] = len(graph[i])
            for neighbor in graph[i]:
                # For an edge i -> neighbor, add a reverse edge neighbor -> i
                reversed_graph[neighbor].append(i)
        
        # Step 2: Initialize a queue with all terminal nodes (out_degree == 0).
        dq = deque()
        for i in range(n):
            if out_degree[i] == 0:
                dq.append(i)
                
        safe_nodes = []
        
        # Step 3: Process the queue.
        while dq:
            # This node is confirmed to be safe.
            node = dq.popleft()
            safe_nodes.append(node)
            
            # Check all nodes that point to this safe node.
            for prev_node in reversed_graph[node]:
                # Decrement the out-degree of the parent node.
                out_degree[prev_node] -= 1
                # If the parent node now has no outgoing paths to "unsafe" nodes, it becomes safe.
                if out_degree[prev_node] == 0:
                    dq.append(prev_node)
                    
        # Step 4: Sort the result in ascending order.
        safe_nodes.sort()
        return safe_nodes
