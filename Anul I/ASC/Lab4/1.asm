bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit
extern printf                ; declare printf as an external function
import exit msvcrt.dll
import printf msvcrt.dll     ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

                          
;Se da quadwordul A. Sa se obtina numarul intreg N reprezentat de bitii 35-37 ai lui A. Sa se obtina apoi in B dublucuvantul rezultat prin rotirea spre dreapta a dublucuvantului inferior al lui A cu N pozitii. Sa se obtina octetul C astfel:
;bitii 0-3 ai lui C sunt bitii 8-11 ai lui B
;bitii 4-7 ai lui C sunt bitii 16-19 ai lui B

; our data is declared here (the b needed by our program)
segment data use32 class=data
    ; ...
    format db "Value of C: %02X", 10, 0
    a dq 1234567h
    b resd 1
    c resb 1
    

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov eax, dword[a+4] ; mutam partea superioara a lui x in eax
        shr eax, 3 ; mutarea bititlor spre dreapta
        and eax, 07h ; aplicam masca pentru a retine doar primii 3 biti
        
        mov ecx, eax ; ecx = n si cl = n
        
        mov eax, dword[a] ; incarcam partea inferioara a lui a in eax
        ror eax, cl ; rotim eax spre dreapta cu n biti
        mov [b] , eax ; punem rezultaul in b
        
        ;bitii 0-3 ai lui C sunt bitii 8-11 ai lui B
        ;bitii 4-7 ai lui C sunt bitii 16-19 ai lui B
        
        mov eax, [b] ; eax = b
        mov edx, eax ; edx = b
        
        shr eax, 8 ; deplasam valoarea din b cu 8 biti pentru a aduce bitii 8-11 pe 0-3
        and eax , 0fh ; aplicam masca pentru a retine daor bitii 0-3
        
        shr edx, 16 ; deplasam valoarea lui b cu 16 biti pentru a aduce bitii 16-19 pe 0-3
        and edx, 0fh ; aplicam masca pentru a retine doar bitii 0-3
        shl edx, 4 ; deplasam bitii la stanga cu 4 pozitii pentru a ajunge pe 4-7
        
        or eax, edx ; combinam bitii pentru a forma octetul c
        mov [c], al
        push dword [c]     
        push dword format   
        call [printf] 
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
