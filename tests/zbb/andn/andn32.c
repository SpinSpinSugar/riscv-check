#include <stdint.h>

int32_t test(int32_t x, int32_t y) {
	int32_t res = x & (~y);
	return res;
}

