name = "openexr"

version = "2.2.1"

authors = [
    "Industrial Light & Magic"
]

description = \
    """
    OpenEXR is a high dynamic-range (HDR) image file format for use in computer imaging applications.
    """

requires = [
    "gcc-6",
    "cmake-3",
    "ilmbase-2.2.1"
]

variants = [
    ["platform-linux"]
]

tools = [
    "openexr"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

#TODO: Use the SHA1 of the archive instead.
uuid = "openexr-2.2.1"

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
