bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, fopen, fclose, fscanf, printf, fgets, fprintf           ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import scanf msvcrt.dll 
import fopen msvcrt.dll
import fclose msvcrt.dll
import fscanf msvcrt.dll
import printf msvcrt.dll
import fgets msvcrt.dll
import fprintf msvcrt.dll
   ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    nume_fisier times 50 db 0
    nume_fisier_output db "output.txt", 0
    acces_mode db "r", 0
    acces_mode_output db "w", 0
    format_citire db "%s", 0
    file_descriptor dd -1
    cuvinte times 200 db ' '
    format_afisare db "%c", 0
    nr dd 0
    format_afisare_d db "%d", 0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push nume_fisier
        push format_citire
        call [scanf]
        add esp, 2 * 4
        
        
        push acces_mode
        push nume_fisier
        call [fopen]
        add esp, 2 * 4
        
        cmp eax, 0
        je final
        
        mov dword[file_descriptor], eax
        
        citim_fisierul:
            push dword[file_descriptor]
            push 200
            push cuvinte
            call [fgets]
            add esp, 3 * 4
            
        close:
            push dword[file_descriptor]
            call [fclose]
            add esp, 4
        
        
        
        
        push acces_mode_output
        push nume_fisier_output
        call [fopen]
        add esp, 2 * 4
        cmp eax, 0
        je final
        
        
        mov dword[file_descriptor], eax
        mov esi, cuvinte
        caractere:
            mov eax, 0
            lodsb
            cmp al, 0
            je final
            cmp al, 'a'
            jb continua
            cmp al, 'z'
            ja continua
            
            push eax
            push format_afisare_d
            push dword[file_descriptor]
            call [fprintf]
            add esp, 3 * 4
            jmp caractere
            
            continua:
            push eax
            push format_afisare
            push dword[file_descriptor]
            call [fprintf]
            add esp, 3 * 4
            jmp caractere
            
            
        final:
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
