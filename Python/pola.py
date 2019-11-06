

#  
#  


def main(args):
    a = input("Podaj długość boku:")
    b = input("Podaj długość boku:")
    print("Pole prostokata:", int(a) * int(b))
    c = input("Podaj długość podstawy:")
    d = input("Podaj długość wysokości:")
    print("Pole trójkąta:", int(c) * int(d) * 0.5)
    e = input("Podaj długość promienia:") 
    f = input("podaj liczbę pi:")
    print("Pole koła:", int(e) * int(e) * int(f))
    
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
