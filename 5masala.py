# 5--------
def are_numbers_ascending(text: str)->bool:
    sonlar=[]
    for i in text.split():
        if i.isdigit():
            sonlar.append(int(i))
    for i in range(len(sonlar)-1):
        if sonlar[i]>=sonlar[i+1]:
            return False
    return True
text="1 qutida 5 ta yashil,9 ta qizil,12 ta sariq to'p bor edi"
print(are_numbers_ascending(text))