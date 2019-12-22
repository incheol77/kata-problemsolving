//
//  main.cpp
//  algo_ex_xcode
//
//  Created by IncheolKim on 2019/12/15.
//  Copyright © 2019 IncheolKim. All rights reserved.
//

//5 5
//1 1 1 1 1
//1 1 0 0 1
//1 1 1 1 1
//1 1 1 0 1
//0 0 1 1 1
//11

#include <cstdio>

#define MAX 1001

int map[MAX][MAX];
int path[MAX][MAX];

void print_map(int (*map)[MAX], int row, int col)
{
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            printf("%d ", map[i][j]);
        }
        printf("\n");
    }
}

int calc_path_recur(int m, int n)
{
    if (map[m][n] == 0) {
        return 0;
    }
    if (m == 0 && n == 0) {
        return 1;
    }
    return ((m > 0) ? calc_path_recur(m - 1, n) : 0)
         + ((n > 0) ? calc_path_recur(m, n - 1) : 0);
}

void calc_path_dp(int m, int n)
{
    path[0][0] = map[0][0];
    
    // 1. calc the first column on the left
    for (int i = 1; i < m; i++) {
        if (map[i][0] == 0) {
            path[i][0] = 0;
        } else {
            path[i][0] = path[i-1][0];
        }
    }
    
    // 2. calc the first row on the top
    for (int j = 1; j < n; j++) {
        if (map[0][j] == 0) {
            path[0][j] = 0;
        } else {
            path[0][j] = path[0][j-1];
        }
    }
    
    // 3. calc the rectangle in the inner path
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (map[i][j] == 0) {
                path[i][j] = 0;
            } else {
                path[i][j] = path[i-1][j] + path[i][j-1];
            }
        }
    }
}

int main()
{
    int row, col;
    freopen("/Users/ickim/dev/algo_ex/problem_algo/ch02_DP/data/input_path.dat", "r", stdin);
    
    scanf("%d %d", &row, &col);
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            scanf("%d ", &map[i][j]);
        }
    }
    print_map(map, row, col);
    printf("%d\n", calc_path_recur(row-1, col-1));
    printf("\n");
    calc_path_dp(row, col);
    print_map(path, row, col);
    printf("%d\n", path[row-1][col-1]);

    
    return 0;
}
