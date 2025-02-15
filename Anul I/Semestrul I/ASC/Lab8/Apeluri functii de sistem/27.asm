bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll   ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    sir_caractere db  "adjkajsnanld"
    len dd $ - sir_caractere
    format_citire db "%c", 0
    format_afisare db "%c %d", 0
    nr_aparitii dd 0
    caracter dd 0
    
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
       
        push caracter
        push format_citire
        call [scanf]
        add esp, 2 * 4
        mov esi, sir_caractere
        mov ecx, [len]
        
       
        
        repeta:
        mov bl, [caracter]
        lodsb
        cmp al, bl
        jne nu_egal
        mov eax, [nr_aparitii]
        add eax, 1
        mov [nr_aparitii], eax
        
        
        nu_egal:
        loop repeta
        
        push dword [nr_aparitii]
        push dword [caracter]
        push format_afisare
        call [printf]
        add esp, 3 * 4
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
