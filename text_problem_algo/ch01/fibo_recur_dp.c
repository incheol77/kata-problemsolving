#include <stdio.h>
#include <string.h>
#include <time.h>

#define MAX 100000

int func_call_cnt = 0;
int dp[MAX];


//---------------------------//
// functions for measurement
int get_call_cnt()
{
    return ++func_call_cnt;
}

void reset_call_cnt()
{
    func_call_cnt = 0;
}

void init_dp()
{
    memset(dp, -1, sizeof(dp));
}

//---------------------------//
// fibonacci functions
int fibo_recur(int num)
{
    if (num == 1 || num == 2) {
        return 1;
    } else { 
        printf("fino_recur call_cnt = %d\n", get_call_cnt());
        return fibo_recur(num-1) + fibo_recur(num-2);
    }
}

int fibo_dp(int num)
{
    if (dp[num] != -1) {
        return dp[num];
    }
    if (num == 1 || num == 2) {
        return dp[num] = 1;
    } else {
        printf("fino_dp call_cnt = %d\n", get_call_cnt());
        return dp[num] = fibo_dp(num-1) + fibo_dp(num-2);
    }
}


//---------------------------//
// fibonacci functions
int main()
{
    clock_t start, end;
    double run_time;
    int input = 0;

    printf("Enter input : ");
    scanf("%d", &input);

    printf("----- fibo_recur -----\n");
    start = clock();
    int fibo = fibo_recur(input);
    end = clock();
    run_time = (double)(end - start);
    printf("fibonacci value = %d, run_time = %.1lf usec\n", fibo, run_time);

    reset_call_cnt();
    init_dp();
    printf("\n----- fibo_dp -----\n");
    start = clock();
    fibo = fibo_dp(input);
    end = clock();
    run_time = (double)(end - start);
    printf("fibonacci value = %d, run_time = %.1lf usec\n", fibo, run_time);


    return 0;
}
