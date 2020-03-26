//
//  main.cpp
//  algo_ex_xcode
//
//  Created by IncheolKim on 2019/12/15.
//  Copyright © 2019 IncheolKim. All rights reserved.
//

// True
//7 7
//2 5 1 6 1 4 1
//6 1 1 2 2 9 3
//7 2 3 2 1 3 1
//1 1 3 1 7 1 2
//4 1 2 3 4 1 2
//3 3 1 2 3 4 1
//1 5 2 9 4 7 0

// False
//7 7
//2 5 1 6 1 4 1
//6 1 1 2 2 9 3
//7 2 3 2 1 3 1
//1 1 3 1 7 1 2
//4 1 2 3 4 1 3
//3 3 1 2 3 4 1
//1 5 2 9 4 7 0

#include <iostream>
using namespace std;
const int MAX = 1000;

int board[MAX][MAX];
int cache[MAX][MAX];
int init_cache_value = -1;

void print_board(int (*map)[MAX], int row, int col)
{
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            cout << map[i][j] << ' ';
        }
        cout << endl;
    }
}

void init_cache()
{
    memset(cache, init_cache_value, sizeof(cache));
}


bool jump_recur(int size, int y, int x)
{
    if (y >= size || x >= size) {
        return false;
    } else if (y == size-1 && x == size-1) {
        return true;
    }
    int jump_size = board[y][x];
    return jump_recur(size, y + jump_size, x) ||
           jump_recur(size, y, x + jump_size);
}


int jump_memo(int size, int y, int x)
{
    if (y >= size || x >= size) {
        return 1;
    } else if (y == size-1 && x == size-1) {
        return 0;
    }
    int& ret = cache[y][x];
    if (ret != init_cache_value) {
        return ret;
    }
    int jump_size = board[y][x];
    return ret = (jump_memo(size, y + jump_size, x) ||
                  jump_memo(size, y, x + jump_size));
}

int main()
{
    int row, col;
    freopen("/Users/ickim/dev/algo_ex/algo_strategy/ch08_dp/input.dat", "r", stdin);
    setbuf(stdout, NULL);
    
    cin >> row >> col;
    cout << row << ' ' << col << endl;
    
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            cin >> board[i][j];
        }
    }
    
    print_board(board, row, col);
    cout << endl;
    init_cache();
    print_board(cache, row, col);
    cout << endl;
    
    cout << "jump_recur : " << jump_recur(row, 0, 0) << endl;
    cout << "jump_memo : " << jump_memo(row, 0, 0) << endl;

    
    return 0;
}
