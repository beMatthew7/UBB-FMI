bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, fprintf, fopen               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import scanf msvcrt.dll
import fprintf msvcrt.dll
import fopen msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    m dd 0
    n dd 0
    format_citire db "%d%d", 0
    format_citire_s db "%s", 0
    numar times 50 db 0
    acces_mode db "w", 0
    file_name db "output.txt", 0
    format_afisare db "%s", 10,0
    file_descriptor dd -1
    

; our code starts here
segment code use32 class=code
    start:
        ; ...
        push n
        push m
        push format_citire
        call [scanf]
        add esp, 3 * 4
        
        push acces_mode
        push file_name
        call [fopen]
        add esp, 2 * 4
        
        cmp eax, 0
        je final
        
        mov dword[file_descriptor], eax
        
        citire_numere:
            mov ecx, dword[m]
            cmp ecx, 0
            je afisare
            dec ecx
            mov [m], ecx
            
            push numar
            push format_citire_s
            call [scanf]
            add esp, 2 * 4
            
            mov esi, numar
            
            verificare_numar_cifre:
                lodsb 
                cmp al, 0
                je ver
                jmp verificare_numar_cifre
            
            
        
            ver:
                mov eax, esi
                sub eax, numar
                
                mov ebx, [n]
                inc ebx
                
                cmp eax, ebx
                jb citire_numere
                push numar
                push format_afisare 
                push dword[file_descriptor]
                call [fprintf]
                add esp, 3 * 4
                jmp citire_numere 
                
                

        afisare:


            
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
