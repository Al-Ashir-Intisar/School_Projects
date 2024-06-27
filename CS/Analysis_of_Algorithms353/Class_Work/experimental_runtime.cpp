// Credit: Used https://www.geeksforgeeks.org/measure-execution-time-function-cpp/ as a source for timing code

#include <chrono>
#include <iostream>
using namespace std;
using namespace std::chrono;

bool find(int arr[], int size, int target)
{
    for (int i = 0; i < size; i++)
    {
        if (arr[i] == target)
            return true;
    }
    return false;
}

int get_middle(int arr[], int size)
{
    int i = 0;
    int j;

    if (size % 2 == 0)
    {
        j = size;
    }

    if (size % 2 != 0)
    {
        j = size - 1;
    }

    while (i != j)
    {
        i += 1;
        j -= 1;
    }

    return arr[i];
}

int main()
{
    // Fill an array with 10000 random numbers
    int numbers[10000];
    for (int i = 0; i < 10000; i++)
    {
        numbers[i] = rand();
    }

    // Store time before function call
    auto start = high_resolution_clock::now();

    // Function call
    bool result = get_middle(numbers, 10000);

    // Store time after function call
    auto stop = high_resolution_clock::now();

    // Compute the time taken by the function, by subtracting the start time from the stop time
    auto duration = duration_cast<microseconds>(stop - start);

    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;

    return 0;
}