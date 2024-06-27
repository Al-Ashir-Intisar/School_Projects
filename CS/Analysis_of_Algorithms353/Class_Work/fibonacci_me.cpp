#include <iostream>
using namespace std;

int fib(const int n){
    int x_0 = 0;
    int x_1 = 1;
    int start = 1;
    long fib = 0;

    if (n <= 1)
    {
        cout << n << "\n" << endl;
    }
    else{
        while(start < n){
        int fib = x_0 + x_1;
        cout << fib << "\n" << endl;
        x_0 = x_1;
        x_1 = fib;
        start++;

    }

    }
    
    return 0;
}

int main(){
    fib(0);
    fib(1);
    fib(10);
    return 0;
}