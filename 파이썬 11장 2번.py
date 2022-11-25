filename = input("파일 이름을 입력하세오: ") #파일 경로 입력
infile = open(filename,"r")
read_file = infile.readlines()

outfile = open(filename, "w")
del_word = input("삭제할 문자열을 입력하시오: ")#삭제할 문자열 입력

for line in read_file: #여러 줄이 있으면 한 줄씩 처리함
    l, r = 0, len(del_word)
    new_line = "" #삭제하지 않아도 되는 문자열을 저장함
    while l < len(line): #while문으로 삭제할 단어를 찾아냄
        if line[l:r] == del_word: #만약 삭제할 단어가 있을 경우
            l += len(del_word)
            r += len(del_word)
        else: #삭제할 단어가 아닌 경우
            new_line += line[l]
            l+=1
            r+=1
    print(new_line, file = outfile, end="") #new_line에 저장한 문자열을 outfile에 작성해줌

infile.close()
outfile.close()
print("변경된 파일이 저장되었습니다.")
