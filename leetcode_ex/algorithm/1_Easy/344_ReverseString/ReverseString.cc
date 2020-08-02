#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
	void reverseString(string& str) {
		for (int i = 0; i < str.length()/2; i++) {
			char temp = str[i];
			str[i] = str[str.length()-1-i];
			str[str.length()-1-i] = temp;
		}
	}
};

int main() {
	string input = "hello";
	cout << input << endl;
	
	Solution sol;
	sol.reverseString(input);
	cout << input << endl;

	return 0;
}


