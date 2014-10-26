'''
Created on Jun 6, 2014

@author: tanmaymehrotra
'''

print "I am in %(s)s city %(s)s" % {"s" :"New_york"}

def print_range(*args):
    print range(*args)

if __name__== "__main__":
    print_range(10,20)
    
    if None:
        print "tanmay"
    else:
        print "mehrotra"