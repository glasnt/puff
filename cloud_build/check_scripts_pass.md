# Check scripts pass in Cloud Build with 'set -e'

[Cloud Build scripts](https://cloud.google.com/build/docs/configuring-builds/run-bash-scripts) let you run inline scripts to add extra complexity to builds. 

However, as with regular Bash shell scripts, if a shell script has multiple commands and one fails, it keeps running. Only if the last command returns a non-zero exit code would the entire step fail. 

Prevent this by adding `set -e` to `Exit Immediately` on errors. This will ensure you have a fast-fail mechanism on steps. 

Example: 

```
steps: 
    - name: bash
      script:  |
        #!/usr/bin/env bash -e
        ./my_script_that_could_fail
        ./my_other_script
```