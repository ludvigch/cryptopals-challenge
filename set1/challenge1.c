#include <string.h>
char* hexstr = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
// converts six bit value to B64 represented in ascii
char b64ToAsc(char sixbit){
    if(sixbit < 0)
        return '\0';
    else if(sixbit <= 25)
        return sixbit+65;
    else if(sixbit <= 51)
        return sixbit+(97-26);
    else if(sixbit <= 61)
        return sixbit+(48-52);
    else if(sixbit == 62)
        return sixbit+(43-62);
    else if(sixbit == 63)
        return sixbit+(47-63);
    else
        return 0;
}

// converts hex represented in ascii to its decimal value
char ascToHex(char ascii){
    if(ascii <= 57)
        return ascii-48;
    else
        return ascii-87;
}

void hexToB64(char* hexasc, char* storage){
    int buffer=0; int i;
    int b64index = 0;

    for(i=0; i < strlen(hexasc); i++){
        buffer = buffer << 4;
        buffer = buffer | ascToHex(hexasc[i]);
        if(i%6 == 5){
            int k;
            for(k=3; k>=0; k--){
                storage[b64index + k] = 0x3f & buffer;
                buffer = buffer >> 6;
            }
            b64index += 4;
            buffer = 0;
        }
    }
}

int main(int argc, char const *argv[]) {
    int i;
    char yo[(strlen(hexstr)/3)*2];
    hexToB64(hexstr, yo);

    for(i=0; i<strlen(yo); i++){
        yo[i] = b64ToAsc(yo[i]);
    }
    printf("Hex:\t%s\n", hexstr);
    printf("Base64: %s\n", yo);
    return 0;
}
