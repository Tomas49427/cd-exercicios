#include <stdio.h>

void print_histogram_line(int frequency, char symbol){
    char buffer[255];
    char histogram_symbol;
    int histogram_value;
    if(frequency % 10 == 0){
        histogram_symbol = '+';
        histogram_value = frequency / 10;
    } else if(frequency % 5 == 0){
        histogram_symbol = '#';
        histogram_value = frequency / 5;
    } else {
        histogram_symbol = '!';
        histogram_value = frequency;
    }
    for(int i = 0; i<histogram_value; i++){
        buffer[i] = histogram_symbol;
    }
    buffer[histogram_value] = '\0';
    printf("%c | %s\n", symbol,buffer);
}

void file_histogram(char *file_name){
    int symbol_freq[256];
    for(int i = 0; i< 256; i++){
        symbol_freq[i] = file_symbol_freq(file_name,(char)i);
    }
    printf("! = 1 | # = 5 | + = 10\n");
    printf("----------------------\n");
    for(int i = 0; i < 256; i++){
        if(symbol_freq[i] != 0){
            print_histogram_line(symbol_freq[i],(char)i);
        }
    }
    printf("----------------------\n");
}

int main() {
    char filename[] = "input.txt";
    file_histogram(filename);
    return 0;
}