#include <stdint.h>

int test() {
	volatile int32_t a = 0;
    return __builtin_clz(a);
}
