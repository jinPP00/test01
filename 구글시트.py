# https://docs.gspread.org/en/latest/user-guide.html#opening-a-spreadsheet
# 새로운 스프레드 추가시 spreadsheet@spiritual-storm-330801.iam.gserviceaccount.com 공유.
import gspread
import pickle
import pandas as pd

# 구글시트 불러오기
def SheetLoad(myFile, myWorksheet):
  gc = gspread.service_account(filename="./data/spiritual-storm-330801-38127d4a8be0.json")
  sh = gc.open(myFile)
  worksheet = sh.worksheet(myWorksheet)
  df = pd.DataFrame(worksheet.get_all_records())
  return df, worksheet

if __name__ == '__main__':
  df, worksheet = SheetLoad("실시간크롤링", "TV")
