infile = open("D:/test.txt", "r")  #打开文件
outfile = open("D:/pp2.txt", "w") # 内容输出
for line in infile:  #按行读文件，可避免文件过大，内存消耗        
      outfile.write(line.replace('    ', '    '))#first is old ,second is new
infile.close()    #文件关闭
outfile.close()