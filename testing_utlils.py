''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Header -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
import sys, os    ;     sys.path.insert(1, os.path.join(sys.path[0], os.path.dirname(os.path.abspath(__file__)))) # to allow for relative imports, delete any imports under this line

util_submodule_l = ['exception_utils', 'txt_logger'] # list of all imports from local util_submodules that could be imported elsewhere to temporarily remove from sys.modules

# temporarily remove any modules that could conflict with this file's local util_submodule imports
og_sys_modules = sys.modules    ;    pop_l = [] # save the original sys.modules to be restored at the end of this file
for module_descrip in sys.modules.keys():  
    if any( util_submodule in module_descrip for util_submodule in util_submodule_l )    :    pop_l.append(module_descrip) # add any module that could conflict local util_submodule imports to list to be removed from sys.modules temporarily
for module_descrip in pop_l    :    sys.modules.pop(module_descrip) # remove all modules put in pop list from sys.modules
util_submodule_import_check_count = 0 # count to make sure you don't add a local util_submodule import without adding it to util_submodule_l

''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard: Local Utility Submodule Imports  -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''

from util_submodules .exception_utils import exception_utils as eu    ; util_submodule_import_check_count += 1 
from util_submodules .logger          import txt_logger               ; util_submodule_import_check_count += 1 
    
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if util_submodule_import_check_count != len(util_submodule_l)    :    raise Exception("ERROR:  You probably added a local util_submodule import without adding it to the util_submodule_l")
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''


import json



TEMP_FILE_PATH = 'temp.txt'


    
# Full Pretty Print
# if no title given, obj_from_title_indent set to 0
# passing func as obj or title Ex:  fp_print((lambda: p_func("hi", 3))
def fp_print(obj, title = None, log_file_path = None, log_write_mode = 'overwrite', print_indent = 0, obj_from_title_indent = 0, json_indent = 4, print_output = True):
    eu.error_if_param_type_not_in_whitelist( log_file_path          , ['NoneType' , 'str'])
    eu.error_if_param_key_not_in_whitelist ( log_write_mode         , ['overwrite', 'append'])    
    eu.error_if_param_type_not_in_whitelist( print_indent           , ['int'])
    eu.error_if_param_type_not_in_whitelist( obj_from_title_indent  , ['int'])
    eu.error_if_param_type_not_in_whitelist( json_indent            , ['int'])
    eu.error_if_param_type_not_in_whitelist( print_output           , ['bool'])
    eu.error_if_forbidden_param_val_combo({log_file_path : None, print_output : False}, reason = "If you arn't logging or printing, this function does nothing")
    
    
    # Ex: lines = get_func_print_as_line_tup(lambda: p_func("hi", 3))
    def get_func_print_as_line_tup(func):
        orig_stdout = sys.stdout
        f = open(TEMP_FILE_PATH, 'w')
        sys.stdout = f

        func()
         
        sys.stdout = orig_stdout
        f.close()
        
        with open(TEMP_FILE_PATH) as textFile:  # can throw FileNotFoundError
            line_tup = tuple(l.rstrip() for l in textFile.readlines())
        
        os.remove(TEMP_FILE_PATH)
        
        return line_tup
    

#     
    # if obj or title are functions, reset them as their print outputs
    # treat single line printed outputs of functions like strings, not lists
    if callable(obj):
        obj   = get_func_print_as_line_tup(obj)
        if len(obj) == 1:
            obj = obj[0]
    if callable(title):
        title = get_func_print_as_line_tup(title)
        if len(title) == 1:
            title = title[0]
#         print(' in testing utils, title after convert:  ', title)#``````````````````````````````````````````````````````````````````````````````
        
        
    # indents
    if title == None:
        obj_from_title_indent = 0
    
    print_indent_str          = ' ' * print_indent
    obj_from_title_indent_str = ' ' * obj_from_title_indent
    
    out_str = ''
    
    # add title to out_str
    if title != None:
        dump = json.dumps(title, indent = json_indent)
#         print('title dump: ', dump)#`````````````````````````````````````````````````````````````````````
        dump_line_l = dump.split('\n')
#         print('title dump_line_l: ', dump_line_l)#`````````````````````````````````````````````````````````````````````

          
        for line in dump_line_l:
            out_str += print_indent_str + line + '\n'
        
        
    # add obj to out_str   
    dump = json.dumps(obj, indent = json_indent)
    dump_line_l = dump.split('\n')
    
    for line in dump_line_l:
        out_str += print_indent_str + obj_from_title_indent_str + line + '\n'
        
    # log file if needed
    if log_file_path != None:
        txt_logger.write(out_str, log_file_path, write_mode = log_write_mode)
        
    # print if needed
    if print_output:
        print(out_str)
        
        
      
