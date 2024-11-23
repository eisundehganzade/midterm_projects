import string
def main():
   text = str(input("enter your text: "))
   text = hazfSpace(text)
   sort(text) 


def sort(text):
    alefba = []
    adad = []
    digar = []
    for ch in text :
        if ch in string.ascii_letters:
            alefba.append(ch)
        elif ch in string.digits:
            adad.append(ch)
        else:
            digar.append(ch)        
    print(''.join(digar) + ''.join(sorted(adad)) + ''.join(sorted(alefba , key = lambda s:s.lower())))


def hazfSpace(text):
    return''.join(text.split())

if  __name__ == '__main__':
    main()    