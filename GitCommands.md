This describes the available aliases:

pr $pull_req_id: fetching a specific Pull Request and checking it out.

Implementation:
```
    pr  = "!f() { git fetch -fu ${2:-$(git remote |grep ^upstream || echo origin)} refs/pull/$1/head:pr/$1 && git checkout pr/$1; }; f"
```

