from numseq import hello

def test_hello():
    assert hello("Luca") == "Salut, Luca!"
    assert hello("Mundo") == "Salut, Mundo!"
    print("Toate testele au trecut!")

if __name__ == "__main__":
    test_hello()
