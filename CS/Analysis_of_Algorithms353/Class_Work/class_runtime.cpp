#include <chrono>
#include <iostream>
using namespace std;
using namespace std::chrono;

int min_index(int arr[], int size)
{

    int i = 0;

    for (int j = 0; j < (size - 1); j++)
    {
        if (arr[j] < arr[i])
        {
            i = j;
        }
    }
    return i;
}

int main()
{
    int n = 100000;
    // Fill an array with 10000 random numbers
    int numbers[100000];
    for (int i = 0; i < n; i++)
    {
        numbers[i] = i;
    }
    // Store time before function call
    auto start = steady_clock::now();

    // Function call
    int result = min_index(numbers, n);

    // Store time after function call
    auto stop = steady_clock::now();

    // Compute the time taken by the function, by subtracting the start time from the stop time
    auto duration = duration_cast<nanoseconds>(stop - start);

    std::cout << "Time taken by function min_index:  "
              << duration.count() << " nanoseconds" << endl;
    std::cout << result;

    return 0;
}