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

	TEST(NAGTIVE_CONDITION, ADD_NAGTIVE_TEST) {
                ASSERT_EQ(add(10, -2), 8);
        }

}
