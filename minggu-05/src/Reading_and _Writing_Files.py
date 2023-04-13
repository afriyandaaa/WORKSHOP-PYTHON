#..Reading and Writing Files..##
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()
    print(read_data)
    # Kami dapat memeriksa apakah file telah ditutup secara otomatis.
    print(f.closed)
    print(f.close())
    f.read()
    print("---------------")
   
##..Methods of File Objects..##
    f.read()
    f.read()
    f.readline()
    f.readline()
    f.readline()
    for line in f:
        print(line, end='')
    f.write('This is a test\n')
    value = ('the answer', 42)
    s = str(value)  # ubah tuple menjadi string
    f.write(s)
    f = open('workfile', 'rb+')
    f.write(b'0123456789abcdef')
    f.seek(5)      # Pergi ke byte ke-6 dalam file
    f.read(1)
    f.seek(-3, 2)  # Pergi ke byte ke-3 sebelum akhir
    f.read(1)

##..Saving structured data with json..##
import json
x = [1, 'simple', 'list']
print(json.dumps(x))
