#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

/**
 *infinite_while - infinite while loop
 *Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(100);
	}
	return (0);
}

/**
 *main - entry point
 *Return: 0 on success
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid < 0)
		{
			perror("fork");
			exit(1);
		}

		/*child*/
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	/*parent*/
	infinite_while();

	return (0);
}
/*
 *The code uses a for loop to create 5 child processes by calling the fork()
 *function 5 times. If the return value of fork() is 0, it means the current
 *process is a child process, and it exits immediately with status 0.
 *
 *In the parent process, the code waits for 100 seconds using the sleep()
 *function, after which the program exits, leaving the 5 child processes as
 *zombies.
*/
