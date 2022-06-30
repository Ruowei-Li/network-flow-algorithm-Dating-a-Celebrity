# Network Flow algorithm -- Dating a Celebrity

Actors and actresses, sport stars, and some famous geeks have donated their time to support the “Dating a Celebrity” global charity event. Each star promised to date as many fans to support the charity. Each fan will date one, and only one, celebrity from her/his nominated set of favorite preferences. 

This program reads a listing of the names of the celebrities voluntering their time, a listing of the donor fans along with their favorite celebrites, it assigns the celebrities to one or more fans, for a date, in a way that minimizes the maximum number of dates that any celebrity has to attend.

# Test case description:

## Input
Input begins with an integer E on a line by itself, 1 ≤ E ≤ 2000, that represents the number of scenarios where each scenario describes a charity event. Each event description begins with two integers N and M, separated by a single space, on a line by themselves. The integer N represents the number of celebrities and M represents the number of donor fans. Each of the next N lines contains the name of a celebrity. Each of the following M lines, one line per donor, starts with the name of a donor followed by the names of her/his favourite stars, if any. 

Names are separated by a single space, and the name of a celebrity cannot appear more than once in each line. Each name (celebrity or fan) consists of a single word; that is, a string with no white spaces. The names of celebrities and fans are all distinct from each other. 1 ≤ N ≤ 50 and 1 ≤ M ≤ 2000.


## Output
There are two programs. The first program can parse the input and decide a lower bound on the number of dates needed [case (a)]. The second program will give the optimal answer [case (b)].
For each charity event, print the event number (starting with 1, and using the format in the samples) followed by a single space and then an integer (round up if needed) describing (a) the ‘number of fans who want to play with a star’ divided by N=‘number of celebrities’ and (b) the maximum number of rounds any star has to play.

### Sample Input
```
2
3 7
PrincessCindy
MrBig
BillGates
Zena MrBig
BuckJock PrincessCindy BillGates
DrMJD MrBig PrincessCindy BillGates
MissyC MrBig BillGates
MicheleJackson MrBig
MrsSmith
AdamSandman PrincessCindy
3 6
CaptainKirk
MrSpock
Xindi
FakeZena MrSpock
BuckGuy MrSpock
DrLove MrSpock
MissyC MrSpock
BootyJackson MrSpock
AliceSandy CaptainKirk Xindi
```

### Sample Output for case (a): lower bound 
```
Event 1: 2
Event 2: 2
```

### Sample Output for case (b): optimal answer
```
Event 1: 2
Event 2: 5
```