''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''
'''                                                                           
        Simple Functions For Quick Auto-Complete
'''
''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''
    
# prefix order: i, t, m

# prints
def p_print  (obj)                : fp_print(obj, json_indent = 4) # Pretty Print
def tp_print (obj, title)         : fp_print(obj, json_indent = 4, title = title, obj_from_title_indent = 4) # Titled Pretty Print
def ip_print (obj,        indent) : fp_print(obj, json_indent = 4, print_indent = indent) # Indented Pretty Print
def itp_print(obj, title, indent) : fp_print(obj, json_indent = 4, title = title, obj_from_title_indent = 4, print_indent = indent) # Indented Titled Pretty Print

# logs
def o_log   (obj,                     log_file_path):              fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'overwrite', print_output = False) # Overwrite Log
def a_log   (obj,                     log_file_path):              fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'append'   , print_output = False) # Append Log
                                                                   
def to_log  (obj,      title,         log_file_path):              fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'overwrite', print_output = False, obj_from_title_indent = 4, title = title) # Titled Overwrite Log
def ta_log  (obj,      title,         log_file_path):              fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'append'   , print_output = False, obj_from_title_indent = 4, title = title) # Titled Append Log
                                                                   
def io_log  (obj,             indent, log_file_path):              fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'overwrite', print_output = False, obj_from_title_indent = 4, print_indent = indent) 
def ia_log  (obj,             indent, log_file_path):              fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'append'   , print_output = False, obj_from_title_indent = 4, print_indent = indent) 
                                                                   
def ito_log (obj,      title, indent, log_file_path):              fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'overwrite', print_output = False, obj_from_title_indent = 4, title = title, print_indent = indent) 
def ita_log (obj,      title, indent, log_file_path):              fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'append'   , print_output = False, obj_from_title_indent = 4, title = title, print_indent = indent) 

# logs that print a given message 
def mo_log  (obj, msg,                log_file_path): print(msg) ; fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'overwrite', print_output = False) # Message Overwrite Log
def ma_log  (obj, msg,                log_file_path): print(msg) ; fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'append'   , print_output = False) # Message Append Log

def mto_log (obj, msg, title,         log_file_path): print(msg) ; fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'overwrite', print_output = False, obj_from_title_indent = 4, title = title) # Titled Overwrite Log
def mta_log (obj, msg, title,         log_file_path): print(msg) ; fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'append'   , print_output = False, obj_from_title_indent = 4, title = title) # Titled Append Log
                                                      
def mio_log (obj, msg,        indent, log_file_path): print(msg) ; fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'overwrite', print_output = False, obj_from_title_indent = 4, print_indent = indent) 
def mia_log (obj, msg,        indent, log_file_path): print(msg) ; fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'append'   , print_output = False, obj_from_title_indent = 4, print_indent = indent) 
                                                       
def mito_log(obj, msg, title, indent, log_file_path): print(msg) ; fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'overwrite', print_output = False, obj_from_title_indent = 4, title = title, print_indent = indent) 
def mita_log(obj, msg, title, indent, log_file_path): print(msg) ; fp_print(obj, json_indent = 4, log_file_path = log_file_path, log_write_mode = 'append'   , print_output = False, obj_from_title_indent = 4, title = title, print_indent = indent) 



    
    
    
    
    
    
