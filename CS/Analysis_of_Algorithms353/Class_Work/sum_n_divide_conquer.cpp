#include <iostream>
#include <vector>

using namespace std;

int divide_and_conquer_sum(const vector<int>& arr, int start, int end) {
    // Base case: If the array has only one element, return that element
    if (start == end) {
        return arr[start];
    }

    // Divide the array into two halves
    int mid = (start + end) / 2;

    // Recursively calculate the sum of the left and right halves
    int left_sum = divide_and_conquer_sum(arr, start, mid);
    int right_sum = divide_and_conquer_sum(arr, mid + 1, end);

    // Combine the results to get the total sum
    int total_sum = left_sum + right_sum;

    return total_sum;
}

int main() {
    // Example usage:
    vector<int> numbers = {1, 2, 3, 4, 5};
    int result = divide_and_conquer_sum(numbers, 0, numbers.size() - 1);
    
    cout << "Sum of the numbers: " << result << endl;

    return 0;
}
