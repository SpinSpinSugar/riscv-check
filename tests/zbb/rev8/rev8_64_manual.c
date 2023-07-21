#include <stdint.h>

uint64_t test(uint64_t rs) {
    uint8_t tmp = 0;
    uint64_t res = 0;
    for (int i = 0; i < 8; ++i) {
        tmp = rs >> (i * 8);
        uint64_t new_byte = ((uint64_t) tmp) << ((7 - i) * 8);
        res |= new_byte;
    }

    return res;
}

