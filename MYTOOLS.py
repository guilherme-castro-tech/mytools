
PI_INT  = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
E_INT   = "7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"

def pi_real(N:int)->str:
    if (N>100) or (N<0) :
        return print("Número de dígitos excede o tamanho possível.")
    else:
        pi_dec_trunc = PI_INT[:N]
        pi_trunc = f"3.{pi_dec_trunc}"
        return print(pi_trunc)

def e_real(N:int)->str:
    if (N>100) or (N<0) :
        return print("Número de dígitos excede o tamanho possível.")
    else:
        e_dec_trunc = PI_INT[:N]
        e_trunc = f"2.{e_dec_trunc}"
        return print(e_trunc)




if __name__ == "__main__":
    N = int(input("Digite um número de 1 a 100: "))
    pi_real(N)