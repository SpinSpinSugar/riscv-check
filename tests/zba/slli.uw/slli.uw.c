#include <stdint.h>

/*
Below implemetation is correct:
        sllw    a0, a0, a1
        zext.w  a0, a0
        ret
see bitmanip 2.41.slli.uw Architecture Explanation
it's equivalent to slli.uw
*/

uint64_t test(int64_t rs1, int shamt) {
    uint32_t word = rs1;
    uint64_t res = word << shamt;
    return res;
}

