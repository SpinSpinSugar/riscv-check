#include <stdint.h>

int test(int64_t rs) {
	return __builtin_popcount(rs);
}

