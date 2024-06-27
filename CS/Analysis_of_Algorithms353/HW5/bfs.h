#ifndef BFS
#define BFS

#include <iostream>
#include <queue>

#include "adjacency_list.h"

void bfs(AdjacencyList *graph, int start, int numNodes)
{
	// takes a pointer to the adjacency list of a graph, a starting node, and the total number of nodes
	// performs a breadth first traversal, printing each node as it is visited

	// WHEN YOU START WORKING ON THIS, DELETE OR COMMENT THE NEXT TWO LINES
	// std::cout << "bfs not implemented" << std::endl;
	// return;

	// track which nodes have been visited using an array of booleans
	bool *visited = new bool[numNodes];

	// to_visit tracks nodes that need to be explored, stored in a queue
	std::queue<int> to_visit;

	// WHAT SHOULD YOU DO HERE?
	// initialize visited array to false
	for (int i = 0; i < numNodes; i++)
	{
		visited[i] = false;
	}
	// enqueue the starting node
	to_visit.push(start);

	int current;

	// while there are still nodes to explore
	while (!to_visit.empty())
	{
		// WHAT SHOULD YOU DO HERE?
		// dequeue a node
		current = to_visit.front();
		to_visit.pop();

		if (!visited[current])
		{
			// WHAT SHOULD YOU DO HERE?
			// print the current node
			std::cout << current << " ";
			visited[current] = true;

			for (auto neighbor : *(graph->neighbors(current)))
			{ // for each neighbor of current (this is using an iterator through the neighbors of current, using the member function neighbors of AdjacencyList)
				// WHAT SHOULD YOU DO HERE?
				if (!visited[neighbor])
				{
					to_visit.push(neighbor);
				}
			}
		}
		std::cout << std::endl;
	}
}
#endif