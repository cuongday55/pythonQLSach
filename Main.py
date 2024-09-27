from Book import Book
mangsach = []

def import_data(bookID ,bookName, bookAuthor , bookPageNumber , bookPublishing , bookYear):
   # print(type(bookID) ,type(bookName), type(bookAuthor) , type(bookPageNumber) , type(bookPublishing) , type(bookYear))
    std = Book(bookID ,bookName, bookAuthor , bookPageNumber , bookPublishing , bookYear)
    mangsach.append(std.__str__())

def add():
    std = Book()
    std.input()
    mangsach.append(std.__str__())
    

def menu():
    f = open("book_data.txt",mode = 'r',encoding = 'utf-8')
    sach = f.readlines()
    for i in range(0 , len(sach) , 1):
        tmp = sach[i].split("~")
        import_data(tmp[0] , tmp[1] , tmp[2] , int(tmp[3]) , tmp[4] , int(tmp[5]))
    f.close()
    while True:
        print("1. hien thi cac book trong ds:")
        print("2. tim sach theo keyword:")
        print("3. sap xep sach:")
        print("4. bo sung sach:")
        print("5. xoa sach:")
        print("6.thoat:")
        chon = int(input("nhap lua chon cua ban: "))
        if(chon == 1):
            print("toan bo sach trong danh sach!")    
            for i in mangsach:
                print(i , end="")
        if(chon == 2):
            print("tim kiem!")
            key = input("nhap keyword: ")
            isHas = True
            for i in range(0 , len(mangsach) , 1):
                index = mangsach[i].find(key)
                if(index >= 0):
                    print(mangsach[i])
                    isHas = False
            if(isHas):    
                print("khong tim thay!")
        if(chon == 3):
            mangSachSapXep = []
            print("1. sap xep theo ma sach:")    
            print("2. sap xep theo ten sach:")    
            print("3. sap xep theo ten tac gia:")    
            print("4. sap xep theo so trang:")    
            print("5. sap xep theo nha xuat ban:")    
            print("6. sap xep theo nam:")    
            sort = int(input("nhap lua chon cua ban: "))    
            for i in mangsach:
                tmp = i.split("~")
                mangSachSapXep.append(tmp)
            if(sort == 1):
                mangSachSapXep.sort(key=lambda x: x[0])  
            if(sort == 2):
                mangSachSapXep.sort(key=lambda x: x[1])  
            if(sort == 3):
                mangSachSapXep.sort(key=lambda x: x[2])  
            if(sort == 4):
                mangSachSapXep.sort(key=lambda x: x[3])  
            if(sort == 5):
                mangSachSapXep.sort(key=lambda x: x[4]) 
            if(sort == 6):
                mangSachSapXep.sort(key=lambda x: x[5])       
            print(mangSachSapXep)
        if(chon == 4):
            add()     
        if(chon == 5):
            index = int(input("nhap vi tri can xoa: "))
            del mangsach[index]
        if(chon == 6):
            print("ban muon lua roi thoat k?")
            print("1. thoat va lua")
            print("2. thoat va khong lua")
            exit = int(input("nhap lua chon: "))  
            if(exit == 1):
                f = open("book_data.txt", 'w')
                for i in mangsach:
                    f.write(i)
                f.close()
                quit()
            else:
                quit()

def main():
    menu()

main()