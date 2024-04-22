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

int file_symbol_freq(char *file_name, char symbol){
    FILE * file = fopen(file_name,"r");
    int symbol_count = 0;
    char s;
    while((s = fgetc(file)) != EOF ){
        if(s == symbol){
            symbol_count++;
        }
    }
    fclose(file);
    return symbol_count;
}

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
    count_bits(1232);
    print_fibonnaci(13);
    char symbol = 'o';
    char filename[] = "radom.txt";
    printf("The number of times %c appeared in %s was %d\n",symbol,filename, file_symbol_freq(filename,symbol));
    file_histogram(filename);
    return 0;
}
