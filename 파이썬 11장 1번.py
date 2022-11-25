filename= input("파일 이름을 입력하시오: ").strip() #파일 경로 입력
infile= open(filename, "r", encoding='UTF8')
count = 0

for line in infile: #여러 줄이 있을 경우 각 줄을 line이라는 변수에 저장함
    for ch in line:
        count += 1

print("파일 안에는 총", count, "개의 글자가 있습니다.")
infile.close()
