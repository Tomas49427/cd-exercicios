#include <stdio.h>

// Definição da função que imprime os primeiros N termos da sequência de Fibonacci
void print_fibonnaci(int N){
    if(N == 0){
        printf("%d",0);
        return;
    }
    if(N == 1){
        printf("%d",1);
        return;
    }
    int previous = 0;
    int current = 1;
    for(int i = 2; i<N; i++){
        int temp = current;
        current += previous;
        previous = temp;
    }
    printf("The %d term of the Fibonnaci sequence is: %d\n",N,current);
}

int main() {
    print_fibonnaci(13);
    return 0;
}
