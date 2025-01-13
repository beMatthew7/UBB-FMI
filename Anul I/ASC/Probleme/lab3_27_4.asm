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
    b db 193
    c db 50
    d dw 200

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov al, [a] ;al = [a]
        add al, [b] ; al = [a] + [b]
        mov cl, [c] ; cl = [c]
        add cl, cl ; cl = [c] + [c]
        sub al, cl  ; al = al - cl
        mov bl, al  ; bl = al
        mov ax, [d]  ; ax = [d]
        
                  
        
        div bl
        
        
        
        

        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
