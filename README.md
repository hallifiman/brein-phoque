# BFP
BFP(BrainFuck Plaintext) files are the plaintext version of breinphoque. Operands are to be 2-digit hex numbers marked with a preceeding dollar sign. The following is the documentation for BFP:
### INC
INC is the same as + in brainfuck. It takes one operand and adds that number to the current cell's value.
### DEC
DEC is the same as - in brainfuck. It takes one operand and subtracts that number from the current cell's value.
### PRT
PRT is the same as . in brainfuck. It takes no operands.
### ICI
ICI is the same as > in brainfuck. It takes one operand and moves forward in the memory strip that many times.
### DCI
DCI is the same as < in brainfuck. It takes one operand and moves backward in the memory strip that many times.
### ENL
ENL is the same as [ in brainfuck. It takes no operands.
### EXL
EXL is the same as ] in brainfuck. It takes no operands.
### ENF
ENF enters the definition of a function. It takes one operand, and the ID of said function is that operand.
### EXF
EXF exits the definition of a function.
### RNF
RNF runs a function. It takes one operand and runs the function whose ID is that operand.
### TUI
TUI is the same as , in brainfuck. It takes no operands.
# BFA
BFA(BrainFuck Assembly) files are the byte version of breinphoque. The following is a byte table for opcodes:
### INC
0x00
### DEC
0x01
### PRT
0x02
### ICI
0x03
### DCI
0x04
### ENL
0x05
### EXL
0x06
### ENF
0x07
### EXF
0x08
### RNF
0x09
### TUI
0x0A
