#include <iostream>

void shreeram(int n) {  // Change return type to void
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            std::cout << "Ram";
        }
        std::cout << std::endl;  // Correct use of std::endl
    }
}

int main() {
    shreeram(100);
    return 0;
}
