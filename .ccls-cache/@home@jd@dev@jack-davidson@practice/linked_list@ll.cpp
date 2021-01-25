#include <iostream>

/*
 * Singly linked list that stores integers.
 *
 */

typedef struct node {
	int val;
	struct node *next;
} node_t;

/* create a node from node_t struct */
node_t node(int val, node_t *next)
{
	node_t node = {
		.val = val,
		.next = next,
	};
	return node;
}

int main()
{
	node_t root = node(32, NULL); /* create root node */
	node_t child_1 = node(root.val * 2, NULL); /* create second node */
	root.next = &child_1; /* set root's pointer node to second node */

	std::cout << root.val << "\n";
	std::cout << root.next->val << "\n";
	return 0;
}
