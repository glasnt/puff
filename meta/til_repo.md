# Making your own TIL repo

Oh look, it's a meta doc about how to make a TIL repo (this repo!)

I lovingly copied mine from the illustrious [Lacey Williams-Henschel](https://github.com/williln/til), 
who in turn cribbed from the profilic [Simon Willison](https://github.com/simonw/til). 

## How it work

On pushes to the repo, the [.github/workflows/build.yml](.github/workflows/build.yml) action is invoked, which:

 * runs [build_database.py](build_database.py), building an SQLite database of files, using the git commited date for the written date, then
 * runs [update_readme.py](update_readme.py), writing a sorted list of topics and article information to the README, and commiting the updates.


## How add info

With this setup, all you have to do is create a new markdown file in a folder of your choice, and once you commit it, the index will be updated. 

I like to use the GitHub web interface to add new files (for my repo: <https://github.com/glasnt/puff/new/latest>), which allows me to quickly note down things. 

This speed of publication is a major selling point of this repo. It should (should) allow me to quickly make public notes about tips and tricks without the overhead of a full blog. 

Like some sort of small blog. A micro blog if you will. Wonder if that concept will take off. 


## I tried copying this and it didn't work!

Did you update the permissions GitHub actions have on the repo? Check your Settings > Actions permissions > General > Workflow permissions, 
making sure you have "read and write" permissions" selected. This allows the action to make automatic updates. 
