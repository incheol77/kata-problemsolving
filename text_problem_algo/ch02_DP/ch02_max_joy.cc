//
//  main.cpp
//  algo_ex_xcode
//
//  Created by IncheolKim on 2019/12/15.
//  Copyright © 2019 IncheolKim. All rights reserved.
//

//5 5
//1 2 2 1 5
//1 4 4 3 1
//2 1 1 1 2
//1 3 5 1 1
//1 5 1 2 2
//22

#include <cstdio>
#include <algorithm>
#include <time.h>

#define MAX 1001

using namespace std;

int map[MAX][MAX];
int memo[MAX][MAX];
int joy[MAX][MAX];
int from[MAX][MAX];
enum {LEFT, UP};

void print_map(int (*map)[MAX], int m, int n)
{
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("%2d ", map[i][j]);
        }
        printf("\n");
    }
}

int max_joy_recur(int m, int n)
{
    if (m == 0 && n == 0) {
        return map[0][0];
    }
    if (m == 0) {
        return max_joy_recur(0, n-1) + map[m][n];
    }
    if (n == 0) {
        return max_joy_recur(m-1, 0) + map[m][n];
    }
    return max(max_joy_recur(m-1, n), max_joy_recur(m, n-1)) + map[m][n];
}

int max_joy_memo(int m, int n)
{
    if (memo[m][n] != 0) {
        return memo[m][n];
    }
    if (m == 0 && n == 0) {
        return memo[0][0] = map[0][0];
    }
    if (m == 0) {
        return memo[m][n] = max_joy_recur(0, n-1) + map[m][n];
    }
    if (n == 0) {
        return memo[m][n] = max_joy_recur(m-1, 0) + map[m][n];
    }
    return memo[m][n] = max(max_joy_recur(m-1, n), max_joy_recur(m, n-1)) + map[m][n];
}

void max_joy_dp(int m, int n)
{
    joy[0][0] = map[0][0];
    
    for (int i = 1; i < m; i++) {
        joy[i][0] = joy[i-1][0] + map[i][0];
    }
    for (int j = 1; j < n; j++) {
        joy[0][j] = joy[0][j-1] + map[0][j];
    }
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            joy[i][j] = max(joy[i-1][j], joy[i][j-1]) + map[i][j];
        }
    }
}

void max_joy_dp_from(int m, int n)
{
    joy[0][0] = map[0][0];
    
    for (int i = 1; i < m; i++) {
        joy[i][0] = joy[i-1][0] + map[i][0];
        from[i][0] = UP;
    }
    for (int j = 1; j < n; j++) {
        joy[0][j] = joy[0][j-1] + map[0][j];
        from[0][j] = LEFT;
    }
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (joy[i-1][j] > joy[i][j-1]) {
                from[i][j] = UP;
            } else {
                from[i][j] = LEFT;
            }
            joy[i][j] = max(joy[i-1][j], joy[i][j-1]) + map[i][j];
        }
    }
}

void print_path(int m, int n)
{
    if (m == 0 && n == 0) {
        return;
    }
    printf("(%d %d) ", m, n);
    if (from[m][n] == UP) {
        print_path(m-1, n);
    } else {
        print_path(m, n-1);
    }
}


int main()
{
    clock_t start, end;
    double result;
    
    int row, col;
    freopen("/Users/ickim/dev/algo_ex/problem_algo/ch02_DP/data/input_joy.dat", "r", stdin);
    
    scanf("%d %d", &row, &col);
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            scanf("%d ", &map[i][j]);
        }
    }
    print_map(map, row, col);
    
    start = clock();
    printf("%d\n", max_joy_recur(row-1, col-1));
    end = clock();
    result = (double)(end - start);
    printf("time recur : %.2lf ms\n", result);
    
    start = clock();
    printf("%d\n", max_joy_memo(row-1, col-1));
    end = clock();
    result = (double)(end - start);
    printf("time memo : %.2lf ms\n", result);

    start = clock();
    max_joy_dp(row, col);
    printf("%d\n", joy[row-1][col-1]);
    end = clock();
    result = (double)(end - start);
    printf("time dp : %.2lf ms\n", result);
    
    max_joy_dp_from(row, col);
    print_map(joy, row, col);
    print_map(from, row, col);
    print_path(row-1, col-1);


    
    return 0;
}
