
def getData(Arduino):
    bs = Arduino.readline()
    bs = bs.replace(b'\n', b'').replace(b'\r', b'')
    bs = bs.decode("utf-8")
    if bs == '':
        bs=0
    i = int(bs)
    return i
