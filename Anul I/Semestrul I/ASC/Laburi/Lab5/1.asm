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
    s db '+', '4', '2', 'a', '@', '3', '$', '*'
    len equ $-s
    caract db "!@#$%&^*"
    lenc equ $-caract
    d resb len

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx, len
        mov esi, 0 ; pozitia in s
        mov edi, 0 ; pozitia lui d
        
        jecxz final
        repeta:
            mov al, [s + esi] ; caracte din sirul sursa
            
            push ecx
            push esi
            
            mov ecx, lenc
            mov esi, 0
            
            repeta2:
                mov bl, [caract + esi]
                cmp al, bl ; le comparam
                jne final2            
                
                mov [d + edi], al
                inc edi ; trece in urmaotrea pozitie si in sirul destinatie
                jmp gasit
                
                final2:
                inc esi ; trecem la urmatorul caracter
            loop repeta2
            gasit:
            pop esi
            pop ecx
            
            inc esi
            
        
        loop repeta
        final:
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
