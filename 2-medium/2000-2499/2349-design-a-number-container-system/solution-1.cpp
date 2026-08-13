#include <bits/stdc++.h>

using namespace std;

class NumberContainers {
public:
    NumberContainers() {
        
    }
    
    void change(int index, int number) {
        
        if (index_to_number.find(index) != index_to_number.end())
        {
            int num = index_to_number[index];
            number_to_index[num].erase(index);

            if (number_to_index[num].empty())
            {
                number_to_index.erase(num);
            }
        }

        index_to_number[index] = number;
        number_to_index[number].insert(index);
    }
    
    int find(int number) {
        if (number_to_index.find(number) != number_to_index.end())
        {
            return *number_to_index[number].begin();
        }

        return -1;
    }

private:
    unordered_map<int, int> index_to_number;
    unordered_map<int, set<int>> number_to_index;

};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */

int main() {
    cout << "Hello C++" << endl;
    return 0;
}