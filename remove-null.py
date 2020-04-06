import sys

fi = open(sys.argv[1], 'rb')
data = fi.read()
fi.close()
fo = open(sys.argv[1], 'wb')
fo.write(data.replace('\x00', ''))
fo.close()
