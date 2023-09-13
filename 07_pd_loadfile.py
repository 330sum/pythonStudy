import pandas as pd

# read_csv()를 이용해 CSV 파일을 불러온다
file_path = "/Users/superstar_park/PycharmProjects/heroes.csv"
csv_data = pd.read_csv(file_path)

# 열 제목이 있는 형태로 데이터 5개를 출력한다
print(csv_data.head())


