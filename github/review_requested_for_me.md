# Getting reviews requested for me

Per GitHub repo, if you open the Pull Requests tab, you can see all open pull requests. 

But TIL there's a filter option for "Reviews" in a number of facets. These options add search parameters to the pull request search. 

These are listed below, the last two being particularly interesting: filter by "Awaiting review from you", and "Awaiting review from you or your team"! 

| Filter Name | Filter Search (`is:pr is:open ...`)|
|-------------|---------------|
| No reviews   | `review:none` |
| Review required | ` review:required` |
| Approved review |  `review:approved ` |
| Changes requested |  `review:changes-requested ` |
| Reviewed by you |  `reviewed-by:@me ` |
| Not reviewed by you |  `-reviewed-by:@me ` |
| Awaiting review from you |  `user-review-requested:@me ` |
| Awaiting review from you or your team |  `review-requested:@me ` |

These also work on a global search. 

If you want see all pull requests where you have been asked for by name, use [`is:open is:pr user-review-requested:@me`](https://github.com/search?q=+is%3Aopen+is%3Apr+user-review-requested%3A%40me&type=pullrequests)!