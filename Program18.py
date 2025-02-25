host = open("/Users/krunalb/Desktop/test1")
print(host)
print('Current Position of file >> {}'.format(host.tell()))
host_read = host.read()
print(host_read)
print('Current Position of file >> {}'.format(host.tell()))
host.seek(0)
print('Current Position of file >> {}'.format(host.tell()))

print('is File closed {}'.format(host.closed))

if not host.closed:
    host.close()

print('is File closed {}'.format(host.closed))

with open("/Users/krunalb/Desktop/test1") as hosts:
    print('File Opened')
    print('started Reading a file')
    readFile = hosts.read()
    print(readFile)
    print('is File Closed ? {}'.format(hosts.closed))

print('file read complete!')
print('is File Closed ? {}'.format(hosts.closed))