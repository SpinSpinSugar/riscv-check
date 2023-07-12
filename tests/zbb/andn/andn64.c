#include <stdint.h>

int64_t test(int64_t x, int64_t y) {
	int64_t res = x & (~y);
	return res;
}

