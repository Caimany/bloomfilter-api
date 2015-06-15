import web , os ,json
from pybloom import BloomFilter
import cPickle as p
#crontab   30 21 * * * curl 127.0.0.1/save && curl 127.0.0.1/find?id=1@#@$@#$#$#%%

bloomplefile = 'bloom.ple'
urls = (
    '/save', 'Save' ,
    '/bloom', 'Bloom' ,
    '/init', 'Initfile'
)

exact=10000000
#1000000000 = 4G mem
#100000000 = 1.8G mem
#10000000 = 300M men



if os.path.isfile(bloomplefile):
    if os.stat(bloomplefile).st_size == 0:
        print ("file is empty!")
        bloomfilter = BloomFilter(capacity=exact, error_rate=1/float(exact))
    else:
        print ("file no empty , wait for loading.....")
        f = file(bloomplefile)
        bloomfilter = p.load(f)
        f.close()
else:
    os.system(r'touch %s' % bloomplefile)
    print ("new file !")
    bloomfilter = BloomFilter(capacity=exact, error_rate=1/float(exact))

class Bloom:
    def GET(self):
        user_data = web.input()
        #bloom_result=user_data.id
        bloom_result= bloomfilter.add(user_data.id)
        # False is first data  , True is duplicate data!

        # return "<h1>" + str(bloom_result) + "</h1>"
        return_info = [{'boolean' : bloom_result}]
        return json.dumps(return_info)

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

