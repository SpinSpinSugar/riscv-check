#include <stdint.h>

int64_t test(int64_t rs) {
	return __builtin_ctzl(rs);
}

