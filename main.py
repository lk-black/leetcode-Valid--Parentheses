class Solution:
    def isValid(self, s: str) -> bool:

        # como a comparação será feita quando aparecer um fechado,
        # então temos que colocar os pares invertidos
        # porque nós temos o aberto como o ultimo da pilha,
        # então verifcaremos se o parentese fechado correseponde ao par
        # do ultimo parentese aberto
        pares = {")": "(", "]": "[", "}": "{"}

        pilha = []

        for char in s:

            if char in pares.values():
                pilha.append(char)

            elif char in pares:

                if not pilha:
                    return False

                topo = pilha.pop()

                if topo != pares[char]:
                    return False

        return len(pilha) == 0
