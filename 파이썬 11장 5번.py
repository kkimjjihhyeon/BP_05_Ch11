infilename = input("입력 파일 이름: ") #입력 파일 경로 입력
outfilename = input("출력 파일 이름: ") #작성할 파일 경로 입력

infile = open(infilename,"r")
outfile = open(outfilename,"w")
ans = 0 # 숫자를 더해줄 변수를 만들었음
k = 0 # infile에 있는 숫자가 몇 개나 있는지 확인하는 변수를 만들었음

for line in infile:
    ans += float(line) #메모장에 적힌 숫자를 더해줌
    k += 1 #k에 1을 더해줘서 나중에 평균을 구할 때 사용함

#output 메모장에 합계와 평균을 적어줌
print("합계="+str(ans), file = outfile)
print("평균="+str(ans/k), file = outfile)

infile.close()
outfile.close()
