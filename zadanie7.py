while zgaduj:
    odpowiedz = input("Czy jest snieg? (t/n) ").lower() 

    if odpowiedz == "t": 
        if pada:
            print("Tak, zgadłeś! Jest.")
            zgaduj = False  
        else:
            print("Nie, nie ma. Spróbuj jeszcze raz.")
    elif odpowiedz == "n": 
        if not pada:
            print("Tak, zgadłeś! Nie pada.")
            zgaduj = False 
        else:
            print("Nie, pada. Spróbuj jeszcze raz.")
    else:
        print("Nie rozumiem odpowiedzi. Wpisz 't' lub 'n'.")
