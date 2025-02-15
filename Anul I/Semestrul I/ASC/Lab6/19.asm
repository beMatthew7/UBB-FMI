bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    sir1 db 'abababcbababcabc'   
    len1 equ ($-sir1)             
    sir2 db 'abc'                 
    len2 equ ($-sir2)              
    sir3 resb len1
    nr_pozitii resb 1
    
segment code use32 class=code
    start:
        mov esi, sir1
        mov edi, sir3
        mov ecx, len1
        mov bl, 0 ; index pentru sir1
        mov edx, 0 ; index sir2
        
    loop1:
        inc bl 
        cmp ecx, 0
        je final
        lodsb
        cmp al, [sir2 + edx]
        je egal
        jmp nu_egal
        
        
    egal:
        inc edx
        cmp edx, len2 ; verificam daca am verificat tot subsirul
        jne loop1 ; trecem la urmatorul caracter
        sub bl, len2
        mov al, bl  ; copiem indexul curent
        add bl, len2
        stosb ; punem in sir3 pozitia
        mov edx, 0
        
        
    nu_egal:
        dec ecx 
        jmp loop1
        
        
        
        


    
    final:
        sub edi, sir3 ; numarul de pozitii salvate
        mov [nr_pozitii], edi
        push dword 0             
        call [exit]
