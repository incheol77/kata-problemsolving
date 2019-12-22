#include <stdio.h>

typedef struct _node {
	int key;
	struct _node *next;
} node_t;

node_t *head = NULL;
node_t *tail = NULL;

void insert_node(int n) 
{
	node_t *new_node = (node_t*)malloc(sizeof(node_t));
	if (!new_node) {
		printf("Fail to allocate memory for new_node!\n");
		return;
	}
	new_node->key = n;
	new_node->next = NULL;

	if (head == NULL) {
		head = new_node;
		tail = new_node;
	} else {
		tail->next = new_node;
		tail = new_node;
	}
}

int delete_node() 
{
	int res;
	node_t *del_node;

	if (head == NULL) {
		printf("Head is NULL!\n");
		return -1;
	}

	del_node = head;
	head = head->next;
	if (head == NULL) {
		tail = del_node;
	}

	res = del_node->key;
	del_node->next = NULL;
	free(del_node);

	return res;
}

void print_node()
{
	node_t *curr_node = head;

	if (head == NULL) {
		printf("Head is NULL!\n");
	}

	while (curr_node != NULL) {
		printf("%d ", curr_node->key);
		curr_node = curr_node->next;
	}
	printf("\n");
}

void print_node_recur(node_t *curr)
{
	if (curr == NULL) {
		printf("curr is NULL\n");
		return;
	}
	printf("%d ", curr->key);

	return print_node_recur(curr->next);
}

int main()
{
	for (int i = 1; i <= 5; i++) {
		insert_node(i);
		print_node();
	}

	print_node_recur(head);
}
