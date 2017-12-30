import pickle

val = "hello world!"
filename = "5.1.2.1.pickle"
pickle.dump( val, open( filename, "wb" ) )

print "Pickle object created. Filename:", filename
