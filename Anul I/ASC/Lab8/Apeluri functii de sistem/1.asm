bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    numar1 dw 0
    numar2 dw 0
    format db '%d', 0
    rezultat dd 0
    afisare  db '%d', 0

; our code starts here
segment code use32 class=code
    start:
        ; ...


        push dword numar1
        push dword format
        call [scanf]
        add esp, 2 * 4
        
        push dword numar2
        push dword format
        call [scanf]
        add esp, 2 * 4
        
        mov ax, [numar1]
        mov bx, [numar2]
        
        mul bx
        
        

        push dx
        push ax
        pop eax
        
        mov dword [rezultat], eax
        
        push dword [rezultat]
        push dword afisare
        call [printf]
        add esp, 2 * 4
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
