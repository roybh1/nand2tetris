@256
D=A
@SP
M=D
@RETURN_0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(RETURN_0)
(Sys.init)
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@3
D=D+A
@13
M=D
@SP
A=M-1
D=M
@13
A=M
M=D
@SP
M=M-1
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@3
D=D+A
@13
M=D
@SP
A=M-1
D=M
@13
A=M
M=D
@SP
M=M-1
@RETURN_5
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.main
0;JMP
(RETURN_5)
@1
D=A
@5
D=D+A
@13
M=D
@SP
A=M-1
D=M
@13
A=M
M=D
@SP
M=M-1
(LOOP)
@LOOP
0;JMP
(Sys.main)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@3
D=D+A
@13
M=D
@SP
A=M-1
D=M
@13
A=M
M=D
@SP
M=M-1
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@3
D=D+A
@13
M=D
@SP
A=M-1
D=M
@13
A=M
M=D
@SP
M=M-1
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@LCL
D=D+M
@13
M=D
@SP
A=M-1
D=M
@13
A=M
M=D
@SP
M=M-1
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@LCL
D=D+M
@13
M=D
@SP
A=M-1
D=M
@13
A=M
M=D
@SP
M=M-1
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
@3
D=A
@LCL
D=D+M
@13
M=D
@SP
A=M-1
D=M
@13
A=M
M=D
@SP
M=M-1
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
@RETURN_20
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.add12
0;JMP
(RETURN_20)
@0
D=A
@5
D=D+A
@13
M=D
@SP
A=M-1
D=M
@13
A=M
M=D
@SP
M=M-1
@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
@3
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
@4
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1
@LCL
D=M
@R14
M=D
@5
A=D-A
D=M
@R15
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
D=A
@SP
M=D+1
@R14
AM=M-1
D=M
@THAT
M=D
@R14
AM=M-1
D=M
@THIS
M=D
@R14
AM=M-1
D=M
@ARG
M=D
@R14
AM=M-1
D=M
@LCL
M=D
@R15
A=M
0;JMP
(Sys.add12)
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@3
D=D+A
@13
M=D
@SP
A=M-1
D=M
@13
A=M
M=D
@SP
M=M-1
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@3
D=D+A
@13
M=D
@SP
A=M-1
D=M
@13
A=M
M=D
@SP
M=M-1
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
@12
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1
@LCL
D=M
@R14
M=D
@5
A=D-A
D=M
@R15
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
D=A
@SP
M=D+1
@R14
AM=M-1
D=M
@THAT
M=D
@R14
AM=M-1
D=M
@THIS
M=D
@R14
AM=M-1
D=M
@ARG
M=D
@R14
AM=M-1
D=M
@LCL
M=D
@R15
A=M
0;JMP
