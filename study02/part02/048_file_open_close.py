# open('파일이름','모드')
# close()
f1 = open('text.txt', 'r')
f2 = open('d:/myimages/pypicturel.jpg', 'rb')

f1.close()
f2.close()

# r, rt - 텍스트 모드로 읽기
# w, wt - 텍스트 모드로 쓰기
# a, at - 텍스트 모드로 파일 마지막에 추가하기
# rb - 바이너리 모드로 읽기
# wb - 바이너리 모드로 쓰기
# ab - 바이너리 모드로 파일 마지막에 추가하기