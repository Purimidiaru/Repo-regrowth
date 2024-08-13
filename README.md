# Repo Regrowth

## Introduction
Here is my a tool I've developped to make backup of a repo

This README explains in a few sentences how I proceeded for this project.

**Note:** If you want to test it, you can run the python script with Docker. I implemented it to get a clean environnement:

```bash
docker build -t backup-script .
docker run --rm -v $(pwd)/data:/usr/src/app/data backup-script
```

The project is active by backing up a my portfolio website repo, you are up to change it along with the environment variable

#### Step 1: Understanding the structure
First, I needed to understand what was being asked, it took me some time to really understand everything, but I was able to determine what needed to be done.

So, a python file was needed for the script, as well as tests and also a yml file for GitHub Actions.
From there, everything became faster.


#### Step 2: The script
This was the most important part for me because without it, nothing would work.

So, it had to be done first. The task was to create a backup of files from a repo.

My first instinct was to know which library to use, the ones that came to mind were **'os'** and **'subprocess'** to be able to execute commands and also navigate in the project.

Then it was just a matter of basic git commands with a bit of algorithm where I separated the problem into several functions (**getting the repo, commits, branch manipulation, etc...**) and then centralizing everything in a main function.

At first, I did it with just instructions without separating into functions, but I wanted to have cleaner code, so I decided to make functions.

One of the hardest thing to support was the special characters because it wasn't support by the script. So I had the sanitize the path names and then convert the special characters from their octal form to utf-8.

#### Step 3: The tests
There wasn't much to do, in the end, it was mostly about result verification, where I used unittest for the creation of unit tests.

It was enough to check if all the files were in the right commits, where each folder corresponded to a commit.

I also sanitize the path names and handle the special chararacters

#### Step 4: The workflow
It was something quite rudimentary in the end, the most important thing for me was to properly separate the steps. A difficulty I encountered was handling GitHub Actions since I faced several errors in my workflow due to a lack of GitHub Token. However, after that, it got sorted out quickly.

For the last commit, I just implemented Docker in the workflow which seems to be the best practices in my opinion.

The workflow runs directly the test script which execute the main script. That means there is always unit tests to check if there is no problem at all with the backup

#### Additional Step: Docker

I suddenly reminded during a waking-up that it was the best to create a virtual environnement through Docker.

There is only a simple Dockerfile yet really important to get the right resultats because I noticed that I get difference results depending of the OS used to test the project.


If you have any questions, feel free to ask!

Created by Paul Dam Quang Thanh
