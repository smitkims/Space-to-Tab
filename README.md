# Space-to-Tab

The program will ask the user to enter a strings having several spaces and tabs. 
Then you have to replace all possible spaces into tabs with the same output as when you print. 
When you see the output of the print(), (1 ~ K) spaces is converted into a Tab. 
(Since K depends on system, we get K as an input. But, usually 4 or 8. 
Afterwards, check by printing out string containing tabs and give right number into input() function)

Tab makes [ (the length of string) mod K ] equal to 0. 
So, in this problem, some of the spaces should not be converted into tab. If possible, you must convert spaces into a tab.

Input → Output when you print() the input
a### → a(tab) (1)
ab##b → ab(tab)b (2)
##ab → ##ab (3)
ab##(tab)a##b → ab(tab)(tab)a##b (4)

In example (3), if you convert the two spaces into one tab, then when printed, you’ll see
####ab (X)
the answer is
##ab (O)
Because the output should be same when you print, you shouldn’t convert the spaces into a tab.

Input:
K (an integer)
- the number of spaces equal to tab in your idle when you
print, usually 4 or 8
- Note that, K is not manually defined by user. It only
depends on system. Please check K in your system and
use that K in your code.
- A string
Note that
- to enter tab, press [Shift + tab] instead of [Shift] in case of
IDLE
- Do not enter just /t (two character) for tab.
- Input string can contain ‘ ‘(space) and (tab) both, refer to
example (4) above

Output:
- A space-to-Tab converted string
- actually, the output should be same with the input when
we see the printed output.
- The length of the space-to-Tab converted string
