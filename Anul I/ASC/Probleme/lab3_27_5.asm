bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a db 7
    b db 20
    c db 10
    d db 19
    e dw 121
    f dw 300
    g dw 79
    h dw 432

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov bx, [e] ;bx = [e]
        add bx, [f] ;bx = bx + [f]
        sub bx, [g] ;bx = bx - [g]
        mov al, [b] ;al = [b]
        add al, [c] ;al = [b] + [c]
        mov cl, 3 ;cl = 3
        mul cl ;ax = al * cl
        add ax, bx ;ax = ax + bx 
        mov cx, 5; cx = 5
        mul cx; ax =ax * cx
        push dx
        push ax
        pop eax 
        
        
        
        
        

        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
