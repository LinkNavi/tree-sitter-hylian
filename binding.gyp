{
  "targets": [
    {
      "target_name": "tree_sitter_hylian_binding",
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "src"
      ],
      "sources": [
        "bindings/node/binding.cc",
        "src/parser.c"
      ],
      "cflags_c": [
        "-std=c11",
        "-fvisibility=hidden"
      ]
    }
  ]
}
