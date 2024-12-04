#include <iostream>
#include <climits>
using namespace std;

int main() {
    int marks[] = {1, 100, 50, 48, -1, 76, 954, 9, 90, 10};
    int size = 10;
    int smallest = INT_MAX;
    int longest = INT_MIN;
    
    for(int i=0;i<=size;i++){
            smallest = min(marks[i], smallest);
            longest = max(marks[i], longest);
        }
    
    cout << "smalest value=" << smallest;
    cout << "longest value=" << longest;
    return 0;
}
