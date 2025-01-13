bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    format_citire db "%s", 0
    sir times 200  db 0
    sir_litere_mici times 200 db 0
    sir_litere_mari times 200 db 0
    i dd 0
    j dd 0
    format_afisare_mici db "Sir litere mici:%s", 0
    format_afisare_mari db "Sir litere mari:%
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push sir
        push format_citire
        call [scanf]
        add esp, 2 * 4
        
        mov esi, sir
        
        citire_caractere:
            lodsb
            cmp al, 0
            je afisare             
            cmp al, 'A'
            jb continua
            cmp al, 'Z'
            ja continua
            
            mov ebx, [i]
            mov [sir_litere_mari + ebx], al
            inc ebx
            mov [i], ebx
            
            
            
            continua:
            cmp al, 'a'
            jb continua1
            cmp al, 'z'
            ja continua1
            
            mov ebx,  [j]
            mov [sir_litere_mari + ebx], al
            inc ebx
            mov [j], ebx
            
            continua1:
            jmp citire_caractere
            
        afisare:
            mov esi, sir_litere_mari
            push esi
            mov esi, sir_litere_mici
            push esi
            push format_afisare
            call [printf]
            add esp, 3 * 4
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
