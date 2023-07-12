#include <stdint.h>

uint64_t test (uint64_t rs) {
  return rs & ~(1L << 20);
}

