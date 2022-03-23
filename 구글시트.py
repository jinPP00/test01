# https://docs.gspread.org/en/latest/user-guide.html#opening-a-spreadsheet
# 새로운 스프레드 추가시 spreadsheet@spiritual-storm-330801.iam.gserviceaccount.com 공유.
import gspread
import pickle
import pandas as pd

# 구글시트 불러오기
def SheetLoad(myFile, myWorksheet):
  gc = gspread.service_account(filename="C:\\python\\workspace\\data\\spiritual-storm-330801-38127d4a8be0.json")
  sh = gc.open(myFile)
  worksheet = sh.worksheet(myWorksheet)
  df = pd.DataFrame(worksheet.get_all_records())
  return df, worksheet

# 구글시트 작성
def sheetWrite(myFile, myWorksheet, *values):
  df, worksheet = SheetLoad(myFile, myWorksheet)
  writeValue = []
  for i in values:
    writeValue.append(i)
  worksheet.append_row(writeValue)
  print("시트작성 성공", writeValue)

# last 업데이트
def SheetUpdate(myFile, myWorksheet, SheetData, updated_num):
  df, worksheet = SheetLoad(myFile, myWorksheet)
  for i in range(len(SheetData)):
    try:
      print(SheetData[i], updated_num[i])
      if str(SheetData[i]) == updated_num[i]:
        pass
      else:
        worksheet.update_acell(f'''D{i+2}''', updated_num[i])
        worksheet.update_acell(f'''E{i+2}''', "업데이트")
        print(updated_num[i],"시트 업데이트 성공")     
    except:
      print(i,"번째에서 오류")
      pass  

#피클 저장
def pickleSave(myFile, myWorksheet, savePickle):
  df, worksheet = SheetLoad(myFile, myWorksheet)
  # df = pd.DataFrame(worksheet.get_all_records())
  with open(f'''C:\\python\\workspace\\data\\{savePickle}.pickle''',"wb") as fw:
    pickle.dump(df, fw)
  print("피클 저장 완료", f'''./{savePickle}.pickle''')

#피클 링크 로드
def pickleload(loadPickle):
  with open(f'''C:\\python\\workspace\\data\\{loadPickle}.pickle''', 'rb') as f:
    df = pickle.load(f)
  return df

if __name__ == '__main__':
  pickleSave("크롤링완", "대출", "대출크롤링완")
  pickleSave("크롤링완", "페북", "페북크롤링완")
  pickleSave("크롤링완", "잡", "잡크롤링완")
  pickleSave("크롤링완", "크롤링실패", "크롤링실패")

  pickleSave("포스팅완", "대출", "대출포스팅완")
  pickleSave("포스팅완", "페북", "페북포스팅완")
  pickleSave("포스팅완", "잡", "잡포스팅완")
  pickleSave("포스팅완", "지원금", "지원금포스팅완")
  pickleSave("포스팅완", "실시간", "실시간포스팅완")
  pickleSave("포스팅완", "애드센스", "애드센스포스팅완")

  # df, df1 = pickleload("대출크롤링완"), pickleload("페북크롤링완")
  # print(df, df1)