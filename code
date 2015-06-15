import web , os
from pybloom import BloomFilter
import cPickle as p
#crontab   30 21 * * * curl 127.0.0.1/save && curl 127.0.0.1/find?id=1@#@$@#$#$#%%

bloomplefile = 'bloom.ple'
urls = (
    '/save', 'Save' ,
    '/find', 'SomePage' ,
    '/init', 'Initfile'
)

exact=100000000
#1000000000 = 4G mem
#100000000 = 1.8G mem
#10000000 = 300M men



if os.path.isfile(bloomplefile):
    if os.stat(bloomplefile).st_size == 0:
        print ("file is empty!")
        bloomfilter = BloomFilter(capacity=exact, error_rate=1/float(exact))
    else:
        print ("file no empty!")
        f = file(bloomplefile)
        bloomfilter = p.load(f)
        f.close()
else:
    os.system(r'touch %s' % bloomplefile)
    print ("new file !")
    bloomfilter = BloomFilter(capacity=exact, error_rate=1/float(exact))

class SomePage:
    def GET(self):
        user_data = web.input()
        #bloom_result=user_data.id
        bloom_result= bloomfilter.add(user_data.id)
        # False is first data  , True is duplicate data!

        return str(bloom_result)

class Save:
    def GET(self):
        f = file(bloomplefile, 'w')
        p.dump(bloomfilter , f)             # dump the object to a file
        f.close()
        return "The object is saved !!!"

class Initfile:
    def GET(self):
        os.remove(bloomplefile)
        return "The file is removed !"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

