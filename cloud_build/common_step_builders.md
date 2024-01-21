# Common and Useful to remember Cloud Builders ('Steps')

I always have to look these up from previous examples, so here's a list!

* Docker: `gcr.io/cloud-builders/docker` ([Source](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/docker))
* Pack: `gcr.io/k8s-skaffold/pack` ([Source](https://github.com/GoogleContainerTools/skaffold/tree/main/deploy/buildpacks))
* `gcloud`: `gcr.io/google.com/cloudsdktool/cloud-sdk:slim` ([Source](https://github.com/GoogleCloudPlatform/cloud-sdk-docker))

Remember you can use any Docker Hub image (e.g. [python](https://hub.docker.com/_/python)), [terraform](https://hub.docker.com/r/hashicorp/terraform)) as steps. 

The above are specifically compiled with credentials that allow for authenticated actions within the step (e.g. pushing to registries). 

