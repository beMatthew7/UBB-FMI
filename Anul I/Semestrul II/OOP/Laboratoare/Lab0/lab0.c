#include <stdio.h>

int main() {
	int n, sum = 0, nr;

	scanf("%d", &n);

	while(n > 0){
		scanf("%d", &nr);
		sum += nr;
		n--;

	}
	printf("Suma numerelor este: %d", sum);

	return 0;
}