# DONT DELETE UNTIL TRY TO MAKE REFLECTION VAR PRINT FUNC !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import inspect
# # call from inside a function passing the name of the function as a str to get a 
# # string describing the names and values of the functions parameters
# def get_param_vals_str_of_last_func_call(func_name):
# #         print(inspect.stack())#````````````````````````````````````````````````````````````````````````````
#     s_stack = str(inspect.stack()).split(func_name)
#     if len(s_stack) > 0:
#         last_slice = s_stack[-1]
# #         param_str = last_slice.split(',\n"index=')[0]
#         param_str_with_backslash = last_slice.split("n'], index=")[0]
#         param_str = param_str_with_backslash[1:-2]
# #             param_str_l = list(param_str)
# #         param_str = last_slice.split(")\n'], index=")[0]
# #         param_str = last_slice.split("index=")[0]
#         print('param_str: ', param_str)#```````````````````````````````````````````````````````````````````````````````````
# #             print('param_str_l: ', param_str_l)#```````````````````````````````````````````````````````````````````````````````````
#     return param_str
# 
#  
# def gat_var_name(var):
#         """
#         Gets the name of var. Does it from the out most frame inner-wards.
#         :param var: variable to get name from.
#         :return: string
#         """
#         print('stack: ', inspect.stack())
#         for fi in reversed(inspect.stack()):
#             names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
#             if len(names) > 0:
#                 return names[0]
    
    
    
    
''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Footer -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
sys.modules = og_sys_modules
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if __name__ == '__main__':
    print('In Main:  testing_utils')
    log_path = "C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\svn_to_git_ip_repo\\test_log.txt"
    
    TEMP_FILE_PATH = 'temp.txt'
    
    # use like: lines = get_func_print_as_line_tup(lambda: p_func("hi", 3))
    def get_func_print_as_line_tup(func):
        orig_stdout = sys.stdout
        f = open(TEMP_FILE_PATH, 'w')
        sys.stdout = f

        func()
         
        sys.stdout = orig_stdout
        f.close()
        
        with open(TEMP_FILE_PATH) as textFile:  # can throw FileNotFoundError
            line_tup = tuple(l.rstrip() for l in textFile.readlines())
        
        os.remove(TEMP_FILE_PATH)
        
        return line_tup
        
                
        
    
    def p_func(str_to_print, num):
        for x in range(num):
            print(str_to_print)
            
            
    p_func("hi", 3)
    
    str = get_func_print_as_line_tup(lambda: p_func("hi", 3))
    
    print('str VVVVVVVVVVVVVVV')
    print(str)
#     print(type(p_func))
# 
#     print(type(p_func) == "<class 'function'>")
# #     print(str(type(p_func)).split("'")[1] == 'function')
# 
#     type_str = str(type(p_func)).split("'")[1]
#     print(type_str)
    fp_print(lambda: p_func("hi", 3), title = lambda: p_func("bro", 3))#, log_file_path, log_write_mode, print_indent, obj_from_title_indent, json_indent, print_output)
    tp_print(lambda: p_func("hi", 3), title = lambda: p_func("bro", 3))#, log_file_path, log_write_mode, print_indent, obj_from_title_indent, json_indent, print_output)
    ta_log(lambda: p_func("hi", 3), title = lambda: p_func("bro", 3), log_file_path = "C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\repo_transfer_out.txt")
#     print
    
# #     log_path = "C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\dir_that_does_not_exist\\test_log.txt"
# #     p_print(['C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\testing_utils', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\file_system_utils', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\logger', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\subprocess_utils', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\exception_utils', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\..\\..', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\git_tools', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\git_tools', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\..\\..', 'C:\\Users\\mt204e\\Development\\Eclipse_2019-06\\eclipse\\plugins\\org.python.pydev.core_7.5.0.202001101138\\pysrc', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts', 'C:\\Users\\mt204e\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs', 'C:\\Users\\mt204e\\AppData\\Local\\Programs\\Python\\Python37-32\\lib', 'C:\\Users\\mt204e\\AppData\\Local\\Programs\\Python\\Python37-32', 'C:\\Users\\mt204e\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages', 'C:\\Users\\mt204e\\AppData\\Local\\Programs\\Python\\Python37-32\\python37.zip'])
#     
# #     print(len(l))
# #     p_print(l)
# #     
#     d = {
#         'A': 1,
#         "b": [1,2,3,4],
#         'v': 3}
# #     
# #     p_print(d)
# #     
# #     
# #     fp_print(d, title = 'Print Title', log_file_path = log_path, log_write_mode = 'overwrite', print_indent = 5, json_indent = 4, print_output = True)
# #     fp_print("hi this is a string", title = 'Print Title', log_file_path = log_path, log_write_mode = 'append', obj_from_title_indent = 4, print_indent = 5, json_indent = 4, print_output = True)
# #     fp_print("hi this is a string", title = 'Print Title', log_file_path = log_path, log_write_mode = 'append', obj_from_title_indent = 4, print_indent = 5, json_indent = 4, print_output = "sodfnos")
# 
#     tp_print(d, "tiltle:")
#     itp_print(d, "tiltle:", 4)
# #     ip_print('hhiasodf', 4)
#     
#     
#     ma_log(d, 'logging d...', log_path)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print('End of Main:  testing_utils')