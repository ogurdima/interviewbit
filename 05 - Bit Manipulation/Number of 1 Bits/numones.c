/**
 * @input A : Integer
 * 
 * @Output Integer
 */
int numSetBits(unsigned int A) {
    int res = 0;
    while (A != 0) {
        //printf("%d\n", A);
        res++;
        A &= (A - 1);
    }
    return res;
}

