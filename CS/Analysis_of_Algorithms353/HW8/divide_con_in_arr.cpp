#include <iostream>
#include <vector>

using namespace std;

bool binarySearch(const vector<int>& arr, int target, int start, int end) {
    if (start > end) {
        return false; // Base case: target not found
    }

    int mid = (start + end) / 2; // Calculate the middle index

    if (arr[mid] == target) {
        return true; // Base case: target found at the middle index
    } else if (arr[mid] < target) {
        return binarySearch(arr, target, mid + 1, end); // Search in the right half
    } else {
        return binarySearch(arr, target, start, mid - 1); // Search in the left half
    }
}

// Wrapper function for the binary search algorithm
bool searchInSortedArray(const vector<int>& arr, int target) {
    return binarySearch(arr, target, 0, arr.size() - 1);
}

int main() {
    // Example usage:
    vector<int> sortedArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int targetItem = 6;

    if (searchInSortedArray(sortedArray, targetItem)) {
        cout << "Item found in the array." << endl;
    } else {
        cout << "Item not found in the array." << endl;
    }

    return 0;
}
