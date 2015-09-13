import sys

code = open('code.in','rb').read()
data = open('data.in', 'rb').read()

namespace = {}
namespace['__builtins__'] = {'True':True, 'False':False, 'None':None, 'data':data}

exec code in namespace
