name = "openexr"

version = "2.4.0"

authors = [
    "Industrial Light & Magic"
]

description = \
    """
    OpenEXR is a high dynamic-range (HDR) image file format for use in computer imaging applications.
    """

requires = [
    "gcc-6+",
    "cmake-3+",
    "boost-1.61",
    "numpy-1.12.1"
]

variants = [
    ["platform-linux"]
]

tools = [
    "exrenvmap",
    "exrheader",
    "exrmakepreview",
    "exrmaketiled",
    "exrmultipart",
    "exrmultiview",
    "exrstdattr"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "openexr-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    env.PYTHONPATH.prepend("{root}/lib64/python2.7/site-packages")

    # Helper environment variables.
    env.OPENEXR_BINARY_PATH.set("{root}/bin")
    env.OPENEXR_INCLUDE_PATH.set("{root}/include")
    env.OPENEXR_LIBRARY_PATH.set("{root}/lib64")
