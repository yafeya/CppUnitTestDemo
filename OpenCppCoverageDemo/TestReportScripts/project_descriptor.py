import os


class ProjectDescriptor:
    __solution_dir__ = ''
    __project_name__ = ''
    __project_bin_dir__ = ''
    __source_dirs__ = []
    __test_apps__ = []
    __test_app_dirs__ = []
    __test_source_dirs__ = []

    def __init__(self):
        self.__source_dirs__ = list()
        self.__test_apps__ = list()

    def set_solution_dir(self, solution_dir):
        self.__solution_dir__ = solution_dir

    def set_project_name(self, name):
        self.__project_name__ = name

    def set_project_bin_dir(self, project_bin_dir):
        self.__project_bin_dir__ = project_bin_dir

    def append_source_dir(self, source_dir):
        if os.path.exists(source_dir):
            self.__source_dirs__.append(source_dir)

    def append_test_app(self, test_app):
        if os.path.isfile(test_app):
            self.__test_apps__.append(test_app)

    def append_test_app_dir(self, test_app_dir):
        if os.path.exists(test_app_dir):
            self.__test_app_dirs__.append(test_app_dir)

    def append_test_source_dir(self, test_source_dir):
        if os.path.exists(test_source_dir):
            self.__test_source_dirs__.append(test_source_dir)

    def get_solution_dir(self):
        return self.__solution_dir__

    def get_project_name(self):
        return self.__project_name__

    def get_project_bin_dir(self):
        return self.__project_bin_dir__

    def get_source_dirs(self):
        return self.__source_dirs__

    def get_test_apps(self):
        return self.__test_apps__

    def get_test_app_dirs(self):
        return self.__test_app_dirs__

    def get_test_source_dirs(self):
        return self.__test_source_dirs__
