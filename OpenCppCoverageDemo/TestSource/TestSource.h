#pragma once
#include <string>

using namespace std;

extern "C" {
	void SayHello(string message);

	int add(int a, int b);
}
