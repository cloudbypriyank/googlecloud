
#include <iostream>
using namespace std;





int main() {
    int arr[] = {1,2,3,4,5,6,7,8,9,10};
    int size = 9;
    
    
    
    for(int i = 9;i<=size;i--){
        cout <<  arr[i]  << endl;
        if(i == 0){
            break;
        }
    }
    
 return 0;
}
