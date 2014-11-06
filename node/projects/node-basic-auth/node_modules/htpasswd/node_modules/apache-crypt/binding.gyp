{
  "targets": [
    {
      "target_name": "crypt3",
      "sources": [ "./deps/crypt3.cc" ],
      "link_settings": {
        "conditions": [
          ['OS!="mac"', {
            "libraries": ["-lcrypt"]
          }]
        ]
      },
      "include_dirs" : [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}