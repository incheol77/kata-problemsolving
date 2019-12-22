#include <stdio.h>
#include <time.h>

#define MAX 20

int memo[MAX][MAX];

int combi(int n, int r)
{
	if (r == 0 || n == r) {
		return 1;
	}

	return combi(n-1, r-1) + combi(n-1, r);
}

int combi_recur(int n, int r) 
{
	if (memo[n][r] > 0) {
		return memo[n][r];
	}
	if (r == 0 || n == r) {
		return memo[n][r] = 1;
	}

	return memo[n][r] = combi_recur(n-1, r-1) + combi_recur(n-1, r);
}

int main() 
{
	time_t start, end;
	int diff_time;
	int n, r, res;

	printf("enter [n, r] : ");
	scanf("%d %d", &n, &r);

	start = clock();
	res = combi(n,r);
	end = clock();
	diff_time = end - start;
	printf("combi[%d, %d] = %d (%d msec)\n", n, r, res, diff_time);

	start = clock();
	res = combi_recur(n,r);
	end = clock();
	diff_time = end - start;
	printf("combi_recur[%d, %d] = %d (%d msec)\n", n, r, res, diff_time);

	return 0;
}
