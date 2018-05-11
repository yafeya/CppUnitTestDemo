#include <gtest/gtest.h>
#include <TestSource.h>

namespace TestDemo
{
	TEST(NORMAL_MESSAGE_TEST, SAY_HELLO_TEST) {
		ASSERT_NO_THROW(SayHello(""));
	}

	TEST(EQ_CONDITION, ADD_EQ_TEST) {
		ASSERT_EQ(add(1, 2), 3);
	}
}
