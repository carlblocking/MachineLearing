#coding=utf-8
import sys

def main(argv):
    file_path=sys.argv[1]
    save_path=sys.argv[2]
    f=open(file_path, 'rb')
    f1=open(save_path, 'w')
    lines=f.readlines()
    id=0
    new_line=""
    for line in lines:
        line=line.strip().decode()
        if "image_id" in line :
            id=0
            new_line+=line
        if "EO_parameters" in line:
            new_line+=("\t"+line)
            id=1
        if id==1:
            print(new_line)
            id=0
            f1.write(new_line+"\n")
            new_line=""
    f.close()
    f1.close()
    
    
if __name__=="__main__":
    main(sys.argv)
