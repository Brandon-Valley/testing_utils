''' [======- - - - -=================- All Utilities Standard -=================- - - - -======] '''
# to allow for relative imports
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], os.path.dirname(os.path.abspath(__file__))))
''' [======- - - - - - -=============- - - - -========- - - - -=============- - - - - - -======] '''

# print('sys_path:  ', sys.path)#`````````````````````````````````````````````````````````````````````````````````````
og_sys_path = sys.path
sys.path = [os.path.join(sys.path[0], os.path.dirname(os.path.abspath(__file__)))]

print('sys_path: ', sys.path)#````````````````````````````````````````````````````````````````````````````````````````````)

for path in og_sys_path:
#     if any(elm in path for elm in ['\\Python\\Python', '\\eclipse\\plugins\\']):
    if '\\Python\\Python' in path or '\\eclipse\\plugins\\' in path:
        sys.path.append(path)
        print('just added to sys.path:  ', path)
        
        
        
# print('sys_path: ', sys.path)#````````````````````````````````````````````````````````````````````````````````````````````)
print('before imports:\n[')
for path in sys.path:
    print('  ', path)
print(']')

# print('setting testing utils as cwd')
# import os
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
from util_submodules.logger import txt_logger 
# from util_submodules.logger import logger 
from util_submodules.logger import test_import
from test_submodules.test_module_dir import test_module
from util_submodules.exception_utils import exception_utils as eu
from util_submodules.exception_utils import exception_utils


# print('sys_path: ', sys.path)#````````````````````````````````````````````````````````````````````````````````````````````)
print('after imports:\n[')
for path in sys.path:
    print('  ', path)
print(']')


print('test_import.TEST_VAR: ', test_import.TEST_VAR)

# eu.error_if_param_invalid('THIS SHOULD RAISE ERROR', ['overwrite', 'append'])

# sys.path = og_sys_path

# eu.error_if_param_invalid('THIS SHOULD RAISE ERROR', ['overwrite', 'append'])


#         tu.print_me(proj_ver_change_dl, title = commit.abrv_commit_hash, to_file = 'multi_ver_commits.txt', to_file_write_mode = 'append')


import json
    
    
# Full Pretty Print
def fp_print(obj, title = None, log_file_path = None, log_write_mode = 'overwrite', print_indent = 0, json_indent = 4, print_output = True):
    eu.error_if_param_invalid(log_write_mode, ['overwrite', 'append'])
    
    print(sys.path)#```````````````````````````````````````````````````````````````````````````````````````````)
    eu.error_if_forbidden_param_val_combo({log_file_path : None, print_output : False}, reason = "If you arn't logging or printing, this function does nothing")
#     if log_file_path == None and print_output == False:
#         raise eu.IncompatibleParamsError("")
    
    
    print_indent_str = ' ' * print_indent
    
    
    out_str = ''
    
    if title != None:
        out_str += print_indent_str + title + '\n'
        
    dump = json.dumps(obj, indent = json_indent)
    dump_line_l = dump.split('\n')
    
    for line in dump_line_l:
        out_str += print_indent_str + line + '\n'
        
    if log_file_path != None:
        txt_logger.write(out_str, log_file_path, write_mode = 'overwrite')
        
      
    
    
    
# Pretty Print
# keep this one simple for quick auto-complete
def p_print(obj):
    print(json.dumps(obj, indent = 4))
#     fp_print(obj, json_indent = 4)
    
    
    
    
    
