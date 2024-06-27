#include <iostream>
#include <chrono>
#include <fstream>

using namespace std;
using namespace std::chrono;

int min_index(int arr[], int size)
{
    // helper function for sort
    // arguments: (nonempty) array of integers (arr), number of items in array (size)
    // returns: the index of the minimum value in the array

    int i = 0;
    for (int j = 1; j < size; j++)
    {
        if (arr[j] < arr[i])
            i = j;
    }
    return i;
}

void remove_by_index(int arr[], int i, int size)
{
    // helper function for sort
    // arguments: array of integers (arr), index (i), and the number of items in array (size)
    // state change: removes the index i item from the array;
    //	index i of the array is replaced with the value from index i+1,
    //	index i+1 of the array is replaced with the value from index i+2,
    //	and so on until we get to the end of the array.
    // returns: none

    for (int index = i + 1; index < size; index++)
        arr[index - 1] = arr[index];
    return;
}

void sort(int arr[], int size)
{
    // sort function
    // arguments: array of integers (arr), number of items in the array (size)
    // state change: values in arr are sorted to be in ascending order
    // returns: none

    int *temp_arr = new int[size]; // allocate space for temporary array with same size as arr
    int num_left = size;
    int i = 0;
    int index;
    int next_val;
    while (num_left > 0)
    {                                          // while there are still items in arr to sort
        index = min_index(arr, num_left);      // find the index of the minimum value
        next_val = arr[index];                 // store the minimum value
        remove_by_index(arr, index, num_left); // remove the minimum value
        temp_arr[i] = next_val;                // copy minimum value into next position in temporary array
        i++;
        num_left--;
    }
    for (int j = 0; j < size; j++)
    { // copy all items from the temporary array back into arr, this time in order.
        arr[j] = temp_arr[j];
    }
    delete[] temp_arr; // release memory allocated for temporary array
}

int *make_array(int size)
{
    // helper function for timing experiment
    // argument: an integer (size)
    // returns: an array with number of items given by size. Contains numbers 0,1,2,3,...,size-1

    int *array = new int[size];
    for (int i = 0; i < size; i++)
        array[i] = i;
    return array;
}

int time(int arr[], int size, void (*func)(int *, int))
{
    // helper function for timing experiment
    // arguments: array of integers (arr), number of items in array (size), pointer to a function that takes the array and size
    // calls the function (intended for sort) on the array and size, and returns the time taken by this function call (in nanoseconds)

    auto start = high_resolution_clock::now();
    func(arr, size);
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<nanoseconds>(stop - start);
    return duration.count();
}

int avg_time(int size, void (*func)(int *, int), int trials)
{
    // helper function for timing experiment
    // arguments: integer (size), function to time (intended for sort), integer for number of trials (trials)
    // times the function called on arrays of given size, averages over number of trials given by trials.

    int total_time = 0;
    for (int i = 0; i < trials; i++)
    {                                        // repeat for number of trials
        int *arr = make_array(size);         // make array to sort
        total_time += time(arr, size, func); // time call on array, add to total time
        delete[] arr;
    }

    return total_time / trials;
}

int main()
{
    // these variable determine what sizes of arrays we test, and the number of trials
    int max_size = 1000;
    int interval = 10;
    int num_trials = 1000;

    // results of timing are written to the file sort_runtimes.csv
    ofstream my_file;
    my_file.open("sort_runtimes.csv");
    my_file << "size, time\n"; // header for csv file: column names are size, time

    for (int size = 0; size < max_size; size += interval)
    {                                                // for each size
        int time = avg_time(size, sort, num_trials); // compute average time for function call on array of that size
        my_file << size << "," << time << "\n";      // write result to the csv file
        cout << "Time taken by function on array size " << size << ": "
             << time << " nanoseconds" << endl; // print the result as well
    }

    my_file.close();

    return 0;
}