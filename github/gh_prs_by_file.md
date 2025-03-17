# GitHub's `gh`: PRs by File

It's sometimes useful to be able to search what open PRs are editing a specific file. 

You can use GitHub [command line tool `gh`](https://cli.github.com) to do this, with the added power of `jq`: 

```
FIND_FILE="partial/search/path"

gh pr list --json number,title,files \
  --jq 'map(select(.files | any(.path | contains("${FIND_FILE}"))) | {number,title,files})'
```

Note that by default, open PRs are searched, and the limit is 30 results from `gh pr list`, and the `--jq` only operates on the original source results, and isn't a deep search. 

You can adjust the limit by setting `-L`, and the state by setting `-s`. 

[`gh pr list` man](https://cli.github.com/manual/gh_pr_list)

[Source](https://github.com/cli/cli/issues/6642)
