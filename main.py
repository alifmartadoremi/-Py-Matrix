__author__="kvda"

class myClass():
    def myFunc(self):
        barisInp = input("Masukkan jumlah baris : ")
        kolomInp = input("Masukkan jumlah kolom : ")
        print("")

        matriks = []

        offset = 0
        

        while offset<int(barisInp):
            offset2 = 0
            while offset2<int(kolomInp):
                Amatriks = input("Masukkan angka untuk baris {0} kolom {1} : ".format(offset+1,offset2+1))
                matriks.append(Amatriks)
                offset2+=1
            offset+=1
        
        print("Matriks yang telah anda buat : ")
        print(" ")
        offset = 0
        offsetMatriks = 0
        while offset<int(barisInp):
            offset2 = 0
            while offset2<int(kolomInp):
                print(matriks[offsetMatriks],end=" ")
                offsetMatriks+=1
                offset2+=1
            print(" ")
            offset+=1
            
        
if __name__ == '__main__':
    myClass().myFunc()