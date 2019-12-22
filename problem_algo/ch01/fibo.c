#include <stdio.h>
#include <time.h>

#define MAX 1000

long long memo[MAX];


long long fibo(int n)
{
	if (n == 0 || n == 1) {
		return 1;
	}

	return fibo(n-1) + fibo(n-2);
}

long long fibo_dp(int n)
{
	if (memo[n] > 0) {
		return memo[n];
	}

	if (n == 0 || n == 1) {
		return memo[n] = 1;
	}
	return memo[n] = fibo_dp(n-1) + fibo_dp(n-2);
}


int main() {
	int n;
	long long res;
	time_t start1, end1;
	time_t start2, end2;
	double diff1, diff2;
	
	printf("Enter n : ");
	scanf("%d", &n);

	start1 = clock();
	res = fibo(n);
	end1 = clock();
	diff1= end1- start1;
	printf("n = %d, fibo = %lld (%f sec)\n", n, res, diff1);

	start2 = clock();
	res = fibo_dp(n);
	end2 = clock();
	diff2 = end2 - start2;
	printf("n = %d, fibo_dp = %lld (%f sec)\n", n, res, diff2);
	return 0;
}
