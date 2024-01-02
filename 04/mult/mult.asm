// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// Assumes that R0 >= 0, R1 >= 0, and R0 * R1 < 32768.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

//// Replace this comment with your code.
@R2
M=0
(LOOP)
@R1 // read R1
D=M
@END // if R1 = 0, end
D;JEQ

@R0 // read R0 value
D=M
@R2
D=D+M
M=D // R2+=R0 value
@R1
D=M-1
M=D // 1 less iteration
@LOOP // loop
0;JMP

(END)
@END
0;JMP
