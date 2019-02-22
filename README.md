# Pseudo-Code-Interpreter

A pseudo-code interpreter that uses python to interpret a simple language. ft. Mohamed ِAdbulkahar

## Work Completed:

Interpreter that is able to correctly interpret and execute the sample program under the name 'Pseudo-code-interpreter.py'

The interpreter can interpret and execute programs written in PCL (Pseudo Code Language) and not only the sample program.

The python program submitted has a loader which loads the data and program positionally into the corresponding memory.

A different but similar program named 'Different Program.txt' which takes in input and outputs the average of negative numbers and negative numbers separately.

A text file named 'Different Program With Comments', which details the logic and structure of 'Different Program.txt' in a similar structure to the sample program comments in the assignment.

Our interpreter is well documented and easy to read.

## Comments:

Our interpreter reads programs from txt files, stores every line of the program and every individual input in an array named 'inputs' 
and then it loads the data and program lines into the appropriate memory locations. As for the input, it takes it in when input statements are executed.

Since our interpreter reads programs from txt files, the standard program txt file is 'Sample Program.txt'. In order to read from other txt files, you may change the open file statement to open the desired file.

Most of the work our interpreter does is handeled through functions, and the "main" part of the interpreter contains only declaration of memory and global variables along with calls for the most fundamental functions which themselves call more specialised functions. We took this adecision to improve documentation,organization, and readability of our program.

We left some of the lines of code that we used to trace and debug as comments to show where we used tracing and debugging.

We did not need to introduce an absolute jump instruction.

We chose not to introduce the absolute jump instruction because we found that our interpreter (and the program we wrote in PCL) do not need it to run properly. We, thus, concluded that introducingan absolute jump instruction would go against the regularity principle. The regularity principle states that "Regular rules, without exceptions, are easier to learn, use, describe and implement." Introducing the absolute jump instruction would does not follow the principle since, for all our purposes at least, all that the absolute jump instruction does can be acheived using already implemented functions in our interpreter (conditions and loops). Introducing the instruction would also further decrease the readability of our
program and make it even harder to follow and understand.
