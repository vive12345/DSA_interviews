from typing import List
import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # prices[i] will store the minimum cost to reach city i from src.
        # Initialize all prices to infinity, except for the source city.
        prices = [float('inf')] * n
        prices[src] = 0
        
        # We can make at most k stops, which means we can take at most k + 1 flights.
        # We will relax the edges k + 1 times.
        for i in range(k + 1):
            # Use a temporary array to store the updated prices for the current iteration.
            # This is crucial because each iteration should only use costs from the previous one.
            temp_prices = prices[:]
            
            # For each flight, check if we can find a cheaper path.
            for u, v, p in flights:
                # If the source city 'u' of the flight is reachable (not infinity)
                if prices[u] != float('inf'):
                    # If the path through 'u' to 'v' is cheaper than any known path to 'v'
                    if prices[u] + p < temp_prices[v]:
                        temp_prices[v] = prices[u] + p
            
            # Update the main prices array for the next iteration.
            prices = temp_prices
            
        # If prices[dst] is still infinity, the destination is not reachable within k stops.
        if prices[dst] == float('inf'):
            return -1
        else:
            return int(prices[dst])