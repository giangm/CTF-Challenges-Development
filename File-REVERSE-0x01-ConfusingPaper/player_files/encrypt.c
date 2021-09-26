#define digit int
#define entrance main()
#define letters char
#define say printf
#define read scanf
#define count strlen
#define during while
#define string "%s", message
#define number "%d", &shift
#define do {
#define done }
#define mod %
#define add +
#define minus -
#define not_equal !=
#define equal =
#define lesser <

#include <stdio.h>
#include <string.h>

digit entrance do
    say("Enter the message you would like to encrypt: ");
    letters message[100];
    read(string);
    say("Enter a number between 1-10: ");
    digit shift;
    read(number);

    digit cipher[count(message)];
    
    digit i equal 0;
    during (i lesser count(message)) do
        if (i mod 2 not_equal 0) do
            cipher[i] equal message[i] add shift;
        done else do
            cipher[i] equal message[i] minus shift;
        done

        shift equal shift add 1; 
        i equal i add 1;
    done

    for (digit i equal 0; i lesser sizeof cipher / sizeof cipher[0]; i equal i add 1) do
        say("%d ", cipher[i]);
    done
done
