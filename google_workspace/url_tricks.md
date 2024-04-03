# Google Workspace URL Tricks

For a Google Workspace URL in the form: 

```
https://docs.google.com/APP/d/RESOURCE_ID/
```

Where `APP` is `presentation`, `docs`, `sheets`, 

You can perform a number of functions: 

## Edit, View, Copy


Append a verb for the action: 

* `edit`: edit mode
* `copy`: copy mode (useful for templates)
* `view`: view mode

## Export Slides 

Export slides in PDF, or SVG: 

From a URL: 

```
https://docs.google.com/presentation/d/RESOURCE_ID/edit#slide=id.SLIDEHASH
```
(The first created slide may have a hash of just `p`)

Export the slide has SVG: 

```

https://docs.google.com/presentation/d/RESOURCE_ID/export/svg/?pageid=SLIDEHASH
```

Noting: 
  * `edit` changes to `export/svg` (may also work for `export/pdf`, etc)
  * the slidehash is used as the `pageid` (drop the `id.`).


_Thanks to @NimJay for the SVG trick!_
