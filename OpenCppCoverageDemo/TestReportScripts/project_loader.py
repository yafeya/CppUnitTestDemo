import os
import xml.etree.ElementTree as XmlTree
import glob


class ProjectDescriptor:
    __project_name__ = ''
    __project_bin_dir__ = ''
    __source_dirs__ = []
    __test_apps__ = []
    __test_app_dirs__ = []

    def __init__(self):
        self.__source_dirs__ = list()
        self.__test_apps__ = list()

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


class ProjectLoader:
    __project_config_file__ = ''

    def __init__(self, project_file='project.config.xml'):
        self.__project_config_file__ = project_file

    def get_project_descriptor(self):
        project_descriptor = ProjectDescriptor()
        project_tree = XmlTree.parse(self.__project_config_file__)
        project_node = project_tree.getroot()
        project_name = project_node.get('name')
        project_descriptor.set_project_name(project_name)

        source_dir_nodes = project_tree.findall('.//source_dir')
        for source_dir_node in source_dir_nodes:
            source_dir = source_dir_node.text
            if os.path.exists(source_dir):
                project_descriptor.append_source_dir(source_dir)

        output_dir = ''
        output_dir_node = project_tree.find('.//output_dir')
        if not output_dir_node:
            output_dir = output_dir_node.text
            project_descriptor.set_project_bin_dir(output_dir)

        test_app_nodes = project_tree.findall('.//test_app')
        for test_app_node in test_app_nodes:
            test_app = test_app_node.text
            if test_app:
                test_app_pattern = output_dir + '/**/' + test_app
                search_result = glob.glob(test_app_pattern, recursive=True)
                if len(search_result) > 0:
                    for found in search_result:
                        if os.path.isfile(found):
                            project_descriptor.append_test_app(found)
                            test_app_dir = os.path.dirname(found)
                            project_descriptor.append_test_app_dir(test_app_dir)

        return project_descriptor
