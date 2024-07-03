# devops-technical-test-data

# DevOps Technical Project - Descartes Underwriting

## Introduction
Here is my repo for the DevOps technical project of Descartes Underwriting.
This README explains in a few sentences how I proceeded for this project.

**Note:** If you want to test it, you can run the python script. I deleted it to have a clean repo. Just run the command:

```bash
python -m unittest tests/test_backup.py
```

#### Step 1: Understanding the structure
First, I needed to understand what was being asked, it took me some time to really understand everything, but I was able to determine what needed to be done.
So, a python file was needed for the script, as well as tests and also a yml file for GitHub Actions.
From there, everything became faster.


#### Step 2: The script
This was the most important part for me because without it, nothing would work.
So, it had to be done first. The task was to create a backup of files from a repo.
My first instinct was to know which library to use, the ones that came to mind were 'os' and 'subprocess' to be able to execute commands and also navigate in the project.
Then it was just a matter of basic git commands with a bit of algorithm where I separated the problem into several functions (getting the repo, commits, branch manipulation, etc...) and then centralizing everything in a main function.
At first, I did it with just instructions without separating into functions, but I wanted to have cleaner code, so I decided to make functions.


#### Step 3: The tests
There wasn't much to do, in the end, it was mostly about result verification, where I used unittest for the creation of unit tests.
It was enough to check if all the files were in the right commits, where each folder corresponded to a commit.


#### Step 4: The workflow
It was something quite rudimentary in the end, the most important thing for me was to properly separate the steps. A difficulty I encountered was handling GitHub Actions since I faced several errors in my workflow due to a lack of GitHub Token. However, after that, it got sorted out quickly.

Last edit : I just reminded that I forget to ajust one file in one specific case, it was a minor change. If you want to test out the workflow with the scheduling part, it might be the best to take the last one. However if you just want to test locally in a single time, the before last one is enough
If you have any questions, feel free to ask!

Created by Paul Dam Quang Thanh
