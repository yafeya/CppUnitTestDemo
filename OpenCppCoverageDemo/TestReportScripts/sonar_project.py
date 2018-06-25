import os
import project_loader

loader = project_loader.ProjectLoader()
project_descriptor = loader.get_project_descriptor()
print('name: {arg1}'.format(arg1=project_descriptor.get_project_name()))
print('__________________________________________________')
for source_dir in project_descriptor.get_source_dirs():
    print('source directory: {arg1}'.format(arg1=source_dir))
print('__________________________________________________')
for test_app in project_descriptor.get_test_apps():
    print('test application: {arg1}'.format(arg1=test_app))
print('__________________________________________________')
for test_app_dir in project_descriptor.get_test_app_dirs():
    print('test application directory: {arg1}'.format(arg1=test_app_dir))

current_dir = os.curdir
project_bin_dir = project_descriptor.get_project_bin_dir()
reports_dir = 'reports'

os.chdir(project_bin_dir)
if not os.path.exists(reports_dir):
    os.mkdir(reports_dir)
os.system('lcov --directory . --zerocounters')