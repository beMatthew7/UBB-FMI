bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf ; add printf and scanf as extern functions            
import exit msvcrt.dll    
import printf msvcrt.dll    ; tell the assembler that function printf is found in msvcrt.dll library
import scanf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dd 0
    b dd 0
    format_citire db '%d', 0
    format_afisare db '%d', 0
    rezultat dd 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        push a
        push format_afisare
        call [scanf]
        add esp, 4 * 2
        
        push b
        push format_afisare
        call [scanf]
        add esp, 4 * 2
        
        mov eax,[a]
        add eax, [b]
        
        mov ecx, [a]
        sub ecx, [b]
        
        mul ecx
        
        mov [rezultat], eax
        
        push dword [rezultat]
        push format_afisare
        call [printf]
        add esp, 4 * 2
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
