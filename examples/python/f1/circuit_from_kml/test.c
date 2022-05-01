#include <stdio.h>
#include "fastestlapc.h"

int main(void)
{
    int i;
    printf("Hello world!\n");

    const char *left = "/home/kktse/src/fastest-lap/database/tracks/lfg/LFG_Left.kml";
    const char *right = "/home/kktse/src/fastest-lap/database/tracks/lfg/LFG_Right.kml";
    const char *out = "/home/kktse/src/fastest-lap/database/tracks/lfg/mytrack.xml";

    circuit_from_kml(left, right, 500, out);
}

