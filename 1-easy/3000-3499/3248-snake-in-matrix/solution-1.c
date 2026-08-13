#include <stdio.h>
#include <string.h>

int finalPositionOfSnake(int n, char **commands, int commandsSize)
{
    int ans = 0;
    for (int i = 0; i < commandsSize; ++i)
    {
        char c = commands[i][0];
        if (c == 'L')
            --ans;
        else if (c == 'R')
            ++ans;
        else if (c == 'U')
            ans -= n;
        else
            ans += n;
    }
    return ans;
}

int main(void)
{
    char *commands[] = {"RIGHT", "DOWN", "LEFT", "LEFT", "DOWN"};
    int n = 3;
    int commandsSize = sizeof(commands) / sizeof(commands[0]);
    int result = finalPositionOfSnake(n, commands, commandsSize);
    printf("Final Position: %d\n", result); // Output: Final Position:
    return 0;
}