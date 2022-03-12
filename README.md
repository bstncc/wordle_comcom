# wordle_comcom
Live coded wordle scraper + solver, based off of Cory Doctorow's competitive compatibility concept. There have been many wordle *solvers*, but not many wordle *interfaces*. This project will allow us to enter wordle guesses on the command line. Instead of doing this ourselves, we will write a solver to do it. We can watch the computer load the website and play by itself. Fun!

## Format
This presentation is a bit of an experiment attempting to cover the following things
- how to select scraping tools (HTTP requests / browser automation)
- how to build a basic web scraper
- how to write a good enough solver

## Goals
Web scrapers are not usually taught in school, but are intersting and powerful tools. This talk should make tools such as [playwright](https://playwright.dev/python/) and [requests](https://docs.python-requests.org) more approachable.

Additionally, there will be a focus on design, and structuring the program in an understandable way.

## From Scratch?
*Almost.* I have written a wordle solver before, but have not used this exact design. I will also be looking up playwright syntax in some boring but specific sections.

## Time?
Less than 1 hour (maybe ~45 minutes?) to leave time for discussion.

## Video?
This will be linked after it is uploaded

## Dependencies
`python3` with the `playwright` package

## Execute Solver
`python3 solve.py`
