import pandas as pd

# read_csv()를 이용해 CSV 파일을 불러온다
file_path = "/Users/superstar_park/PycharmProjects/heroes.csv"
csv_data = pd.read_csv(file_path)

# 열 제목이 있는 형태로 데이터 5개를 출력한다
print(csv_data.head())

# 열 제목을 생성해서 CSV파일 불러오기
colums = ["인덱스", "이름", "체력", "포지션", "아이디"]

# 열 제목이 없는 CSV파일 불러오기
# 인덱스가 없도록 설정한 다음 nams 파라미터의 값을 columns로 설정
cav_data2 = pd.read_csv(file_path, header=None, names=colums)

# 열 제목이 있는 형태로 데이터 5개를 출력한다
print(cav_data2.head())
