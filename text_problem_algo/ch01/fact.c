#include <stdio.h>
#include <time.h>

#define MAX 1000

long long memo[MAX][MAX];


int fact_recur(int n)
{
	if (n == 1 || n == 0) {
		return 1;
	}

	return n * fact_recur(n-1);
}

int main()
{
	int input = 10;
	time_t start, end;
	long long diff;

	start = clock();
	long long fact1 = fact_recur(input);
	end = clock();
	diff = end - start;

	printf("fact_recur : %lld, %lld msec\n", fact1, diff);


	return 0;
}
