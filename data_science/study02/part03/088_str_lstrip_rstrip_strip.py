txt = ' 양쪽에 공백이 있는 문자열 '
ret1 = txt.lstrip()  # 왼쪽 공백 제거
ret2 = txt.rstrip()  # 오른쪽 공백 제거
ret3 = txt.strip()  # 양쪽 공백 제거
print('<' + txt + '>')
print('<' + ret1 + '>')
print('<' + ret2 + '>')
print('<' + ret3 + '>')
