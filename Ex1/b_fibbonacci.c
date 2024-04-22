#include <stdio.h>

// Definição da função que imprime os primeiros N termos da sequência de Fibonacci
void print_fibonacci(int N) {
    long long first = 0, second = 1, next;
    int i;

    if (N == 1) {
        // Se N for 1, imprime apenas o primeiro termo
        printf("%d\n", first);
    } else {
        // Começa por imprimir os dois primeiros termos
        printf("%d, %d", first, second);
        // Calcula e imprime os termos seguintes até N
        for (i = 2; i < N; i++) {
            next = first + second;
            printf(", %d", next);
            first = second;
            second = next;
        }
        printf("\n");
    }
}

int main() {
    int N;

    // Pede ao utilizador para inserir o número de termos
    printf("Insert the number of terms: ");
    scanf("%d", &N);

    // Chama a função para imprimir a sequência de Fibonacci
    print_fibonacci(N);

    return 0;
}
