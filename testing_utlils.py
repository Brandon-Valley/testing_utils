''' [======- - - - -=================- All Utilities Standard -=================- - - - -======] '''
# to allow for relative imports
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], os.path.dirname(os.path.abspath(__file__))))
''' [======- - - - - - -=============- - - - -========- - - - -=============- - - - - - -======] '''

import json

def p_print(obj):
    print(json.dumps(obj, indent = 4))
    
    
    
    
if __name__ == '__main__':
    print('In Main:  testing_utils')
    
    d = {
        'A': 1,
        "b": [1,2,3,4],
        'v': 3}
    
    p_print(d)
    
    print('End of Main:  testing_utils')