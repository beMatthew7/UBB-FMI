bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
;interpretare fara semn
;(d + d -  b) + (c - a) + d
segment data use32 class=data
    ; ...
    a db 7
    b dw 19
    c dd 20
    d dq 100
        
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ; punem d-ul pe eax:edx
        mov eax, dword [d + 0]
        mov edx, dword [d + 4]
        ; punem d-ul pe ecx:ebx
        mov ebx, dword [d + 0]
        mov ecx, dword [d + 4]
        
        ;ecx:ebx = d + d
        clc
        add ebx, eax ; ebx = ebx + eax 
        adc ecx, edx ; ecx = ecx + edx 
        
        mov eax, 0
        mov edx, 0
        mov ax, [b]; edx:eax = b
        
        ;ecx:ebx = d + d - b
        clc
        sub ebx, eax ; ebx = ebx - eax
        sbb ecx, edx ; ecx = ecx - edx
        
        
        mov eax, [c]
        mov edx, 0
        mov dl, [a]
        sub eax, edx ; eax = eax - edx = (c - a)
        mov edx, 0
        
        
        ;ecx:ebx = (d+d-b)+(c-a)
        clc
        add ebx, eax ; ebx = ebx + eax
        adc ecx, edx ; ecx = ecx + edx
        
        ; edx:eax = d
        mov eax, dword [d + 0]
        mov edx, dword [d + 4]
        
        
        ;ebx:ecx = (d+d-b)+(c-a)+d
        clc
        add ebx, eax ; ebx = ebx + eax
        adc ecx, edx ; ecx = ecx + edx
        
        
        
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
