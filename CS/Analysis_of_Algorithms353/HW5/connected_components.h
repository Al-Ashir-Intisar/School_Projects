#ifndef CONNECTED_COMPONENTS
#define CONNECTED_COMPONENTS

#include <iostream>

#include "adjacency_list.h"

void connected_components(AdjacencyList *graph, int numNodes)
{
	// takes a pointer to the adjacency list of a graph and the total number of nodes
	// discovers the connected components, printing the nodes in each component, with line breaks in between the components.

	// WHEN YOU START WORKING ON THIS, DELETE OR COMMENT THE NEXT TWO LINES
	// std::cout << "connected_components not implemented" << std::endl;
	// return;

	// this is all up to you - reference the pseudocode from class to help, and you might also want to look back at the implementations for bfs and dfs

	// track which nodes have been visited using an array of booleans
	bool *visited = new bool[numNodes];

	// mark all nodes as not visited
	for (int i = 0; i < numNodes; i++)
	{
		visited[i] = false;
	}

	// for every node i in the graph
	for (int i = 0; i < numNodes; i++)
	{
		// if node i is not visited
		if (!visited[i])
		{
			// to_visit tracks nodes that need to be explored, stored in a queue
			std::queue<int> to_visit;
			// enqueue the starting node
			to_visit.push(i);

			int current;

			// while there are still nodes to explore
			while (!to_visit.empty())
			{
				// dequeue a node
				current = to_visit.front();
				to_visit.pop();

				if (!visited[current])
				{
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
			}
			std::cout << std::endl;
		}
	}
}

#endif