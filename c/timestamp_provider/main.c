#include "timestamp_provider.h"
#include "timestamp_parser.h"
#include <stdio.h>

int main(int argc, char** argv)
{
    printf("%ld\n", get_timestamp());
    // printf("%s\n", get_human_readable_from_timestamp(get_timestamp()));
}