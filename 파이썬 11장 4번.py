import pickle

#pickle모듈을 사용해 저장
outfile = open("test.dat", "wb") #저장장소 설정
pickle.dump(12, outfile)
pickle.dump(3.14, outfile)
pickle.dump([1, 2, 3, 4, 5], outfile)
outfile.close()


#pickle모듈을 사용해 읽기
infile = open("test.dat", "rb")#읽을파일 지정
print(pickle.load(infile))
print(pickle.load(infile))
print(pickle.load(infile))
infile.close()
