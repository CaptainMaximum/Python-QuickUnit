import quickunitlib as quickunit

@quickunit.NotEqual(0,5,5)
@quickunit.NoException(5,0) # This one will fail
@quickunit.Equal(1,5,5)
def Divide(a,b):
    return (a / b)
