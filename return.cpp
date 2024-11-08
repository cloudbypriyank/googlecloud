// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

int add() {
    int a;
    int b;
    int sum;
    cout <<"enter number a \n ";
    cin >> a; 
    cout <<"enter number b \n ";
    cin >> b;
    
    sum = a+b;
    cout << "this is your addiition " << sum;
    return sum;
}
int main() {
    
    int a;
    char choice;
    cout << "enter your choice ";
    cin >> a;
    choice = a;
    
    {
        if(choice=1){
            return add();
            
        }
          
        else{
         cout <<"inccorrect";
    }
}
    return 0;
}
