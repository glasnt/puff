# Setting a custom pycache prefix. 

By default, Python will cache to `__pycache__/` in the current path ([docs](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPYCACHEPREFIX)). 

You can set this to be somewhere away from your current working directory, saving you from "dundercruft" (such as accidentally committing `__pycache__/` to source control. 

Depending on your system, you can set Python to cache to somewhere else, such as a temporary folder, or ram filesystem: 


```shell
export PYTHONPYCACHEPREFIX=$XDG_RUNTIME_DIR/__pycache__/ # for xdg systems
# or
export PYTHONPYCACHEPREFIX=/tmp/__pycache__/  # another example
```

_(Thanks to Clinton Roy for the tip!)_
