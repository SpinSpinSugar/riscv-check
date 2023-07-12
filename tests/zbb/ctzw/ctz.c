#include <stdint.h>

int test(int32_t rs) {
	return __builtin_ctz(rs);
}

