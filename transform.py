# file="D:\PycharmProjects\\fastspeech\\tensor2tensor-speech\data\ljspeech\LJSpeech-1.1\metadata_phone.txt"
# fp = open(file,"r")
# lines=fp.readlines()
# for i in range(0,20,2):
#     print(lines[i].strip().split("m"))
"""while(not EOF):
    a=fp.readline
    remove {#number} using re
    replace "," with " " can this be good?
    use , to seperate text and number

    newfile.write(a)

    b=fp.readline
    b.strip()
    b.replace(" ") with " | "
    newfile.write(b)

    newfile.close
"""
# #我懂了，中文的标点符号仍旧使用中文，这样就不会造成csv的格式错误了！
import re
filepath=r"/mnt/guanyu/tensor2tensor-speech/newdata/LJSpeech-1.1/metadata_phone.txt"
fp = open(filepath,"r")
b=fp.readlines()
length=len(b)
with open(r"/mnt/guanyu/tensor2tensor-speech/newdata/LJSpeech-1.1/metadata_phone.csv","w") as written_file:
    written_file.write("wav,txt2,phone2\n")
    for i in range(0,length,2):
        number_and_text=b[i]
        number_and_text=number_and_text.strip()
        number_and_text=number_and_text.split("\t")
        text = re.sub("#\d","",number_and_text[1])
        number_and_text[1]=text
        phone=b[i+1]
        phone=phone.strip().replace(" "," | ")
        written_string=number_and_text[0]+","+number_and_text[1]+","+phone+"\n"
        written_file.write(written_string)
    written_file.close()




