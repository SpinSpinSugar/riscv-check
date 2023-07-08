// TODO

int test(int x, int y) {
	for (int i = 6; i < 64; ++i) {
		y &= ~(1 << i);
	}
	int shamt = y;
	
	int result = (x >> shamt) | (x << (64 - shamt));
	
	return result;
}

