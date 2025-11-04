#include "timestamp_provider.h"
#include <time.h>

long get_timestamp()
{
    return time(NULL);
}