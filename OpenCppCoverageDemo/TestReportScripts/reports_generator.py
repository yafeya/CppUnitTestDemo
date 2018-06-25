import project_loader
import reports_info
import os


class ReportsGenerator:
    __project_descriptor__ = None
    __reports_info__ = None
    __solution_dir__ = ''
    __project_bin_dir__ = ''
    __reports_dir__ = ''
    __project_name__ = ''

    def __init__(self):
        loader = project_loader.ProjectLoader()
        self.__project_descriptor__ = loader.get_project_descriptor()
        self.__reports_info__ = reports_info.ReportsInfo()

        self.__solution_dir__ = os.path.abspath(self.__project_descriptor__ .get_solution_dir())
        self.__project_bin_dir__ = self.__project_descriptor__ .get_project_bin_dir()
        self.__reports_dir__ = os.path.join(self.__project_bin_dir__, 'reports')
        self.__project_name__ = self.__project_descriptor__ .get_project_name()

    def __generate_reports_dir__(self):
        if not os.path.exists(self.__reports_dir__):
            os.mkdir(self.__reports_dir__)

    def __clear_former_results__(self):
        os.system('lcov --directory {arg1} --zerocounters'.format(arg1=self.__project_bin_dir__))

    def __generate_base_report__(self):
        base_report = os.path.join(self.__project_bin_dir__, '{arg1}.base'.format(arg1=self.__project_name__))
        os.system('lcov -c -i -d {arg1} -o {arg2}'.format(arg1=self.__project_bin_dir__, arg2=base_report))

    def __generate_test_reports__(self):
        test_apps = self.__project_descriptor__.get_test_apps()
        for test_app in test_apps:
            parent_dir = os.path.dirname(test_app)
            if not parent_dir.endswith('/'):
                parent_dir += '/'
            test_name = test_app.replace(parent_dir, '')
            test_report_name = os.path.join(self.__reports_dir__, '{arg1}_report.xml'.format(arg1=test_name))
            os.system('{arg1} --gtest_output=xml:{arg2}'.format(arg1=test_app, arg2=test_report_name))
            self.__reports_info__.test_reports.append(test_report_name)

    def __generate_info_report__(self):
        os.system('lcov --directory . --capture --output-file {arg1}.info'.format(arg1=self.__project_name__))

    def __generate_gcovr_report__(self):
        gcovr_report = os.path.join(self.__reports_dir__, 'gcovr_report.xml')
        os.system('gcovr -x -r {arg1} > {arg2}'.format(arg1=self.__solution_dir__, arg2=gcovr_report))
        self.__reports_info__.coverage_report = gcovr_report

    def __generate_cpp_check_report__(self):
        compile_commands_file = os.path.join(self.__project_bin_dir__, 'compile_commands.json')
        cpp_check_report = os.path.join(self.__reports_dir__, 'cppcheck_report.xml')
        os.system('cppcheck --project={arg1} --xml-version=2 2> {arg2}'
                  .format(arg1=compile_commands_file, arg2=cpp_check_report))
        self.__reports_info__.cpp_check_report = cpp_check_report

    def generate_reports(self):
        self.__generate_reports_dir__()

        print('start to clear gcov/lcov former result...')
        self.__clear_former_results__()
        print('clear gcov/lcov former result finished...')

        print('start to generate .base report...')
        self.__generate_base_report__()
        print('generate .base report finished...')

        print('start to generate unit-test report...')
        self.__generate_test_reports__()
        print('generate unit-test report finished...')

        print('start to generate .info report...')
        self.__generate_info_report__()
        print('generate .info report finished...')

        print('start to generate gcovr report...')
        self.__generate_gcovr_report__()
        print('generate gcovr report finished...')

        print('start to generate cpp-check report...')
        self.__generate_cpp_check_report__()
        print('generate cpp-check report finished...')

    def get_project_descriptor(self):
        return self.__project_descriptor__

    def get_report_info(self):
        return self.__reports_info__
