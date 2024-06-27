//memoization 

#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

long long int slow_fibonacci(int n){
	// Takes an integer n, and returns the nth Fibonacci number, F_n

	if (n == 0)
		return 0;

	if (n == 1)
		return 1;

	return slow_fibonacci(n-1) + slow_fibonacci(n-2);
}

// this array is used for memoization
long long int memo[100];			


long long int memoization_fibonacci(int n){
	// Takes an integer n, and returns the nth Fibonacci number, F_n. Updates memo array so that memo[n] is F_n.

	if (memo[n] != -1){			// check if F_n has been computed before. If it has, return that value.
		return memo[n];
	}

	if (n == 0){
		memo[0] = 0;
		return 0;
	}

	if (n == 1){
		memo[1] = 1;
		return 1;
	}

	memo[n] = memoization_fibonacci(n-1) + memoization_fibonacci(n-2);
	return memo[n];
}

long long int tabulation_fibonacci(int n){
	// Takes an integer n, and returns the nth Fibonacci number, F_n.

	long long int results[100];

	results[0] = 0;
	results[1] = 1;

	for (int num = 2; num <= n; num++){
		results[num] = results[num-1] + results[num-2];
	}

	return results[n];
}


int main() {
	// test Fibonacci functions for increasing values of n

	bool time_slow = true;
	bool time_memo = false;
	bool time_tab = false;

	long long int result;
	for (int n = 0; n < 100; n++){
		if (time_slow){
			auto start = high_resolution_clock::now();
    		result = slow_fibonacci(n);
			auto stop = high_resolution_clock::now();

			auto duration = duration_cast<nanoseconds>(stop - start);
			cout << "Slow Fibonacci for n = " << n << " returns " << result << ", taking " <<  duration.count() << " nanoseconds.\n";
		}

		// set all entries of memoization to -1, starting with no computations performed
		for (int i = 0; i < 100; i++){
			memo[i] = -1;
		}

		if (time_memo){
			auto start = high_resolution_clock::now();
    		result = memoization_fibonacci(n);
			auto stop = high_resolution_clock::now();

			auto duration = duration_cast<nanoseconds>(stop - start);
			cout << "Memoization Fibonacci for n = " << n << " returns " << result << ", taking " <<  duration.count() << " nanoseconds.\n";
		}

		if (time_tab){
			auto start = high_resolution_clock::now();
    		result = tabulation_fibonacci(n);
			auto stop = high_resolution_clock::now();

			auto duration = duration_cast<nanoseconds>(stop - start);
			cout << "Tabulation Fibonacci for n = " << n << " returns " << result << ", taking " <<  duration.count() << " nanoseconds.\n";
		}

		cout << endl;
	}

    return 0;
}