#include <iostream>

int main() {
    int n;
    std::cout << "Enter your choice :";
    std::cin >> n;
  
    
    if(n =1){
        int a;
        int b;
        std::cout <<"Enter a value :";
        std::cin >>a;
        std::cout <<"Enter b value :";
        std::cin >>b;
        std::cout <<"Answer is:" << a+b;
    }else {
        std::cout << "Your choice is incorrect";
    }


    return 0;
}
