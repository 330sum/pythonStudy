import pandas as pd

# CSV 파일 읽기
csv_file_path = 'test.csv'  # CSV 파일 경로
df = pd.read_csv(csv_file_path)


# 엑셀 파일로 저장할 때, 최대 행 수를 고려해 나누기
max_rows = 1048576  # Excel의 최대 행 수
excel_file_path = 'test.xlsx'  # 저장할 엑셀 파일 경로

with pd.ExcelWriter(excel_file_path) as writer:
    num_parts = (len(df) // max_rows) + 1  # 필요한 시트 수 계산

    for i in range(num_parts):
        part_df = df.iloc[i * max_rows:(i + 1) * max_rows]
        part_df.to_excel(writer, sheet_name=f'Sheet{i + 1}', index=False)

print("CSV 파일이 엑셀 파일로 저장되었습니다.")