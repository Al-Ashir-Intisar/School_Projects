#include <iostream>
#include <chrono>
#include <fstream>
#include <random>
using namespace std;

void merge(int arr[], int left, int middle, int right)
{
    int n1 = middle - left + 1;
    int n2 = right - middle;

    int L[n1], R[n2];

    for (int i = 0; i < n1; i++)
    {
        L[i] = arr[left + i];
    }
    for (int i = 0; i < n2; i++)
    {
        R[i] = arr[middle + 1 + i];
    }

    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void merge_sort_helper(int arr[], int left, int right)
{
    if (left < right)
    {
        int middle = left + (right - left) / 2;
        merge_sort_helper(arr, left, middle);
        merge_sort_helper(arr, middle + 1, right);
        merge(arr, left, middle, right);
    }
}

void merge_sort(int arr[], int n)
{
    merge_sort_helper(arr, 0, n - 1);
}

bool array_equals(int arr1[], int n1, int arr2[], int n2)
{
    // Helper function: takes two arrays, and returns true if they have the exact same items, otherwise returns false
    if (n1 != n2)
        return false;
    for (int i = 0; i < n1; i++)
    {
        if (arr1[i] != arr2[i])
        {
            return false;
        }
    }
    return true;
}

bool test(void (*func)(int *, int))
{
    bool pass = true;

    int test1[5] = {1, 10, 2, 3, 5};
    int test1_ans[5] = {1, 2, 3, 5, 10};
    func(test1, 5);
    if (!array_equals(test1, 5, test1_ans, 5))
    {
        cout << "Test 1 failed" << endl;
        pass = false;
    }

    int test2[0] = {}; // Empty array
    int test2_ans[0] = {};
    func(test2, 0);
    if (!array_equals(test2, 0, test2_ans, 0))
    {
        cout << "Test 2 failed" << endl;
        pass = false;
    }

    int test3[1] = {45}; // Array with one item
    int test3_ans[1] = {45};
    func(test3, 1);
    if (!array_equals(test3, 1, test3_ans, 1))
    {
        cout << "Test 3 failed" << endl;
        pass = false;
    }

    int test4[5] = {6, 4, 3, 2, 1}; // array with reverse order
    int test4_ans[5] = {1, 2, 3, 4, 6};
    func(test4, 5);
    if (!array_equals(test4, 5, test4_ans, 5))
    {
        cout << "Test 4 failed" << endl;
        pass = false;
    }

    int test5[10] = {6, 7, 8, 9, 10, 5, 4, 3, 2, 1}; // array half organized in opposite direction
    int test5_ans[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    func(test5, 10);
    if (!array_equals(test5, 10, test5_ans, 10))
    {
        cout << "Test 5 failed" << endl;
        pass = false;
    }

    int test6[7] = {0, 0, 0, 0, 0, 0, 0}; // array with all element the same
    int test6_ans[7] = {0, 0, 0, 0, 0, 0, 0};
    func(test6, 7);
    if (!array_equals(test6, 7, test6_ans, 7))
    {
        cout << "Test 6 failed" << endl;
        pass = false;
    }

    int test7[4] = {-6, 6, 3, -3};
    int test7_ans[4] = {-6, -3, 3, 6};
    func(test7, 4);
    if (!array_equals(test7, 4, test7_ans, 4))
    {
        cout << "Test 7 failed" << endl;
        pass = false;
    }

    int test8[2] = {11, 7};
    int test8_ans[2] = {7, 11};
    func(test8, 2);
    if (!array_equals(test8, 2, test8_ans, 2))
    {
        cout << "Test 8 failed" << endl;
        pass = false;
    }

    int test9[6] = {-5, -3, 0, 1, 4, 2};
    int test9_ans[6] = {-5, -3, 0, 1, 2, 4};
    func(test9, 6);
    if (!array_equals(test9, 6, test9_ans, 6))
    {
        cout << "Test 9 failed" << endl;
        pass = false;
    }

    int test10[8] = {10, -10, 10, 0, 5, -5, 0, 0};
    int test10_ans[8] = {-10, -5, 0, 0, 0, 5, 10, 10};
    func(test10, 8);
    if (!array_equals(test10, 8, test10_ans, 8))
    {
        cout << "Test 10 failed" << endl;
        pass = false;
    }

    if (pass)
    {
        cout << "All tests passed!" << endl;
    }
    return pass; // Returns true if all tests pass, otherwise returns false.
}

// Function to generate a random array of a given size
void generateRandomArray(int arr[], int size)
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> distribution(-1000, 1000); // Adjust the range as needed

    for (int i = 0; i < size; i++)
    {
        arr[i] = distribution(gen);
    }
}

// Function to conduct the timing experiment
void timingExperiment()
{
    ofstream outputFile("merge_sort_timing.csv");
    if (!outputFile.is_open())
    {
        cerr << "Failed to open the output file." << endl;
        return;
    }

    outputFile << "Array Size,Average Time (ms)\n";

    const int maxArraySize = 1000;
    const int numTrials = 1000;
    chrono::steady_clock::time_point start, end;
    double totalTime;

    for (int size = 0; size <= maxArraySize; size += 10)
    {
        totalTime = 0.0;
        for (int trial = 0; trial < numTrials; trial++)
        {
            int arr[size];
            generateRandomArray(arr, size);

            start = chrono::steady_clock::now();
            merge_sort(arr, size);
            end = chrono::steady_clock::now();

            totalTime += chrono::duration_cast<chrono::microseconds>(end - start).count() / 1000.0; // in milliseconds
        }

        double averageTime = totalTime / numTrials;
        outputFile << size << "," << averageTime << "\n";
    }

    outputFile.close();

    cout << "Timing experiment completed. Results saved to merge_sort_timing.csv." << endl;
}

int main()
{
    test(merge_sort);
    timingExperiment();

    return 0;
}
