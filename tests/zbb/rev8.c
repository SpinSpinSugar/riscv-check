// TODO
// I don't know if it's working
int y[8];

int* test(int* x) {
	for (int i = 0; i < 8; ++i) {
		y[7-i] = x[i];
	}
	return y;
}

