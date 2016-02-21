equal_passes = {} 
notequal_passes = {}
noexcept_passes = {}

waitlist = []

class qunitBase(object):
    # The arguments that a function decorator is called with will be passed to
    # the init function of this class.  These args will be used to call the
    # decorated function with
    def __init__(self, *args):
        self.args = args
        self.decorator = None

    # This call function is the actual Python decorator function call.  It does
    # not actually call the function yet.  Instead it logs the function to call
    # as an object member, and it adds 'self' to a waiting list of tests to
    # execute.  This decouples the execution of tests from any type of decision
    # of HOW the tests should be executed (Run tests in a certain order, in
    # parallel, etc)
    def __call__(self, f):
        self.f = f
        self.name = f.__name__
        if f.func_closure:
            decorated_function = f.func_closure[0].cell_contents
            self.decorator = f.func_name
            self.name = '@%s:%s' %(self.decorator, decorated_function.func_name)
        waitlist.append(self)
        return f

# Tests whether calling a function with certain values raises an exception
class NoException(qunitBase):
    def test(self):
        try:
            self.f(*self.args)
            noexcept_passes[str(self)] = True
        except Exception as e:
            noexcept_passes[str(self)] = str(e)

    def __str__(self):
        name = self.name
        args = ','.join([str(x) for x in self.args])
        return '%s(%s)' %(name,args)

# Tests the output of a function for equality to an expected value
class Equal(qunitBase):
    def __init__(self, expect, *args):
        qunitBase.__init__(self, *args)
        self.expect = expect

    def test(self):
        try:
            out = self.f(*self.args)
            equal_passes[str(self)] = (self.expect == out)
        except Exception as e:
            equal_passes[str(self)] = str(e)

    def __str__(self):
        name = self.name
        expect = str(self.expect)
        args = ','.join([str(x) for x in self.args])
        return '%s(%s,%s)' %(name,expect,args)

# Tests the output of a function for inequality to an unexpected value
class NotEqual(qunitBase):
    def __init__(self, expect, *args):
        qunitBase.__init__(self, *args)
        self.notexpect = expect

    def test(self):
        try:
            out = self.f(*self.args)
            notequal_passes[str(self)] = (self.notexpect != out)
        except Exception as e:
            notequal_passes[str(self)] = str(e)

    def __str__(self):
        name = self.name
        notexpect = str(self.notexpect)
        args = ','.join([str(x) for x in self.args])
        return '%s(%s,%s)' %(name,notexpect,args)

# Basic reporting of unit test results.  Will probably be improved later.
def report():
    print "NoExcept: ", noexcept_passes
    print "Equal: ", equal_passes
    print "Not Equal: ", notequal_passes
