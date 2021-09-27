# FSM (Finite State Machine)

A FSM $;$ consists of a set S, R and Q, where: 

* $S$ is a finite input alphabet,
* $R$ is a finite output alphabet and
* $Q$ is a set of states.

## Input:

* $n$: the number of tests cases

* $|S|$: Length of input alphabet

* $S$: input alphabet separated by spaces

* $|R|$: Length of output alphabet

* $R$: Output alphabet separated by spaces

* $|Q|$: Cardinality of set of states

* $Q$: set of states separated by spaces

* $Q_0$: Initial state

* Matrix of shape $|Q| \times (2|S| + 1) $ where each row is separated by spaces 

## Ouput:

* $b$, the number of lines corresponding to the number of blocks.

* For each line, print the states that correspond to that each block separated by spaces, the order does not matter

## Examples

### Case 1

#### Input

```
2
0 1
2
0 1
6
A B C D E F
A
A B 0 D 0
B C 1 E 1
C B 0 F 0
D E 0 A 0
E F 0 B 0
F E 0 C 0
```

#### Output
```
4
A C
D F
E 
B
```

### Case 2

#### Input

```
2
a b
4
0 1 2 3
10
A B C D E F G H I J
E
A B 1 C 2
B C 2 D 3
C D 3 A 0 
D A 0 B 1
E F 1 G 2 
F G 2 H 3
G H 3 I 0
H I 0 F 1
I F 1 G 2
J E 0 I 0
```

#### Output
```
4
A E I
B F
C G
D H
```
