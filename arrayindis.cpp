#include <iostream>
using namespace std;

// Global variables
const int size = 9;
int arr[size];

// Function for inserting elements into the array
void arrayInsert() {
    cout << "Enter " << size << " elements: ";
    for (int i = 0; i < size; i++) { // Use 0-based indexing
        cin >> arr[i];
    }
}

// Function for displaying elements of the array
void display() {
    cout << "These are the inserted elements: ";
    for (int i = 0; i < size; i++) { // Use 0-based indexing
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int choice;

    // Ask user for a choice
    cout << "Enter 1 to insert elements, 2 to display elements: ";
    cin >> choice;

    if (choice == 1) {
        arrayInsert();
    } else if (choice == 2) { // Fixed else-if syntax
        display();
    } else {
        cout << "No options available" << endl; // Fixed missing semicolon
    }

    return 0;
}
#include <iostream>
using namespace std;

// Global variables
const int size = 9;
int arr[size];

// Function for inserting elements into the array
void arrayInsert() {
    cout << "Enter " << size << " elements: ";
    for (int i = 0; i < size; i++) { // Use 0-based indexing
        cin >> arr[i];
    }
}

// Function for displaying elements of the array
void display() {
    cout << "These are the inserted elements: ";
    for (int i = 0; i < size; i++) { // Use 0-based indexing
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int choice;

    // Ask user for a choice
    cout << "Enter 1 to insert elements, 2 to display elements: ";
    cin >> choice;

    if (choice == 1) {
        arrayInsert();
    } else if (choice == 2) { // Fixed else-if syntax
        display();
    } else {
        cout << "No options available" << endl; // Fixed missing semicolon
    }

    return 0;
}
