#include "TestSource.h"
#include <iostream>

void SayHello(string message) {
        if (message.empty()) {
                cout << "The input is empty" << endl;
        }
        else {
                cout << message << endl;
        }
}

int add(int a, int b) {
        return a + b;
}

int multipy(int a, int b)
{
	return a * b;
}
