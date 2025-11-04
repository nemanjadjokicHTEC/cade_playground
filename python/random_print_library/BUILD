load("@rules_python//python:defs.bzl", "py_library")
load("@my_pip_deps//:requirements.bzl", "requirement")

py_library(
    name = "random_print_library",
    srcs = ["random_print_library.py"],
    deps = [
        requirement("wonderwords"),
    ],
    visibility = ["//visibility:public"],
)