// SourceCodeLibrary.cpp : Defines the exported functions for the DLL application.
//

#include "SourceCodeLibrary.h"
#include <iostream>

void SayHello(string message) {
	if (message.empty()) {
		cout << "The input is empty" << endl;
	}
	else {
		cout << message << endl;
	}
}

