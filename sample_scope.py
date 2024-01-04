def checkscope() :
    def do_local() :
        test ='local'
    def do_non_local() :
        nonlocal test
        test ='non local test'
    def do_global() :
        global test
        test = 'global'

    test = 'default'
    do_local()
    print('Value after local ' +test)
    do_non_local()
    print('Value after local ' + test)
    do_global()
    print('Value after local ' + test)

checkscope()
print('test value after main' +test)

