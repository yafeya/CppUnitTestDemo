import os
import xml.etree.ElementTree as XmlTree
import glob
import project_descriptor as project__descriptor


class ProjectLoader:
    __project_config_file__ = ''

    def __init__(self, project_file='project.config.xml'):
        self.__project_config_file__ = project_file

    def get_project_descriptor(self):
        project_descriptor = project__descriptor.ProjectDescriptor()
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

        solution_dir_node = project_tree.find('.//solution_dir')
        if not solution_dir_node:
            solution_dir = solution_dir_node.text
            project_descriptor.set_solution_dir(solution_dir)

        test_source_dir_nodes = project_tree.findall('.//test_source_dir')
        for test_source_dir_node in test_source_dir_nodes:
            test_source_dir = test_source_dir_node.text
            if os.path.exists(test_source_dir):
                project_descriptor.append_test_source_dir(test_source_dir)

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
