class Foo:
    def Bar(self):
        print ('BarTest')

    def Hello(self, name):
        print( 'hello my name is %s' % name)

obj = Foo()
obj.Bar()  
obj.Hello('Yaolu')