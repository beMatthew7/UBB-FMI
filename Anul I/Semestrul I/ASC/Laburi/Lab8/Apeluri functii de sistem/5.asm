bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll 
import scanf msvcrt.dll
import printf msvcrt.dll   ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dw 0
    b dw 0
    r dd 0
    cat dd 0
    
        
    format_citire  db '%d', 0
    format_afisare db  "Cat = %d, rest = %d", 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        push a
        push format_citire
        call [scanf]
        add esp, 4 * 2
        
        push b
        push format_citire
        call [scanf]
        add esp, 4 * 2
        
        mov dx, 0
        mov ax, [a]
        mov bx, [b]
        
        div bx
        
        mov [r], dx
        mov [cat], bx
        
        push dword [r]
        push dword [cat]
        push format_afisare
        call [printf]
        add esp, 4 * 3
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
