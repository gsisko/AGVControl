from pybuilder.core import init, use_plugin

use_plugin("python.core")
#use_plugin("python.unittest")
use_plugin('pypi:pybuilder_pytest')
#use_plugin("python.coverage") #Coverage function is currently broken with
use_plugin('pypi:pybuilder_pytest_coverage')
use_plugin("python.install_dependencies")
use_plugin("python.distutils")
use_plugin("python.flake8")


default_task = "publish"

@init
def initialize(project):
    project.get_property("pytest_extra_args").append("-x")

    project.set_property_if_unset("pytest_coverage_break_build_threshold", 50)

    project.set_property("pytest_coverage_html", True) #get html coverage report
    #project.set_property('coverage_reset_modules', True)
    #project.set_property("coverage_break_build", False) # default is True

    project.build_depends_on('pytest')
    project.build_depends_on('mockito')
    project.build_depends_on('coverage')
    project.build_depends_on('CppHeaderParser')
    project.build_depends_on('pySerial')
    project.build_depends_on('flake8')
