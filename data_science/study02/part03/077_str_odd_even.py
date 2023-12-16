txt = 'aAbBcCdDeEfFgGhHiIjJkK'
ret = txt[::2]  # 홀수번째만 출력
print(ret)  # [출력] abcdefghijk

ret = txt[1::2]  # 짝수번째만 출력
print(ret)  # [출력] ABCDEFGHIJK
