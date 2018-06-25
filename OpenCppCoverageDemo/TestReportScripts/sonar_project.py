import reports_generator
import properties_genearator


def generate_reports():
    reporter = reports_generator.ReportsGenerator()
    reporter.generate_reports()
    proj_descriptor = reporter.get_project_descriptor()
    rpt_info = reporter.get_report_info()

    sonar_prj_generator = properties_genearator.PropertiesGenerator(proj_descriptor, rpt_info)
    sonar_prj_generator.write_properties()


if __name__ == "__main__":
    generate_reports()

