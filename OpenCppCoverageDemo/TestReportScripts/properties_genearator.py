import reports_info
import project_descriptor
import os


class PropertiesGenerator:

    __project_descriptor__: project_descriptor.ProjectDescriptor = None
    __reports_info__: reports_info.ReportsInfo = None
    __solution_dir__ = ''

    def __init__(self, proj_descriptor: project_descriptor.ProjectDescriptor, rept_info: reports_info.ReportsInfo):
        self.__project_descriptor__ = proj_descriptor
        self.__reports_info__ = rept_info
        solution_dir = str(self.__project_descriptor__.get_solution_dir())
        if not solution_dir.endswith('/'):
            self.__solution_dir__ = solution_dir+'/'

    def __validate_solution_dir__(self, path: str):
        if path.startswith(self.__solution_dir__):
            result = path.replace(self.__solution_dir__, '')
        else:
            result = path
        return result

    def __get_sonar_sources__(self):
        source_dirs = self.__project_descriptor__.get_source_dirs()
        sonar_sources = ''
        for idx, val in enumerate(source_dirs):
            sonar_sources += self.__validate_solution_dir__(val)
            if not idx == len(source_dirs) - 1:
                sonar_sources += ','
        return sonar_sources

    def __write_project_info__(self):
        lines = list()
        lines.append('sonar.projectKey={arg1}'.format(arg1=self.__project_descriptor__.get_project_name()))
        lines.append(os.linesep)
        lines.append('sonar.projectVersion={arg1}'.format(arg1='0.1'))
        lines.append(os.linesep)
        lines.append('sonar.projectBaseDir={arg1}'.format(arg1=self.__project_descriptor__.get_solution_dir()))
        lines.append(os.linesep)
        return lines

    def __write_code_info__(self):
        lines = list()

        sonar_sources = self.__get_sonar_sources__()
        lines.append('sonar.sources={arg1}'.format(arg1=sonar_sources))
        lines.append(os.linesep)

        test_dirs = self.__project_descriptor__.get_test_source_dirs()
        sonar_tests = ''
        for idx, val in enumerate(test_dirs):
            sonar_tests += self.__validate_solution_dir__(val)
            if not idx == len(test_dirs) - 1:
                sonar_tests += ','
        lines.append('sonar.tests={arg1}'.format(arg1=sonar_tests))
        lines.append(os.linesep)
        return lines

    def __write_server_info__(self):
        lines = list()
        lines.append('sonar.host.url=http://156.140.160.213:9000')
        lines.append(os.linesep)
        lines.append('sonar.login=833f962ae7f83fd3a2344cf00b99f8540ebf76df')
        lines.append(os.linesep)
        lines.append('sonar.language=c++')
        lines.append(os.linesep)
        return lines

    def __write_report_info__(self):
        lines = list()

        sonar_sources = self.__get_sonar_sources__()

        reports = self.__reports_info__.test_reports
        sonar_test_reports = ''
        for idx, val in enumerate(reports):
            sonar_test_reports += self.__validate_solution_dir__(val)
            if not idx == len(reports) - 1:
                sonar_test_reports += ','

        lines.append('sonar.cxx.xunit.reportPath={arg1}'.format(arg1=sonar_test_reports))
        lines.append(os.linesep)
        lines.append('sonar.cxx.includeDirectories={arg1}'.format(arg1=sonar_sources))
        lines.append(os.linesep)
        valid_cov_rpt = self.__validate_solution_dir__(self.__reports_info__.coverage_report)
        lines.append('sonar.cxx.coverage.reportPath={arg1}'.format(arg1=valid_cov_rpt))
        lines.append(os.linesep)
        valid_cpp_check_rpt = self.__validate_solution_dir__(self.__reports_info__.cpp_check_report)
        lines.append('sonar.cxx.cppcheck.reportPath={arg1}'.format(arg1=valid_cpp_check_rpt))
        return lines

    def write_properties(self):
        lines = list()
        lines += self.__write_project_info__()
        lines.append(os.linesep)

        lines += self.__write_code_info__()
        lines.append(os.linesep)

        lines += self.__write_server_info__()
        lines.append(os.linesep)

        lines += self.__write_report_info__()

        print('start to generator sonar-project file...')
        properties_file = '{arg1}.properties'.format(arg1=self.__project_descriptor__.get_project_name())
        fs = open(properties_file, 'w')
        print('the content of the sonar-project is: {arg1}'.format(arg1=os.linesep))
        for line in lines:
            print(line)
            fs.write(line)

        fs.close()
        print('generator sonar-project file finished...')
