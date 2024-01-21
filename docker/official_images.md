# Official Docker Images

If you ever see `python`, `bash`, or something that looks like it could just be a CLI in a Dockerfile, `cloudbuild.yaml` or similar, it's a "Docker Official Image". 

More importantly, if your image doesn't have a slash (user/org separation), it's probably an official image, and you'll want to use `_` as the placeholder when looking it up on Docker Hub. 

E.g. 

* `python` -> <https://hub.docker.com/_/python>
*  `bash` -> <https://hub.docker.com/_/bash>
