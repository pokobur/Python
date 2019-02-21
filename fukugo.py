#シーザー暗号を復号化するプログラムである。

#一文字先の文字にシフトしてる。
#一文字前の文字を見たい場合は、最後の行の文字列を見る。

def rot(data):
    for i in range(25):
        for j in range(len(data)):
            code = ord(data[j]) + 1
            if code <= 122:
                data = data[:j] + chr(code) + data[j+1:]
            else:
                data = data[:j] + chr(code - 26) + data[j+1:]
        print(data)
 
if __name__ == '__main__':
    data = input('文字列:')
    data = data.lower()
    rot(data)