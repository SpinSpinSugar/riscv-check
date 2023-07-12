#include <stdint.h>

uint64_t test (uint64_t rs) {
  return 1 & (rs >> 20);
}

