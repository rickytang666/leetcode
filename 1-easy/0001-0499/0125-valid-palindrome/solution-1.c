#include <stdbool.h>
#include <ctype.h>
#include <string.h>

bool isPalindrome(char *s)
{
    int left = 0, right = strlen(s) - 1;
    while (left < right)
    {
        while (left < right && !isalnum(s[left]))
            left++;
        while (left < right && !isalnum(s[right]))
            right--;
        char c1 = tolower(s[left]);
        char c2 = tolower(s[right]);
        if (c1 != c2)
            return false;
        left++;
        right--;
    }
    return true;
}