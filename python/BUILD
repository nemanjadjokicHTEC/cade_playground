load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "dummy_logger",
    srcs = ["dummy_logger.py"],
    main = "dummy_logger.py",
    deps = [
        "//python/random_print_library:random_print_library",
    ],
    visibility = ["//visibility:public"],
)