sys.path = og_sys_path 
if __name__ == '__main__':
    print('In Main:  testing_utils')
    p_print(['C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\testing_utils', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\file_system_utils', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\logger', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\subprocess_utils', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\exception_utils', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\..\\..', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\git_tools', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\git_tools', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\..\\..', 'C:\\Users\\mt204e\\Development\\Eclipse_2019-06\\eclipse\\plugins\\org.python.pydev.core_7.5.0.202001101138\\pysrc', 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts', 'C:\\Users\\mt204e\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs', 'C:\\Users\\mt204e\\AppData\\Local\\Programs\\Python\\Python37-32\\lib', 'C:\\Users\\mt204e\\AppData\\Local\\Programs\\Python\\Python37-32', 'C:\\Users\\mt204e\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages', 'C:\\Users\\mt204e\\AppData\\Local\\Programs\\Python\\Python37-32\\python37.zip'])
    
#     l = '''[FrameInfo(frame=<frame at 0x0414E300, file 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\testing_utils\\util_submodules\\exception_utils\\exception_utils.py', line 19, code gat_var_name>, filename='C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\testing_utils\\util_submodules\\exception_utils\\exception_utils.py', lineno=19, function='gat_var_name', code_context=["        print('stack: ', inspect.stack())\n"], index=0), FrameInfo(frame=<frame at 0x0413F498, file 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\testing_utils\\util_submodules\\exception_utils\\exception_utils.py', line 51, code error_if_forbidden_param_val_combo>, filename='C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\testing_utils\\util_submodules\\exception_utils\\exception_utils.py', lineno=51, function='error_if_forbidden_param_val_combo', code_context=["                msg += '\\n' + gat_var_name(param) + ' == ' + str(value)\n"], index=0), FrameInfo(frame=<frame at 0x04C45030, file 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\testing_utils\\testing_utlils.py', line 21, code fp_print>, filename='C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\testing_utils\\testing_utlils.py', lineno=21, function='fp_print', code_context=['    eu.error_if_forbidden_param_val_combo({log_file_path : None, print_output : False}, reason = "If you arn\'t logging or printing, this function does nothing")\n'], index=0), FrameInfo(frame=<frame at 0x040A6690, file 'C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\testing_utils\\testing_utlils.py', line 70, code <module>>, filename='C:\\Users\\mt204e\\Documents\\projects\\Bitbucket_repo_setup\\bitbucket_repo_setup_scripts\\submodules\\testing_utils\\testing_utlils.py', lineno=70, function='<module>', code_context=["    fp_print(d, title = 'Print Title', log_file_path = None, log_write_mode = 'overwrite', print_indent = 5, json_indent = 4, print_output = False)\n"], index=0), FrameInfo(frame=<frame at 0x0412EAE8, file 'C:\\Users\\mt204e\\Development\\Eclipse_2019-06\\eclipse\\plugins\\org.python.pydev.core_7.5.0.202001101138\\pysrc\\_pydev_imps\\_pydev_execfile.py', line 25, code execfile>, filename='C:\\Users\\mt204e\\Development\\Eclipse_2019-06\\eclipse\\plugins\\org.python.pydev.core_7.5.0.202001101138\\pysrc\\_pydev_imps\\_pydev_execfile.py', lineno=25, function='execfile', code_context=['    exec(compile(contents+"\\n", file, \'exec\'), glob, loc)\n'], index=0), FrameInfo(frame=<frame at 0x03F72CB0, file 'C:\\Users\\mt204e\\Development\\Eclipse_2019-06\\eclipse\\plugins\\org.python.pydev.core_7.5.0.202001101138\\pysrc\\pydevd.py', line 2202, code _exec>, filename='C:\\Users\\mt204e\\Development\\Eclipse_2019-06\\eclipse\\plugins\\org.python.pydev.core_7.5.0.202001101138\\pysrc\\pydevd.py', lineno=2202, function='_exec', code_context=['            pydev_imports.execfile(file, globals, locals)  # execute the script\n'], index=0), FrameInfo(frame=<frame at 0x03E55E30, file 'C:\\Users\\mt204e\\Development\\Eclipse_2019-06\\eclipse\\plugins\\org.python.pydev.core_7.5.0.202001101138\\pysrc\\pydevd.py', line 2195, code run>, filename='C:\\Users\\mt204e\\Development\\Eclipse_2019-06\\eclipse\\plugins\\org.python.pydev.core_7.5.0.202001101138\\pysrc\\pydevd.py', lineno=2195, function='run', code_context=['        return self._exec(is_module, entry_point_fn, module_name, file, globals, locals)\n'], index=0), FrameInfo(frame=<frame at 0x03EF7588, file 'C:\\Users\\mt204e\\Development\\Eclipse_2019-06\\eclipse\\plugins\\org.python.pydev.core_7.5.0.202001101138\\pysrc\\pydevd.py', line 3122, code main>, filename='C:\\Users\\mt204e\\Development\\Eclipse_2019-06\\eclipse\\plugins\\org.python.pydev.core_7.5.0.202001101138\\pysrc\\pydevd.py', lineno=3122, function='main', code_context=["        globals = debugger.run(setup['file'], None, None, is_module)\n"], index=0), FrameInfo(frame=<frame at 0x01652960, file 'C:\\Users\\mt204e\\Development\\Eclipse_2019-06\\eclipse\\plugins\\org.python.pydev.core_7.5.0.202001101138\\pysrc\\pydevd.py', line 3129, code <module>>, filename='C:\\Users\\mt204e\\Development\\Eclipse_2019-06\\eclipse\\plugins\\org.python.pydev.core_7.5.0.202001101138\\pysrc\\pydevd.py', lineno=3129, function='<module>', code_context=['    main()\n'], index=0)]'''.split(', ')
#     print(len(l))
#     p_print(l)
#     
    d = {
        'A': 1,
        "b": [1,2,3,4],
        'v': 3}
#     
#     p_print(d)
#     
#     
    fp_print(d, title = 'Print Title', log_file_path = None, log_write_mode = 'overwrite', print_indent = 5, json_indent = 4, print_output = False)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print('End of Main:  testing_utils')