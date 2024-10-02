def je_v_mnozici(el, set):
    if el in set:
        return True
    else:
        return False

vrne = je_v_mnozici("d", {"a", "b", "c"})
print(vrne)


