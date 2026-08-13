#include <stdbool.h>

bool strongPasswordCheckerII(char *password)
{
    if (strlen(password) < 8)
        return false;

    const char *specialChars = "!@#$%^&*()-+";
    bool lower = false, upper = false, digit = false, special = false;

    for (int i = 0; password[i]; ++i)
    {
        if (i > 0 && password[i] == password[i - 1])
            return false;

        int ascii = (int)password[i];
        if (ascii >= 48 && ascii <= 57)
        {
            if (!digit)
                digit = true;
        }
        else if (ascii >= 65 && ascii <= 90)
        {
            if (!lower)
                lower = true;
        }
        else if (ascii >= 97 && ascii <= 122)
        {
            if (!upper)
                upper = true;
        }
        else if (!special)
        {
            for (int j = 0; specialChars[j]; ++j)
            {
                if (specialChars[j] == password[i])
                {
                    special = true;
                    break;
                }
            }
        }
    }
    return lower && upper && digit && special;
}