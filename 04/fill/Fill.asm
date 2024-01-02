// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// init POSITION
@SCREEN
D=A
@POSITION
M=D

(LOOP)
@KBD
D=M
@CLEARSCREEN
D;JEQ
@FILLSCREEN
D;JNE
@LOOP
0;JMP

(FILLSCREEN)
// check if POSITION is max
@POSITION
D=M
@24576
D=D-A
// if so
@LOOP
D;JEQ
// otherwise
@POSITION
A=M
M=-1
// next POSITION
@POSITION
D=M+1
M=D
// back to loop
@LOOP
0;JMP

(CLEARSCREEN)
// check if POSITION is SCREEN
@POSITION
D=M
@SCREEN
D=D-A
// if so
@LOOP
D;JLT
// otherwise
@POSITION
A=M
M=0
// next POSITION
@POSITION
D=M-1
M=D
// back to loop
@LOOP
0;JMP
