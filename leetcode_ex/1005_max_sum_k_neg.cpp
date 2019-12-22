//
//  1005_max_sum_k_neg.cpp
//  
//
//  Created by IncheolKim on 2019/11/13.
//

#include "1005_max_sum_k_neg.hpp"

class Solution {
public:
    int largestSumAfterKNegations(vector<int>& A, int K) {
        priority_queue<int, vector<int>, greater<int>> q{A.begin(), A.end()};
        for (auto top{0}; K--; top = -1 * q.top(), q.pop(), q.push(top));
        for (; !q.empty(); ans += q.top(), q.pop());
        return ans;
    }
}


class Solution {
public:
    int largestSumAfterKNegations(vector<int>& A, int K) {
        priority_queue<int, vector<int>, greater<int>> q{A.begin(), A.end()};
        for (auto top{0}; K--; top = -1 * q.top(), q.pop(), q.push(top));
        for (; !q.empty(); ans += q.top(), q.pop());
        return ans;
    }
}
