# Sorting: Comparisons
### Author: Mahdi Malkawi

# Movie Sorting 

This code challenge involves sorting an array of Movie objects based on different criteria. The Movie objects have properties such as title, year, and genres. The goal is to implement sorting functions and corresponding tests to ensure their correctness.

## Task Description
In the first part of the code challenge, you need to write two sorting functions:

- sortByMostRecentYearFirst(movies: Movie[]): Movie[]: This function sorts the array of Movie objects in descending order based on the year property, so the most recent movies come first.

- sortByTitleIgnoringArticles(movies: Movie[]): Movie[]: This function sorts the array of Movie objects alphabetically by title, ignoring any leading articles like "A", "An", or "The".

In the second part of the code challenge, you will write tests for these sorting functions. The tests will ensure that the comparator functions used for sorting provide the expected results.

## Movie Object Properties
Each Movie object has the following properties:

- title: A string representing the title of the movie.
- year: A number representing the release year of the movie.
- genres: An array of strings representing the genres of the movie.