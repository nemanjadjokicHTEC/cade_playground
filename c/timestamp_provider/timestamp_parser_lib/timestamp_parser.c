#include <stdio.h>
#include <time.h>


char* get_human_readable_from_timestamp(long timestamp)
{
    struct tm *timeinfo = localtime(&timestamp);
    return asctime(timeinfo);
}