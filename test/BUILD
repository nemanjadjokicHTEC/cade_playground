load("@rules_python//python:defs.bzl", "py_test")
load("@my_pip_deps//:requirements.bzl", "requirement")

py_test(
    name = "test_dummy_logger",
    srcs = [
        "test_dummy_logger.py",
    ],
    deps = [
       "//python:dummy_logger",
    ],
    visibility = ["//visibility:public"],
)