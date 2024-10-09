#include <iostream>
using namespace std;

int main () {
    int a;
    cout << "Enter Your Marks: ";
    cin >> a;
    
    
    if(a>=90){
        cout <<"Grade is A";
    }else if(a>=80 && a<=90){
        cout <<"Grade is B";
    }else {
        cout <<"Grade is C";
        
    }
    return 0;
}
