bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=dataa
    s db 5, 25, 55, 127  
    len equ ($-s)         
    d resb len            

segment code use32 class=code
    start:
        mov ECX, len       
        mov ESI, s         
        mov EDI, d         

        jecxz final        
        
        cld                
    procesare:
        lodsb              ; Incarcam un octet din s in AL
        mov BL, 0      
        mov DL, AL         

        push ecx
        
        mov ecx, 8
    numara_biti:
    
        and DL, 1          
        add BL, DL         
        shr AL, 1 
        mov dl, al
        loop numara_biti   
        
        pop ECX
        
        mov al, bl
        stosb              ; Salvam contorul in d
        loop procesare     
        
    final:
        push    dword 0    ; push the parameter for exit onto the stack
        call    [exit]     ; call exit to terminate the program
