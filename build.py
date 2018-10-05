from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage") #Coverage function is currently broken with
use_plugin("python.install_dependencies")
use_plugin("python.distutils")


default_task = "publish"

@init
def initialize(project):
    project.set_property('coverage_reset_modules', True)
    project.set_property("coverage_break_build", False) # default is True

    project.build_depends_on('mockito')
    project.build_depends_on('coverage')
    project.build_depends_on('CppHeaderParser')
