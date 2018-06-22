#include <gtest/gtest.h>
#include <TestSource.h>

namespace TestDemo
{
	TEST(EQ_CONDITION_TEST, MULTIPY_EQ_TEST) {
		ASSERT_EQ(multipy(1, 2), 2);
	}

	TEST(NAGTIVE_CONDITION, MULTIPY_NAGTIVE_TEST) {
		ASSERT_EQ(multipy(10, -2), -20);
	}

	TEST(ZERO_CONDITION, MULTIPY_ZERO_TEST) {
		ASSERT_EQ(multipy(1024, 0), 0);
	}
}
