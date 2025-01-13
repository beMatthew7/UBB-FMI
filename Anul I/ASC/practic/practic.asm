; Se citeste de la tastatura un nume de fisier, un caracter c si un numar n. Sa se determine daca numarul de aparitii ale caracterului c in textul fisierului este egal cu numarul n, afisandu-se la consola un mesaj corespunzator (formatati textul ca si in exemplu)./

; Read from the console a file name, a character c, and a number n. Determine if the number of occurrences of the character c from the text file is equal with n, and write the corresponding message to the console (with the format as in the example).

; Example:

; c = a

; n = 2

; Input.txt

; ana are alte mere alina are doar pere

; Console:

; Numarul de aparitii al caracterului a citit nu este egal cu numarul 2 citit./

; The number of occurrences of the character a is not equal to the read number 2.
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, fopen, printf, fclose, fread              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll 
import scanf msvcrt.dll
import fopen msvcrt.dll
import printf msvcrt.dll
import fclose msvcrt.dll 
import fread msvcrt.dll ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name times 50 db 0
    acces_mode db "r", 0
    c dd 0
    n dd 0
    format_citire db "%s %c %d", 0
    file_descriptor dd -1
    text times 501 db 0
    nr_aparitii dd 0
    format_afisare_nu db "Numarul de aparitii al caracterului %c nu este egal cu numarul %d citit", 0
    format_afisare_da db "Numarul de aparitii al caracterului %c este egal cu numarul %d citit", 0
    

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;citire nume fisier, caracter c, numarul n
        push n
        push c
        push file_name
        push format_citire
        call [scanf]
        add esp, 4 * 4
        
        
        ;deschidere fisier
        push acces_mode
        push file_name
        call [fopen]
        add esp, 2 * 4
        
        ;verificam daca s-a deschis corect fisierul
        cmp eax, 0
        je eroare
        
        mov dword[file_descriptor], eax
        
        ;citire text fisier
      
        push dword[file_descriptor]
        push 500
        push 1
        push text
        call [fread]
        add esp, 4 * 4
        
        mov esi, text
        
        parcurgere_caractere_fisier:
            lodsb
            cmp al, 0
            je verificare_nr_aparitii
            mov bl, [c]
            cmp al, bl
            jne parcurgere_caractere_fisier
            
            add dword[nr_aparitii], 1
            jmp parcurgere_caractere_fisier
            
        verificare_nr_aparitii:
            mov eax, [nr_aparitii]
            mov ebx, [n]
            
            cmp eax, ebx
            jne afisare_nu
            
            
        afisare_da:
            push dword [n]
            push dword [c]
            push format_afisare_da
            call [printf]
            add esp, 3 * 4
            
            jmp close        
            
        afisare_nu:
            push dword [n]
            push dword [c]
            push format_afisare_nu
            call [printf]
            add esp, 3 * 4
            
            jmp close
        
        
        
        
        ;inchidere fisier
        close:
            push dword [file_descriptor]
            call [fclose]
            add esp, 4
        
        
        eroare:
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
