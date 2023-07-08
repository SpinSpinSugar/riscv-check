#ifndef XLEN
#define XLEN 64
#endif

int test(int rs1, int shamt) {
	int index = shamt & (XLEN - 1);
	int rd = rs1 ^ (1 << index);
	return rd;
}
