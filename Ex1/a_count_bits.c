#include <stdio.h>

void count_bits(int val){
    int cpy = val;
    int one_count = 0;
    int zero_count = 0;
    while(cpy != 0){
        if(cpy & 1){
            one_count++;
        } else {
            zero_count++;
        }
        cpy = cpy>>1;
    }
    printf("%d has %d one's and %d zero's\n",val,one_count,zero_count);
}

int main() {
    count_bits(1232);
    return 0;
}