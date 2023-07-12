#include <stdint.h>

int32_t test(int32_t rs1, int32_t rs2) {
    int32_t result = rs2 + (rs1 << 3);
    return result;
}

