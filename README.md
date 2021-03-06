# jTU-22-design-pattern-assignment

## Rock Paper Scissor Game

The application is a Human vs. CPU game. Since the focus is on various strategies the CPU can use, I have used the Strategy pattern.
I have implemented both the strategies as classes following an (informal) interface. This interface is completely seperate from the CpuPlayer class.
Strategies can be changed at runtime.
Strategies can be added, modified without any hassle.

Since the history of a Rock Paper Scissor session is required for the mirror strategy (practically only the last move), it should be available to all strategies. In a large code-base such things maybe implemented as Singletons (Global variables but safe) or it would be passed to all strategies as parameters.

## Division Decorator

Assumption - The decorator is intended to be used only for the division function

The decorator checks for number of arguments, whether the arguments can be converted to numbers and if there is division by zero.
