#include <stdint.h>

int64_t test(int64_t rs1, int64_t rs2) {
    int64_t result = rs2 + (rs1 << 3);
    return result;
}

