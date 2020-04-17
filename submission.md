# Write Less and Test More with Data Regression Testing

## Description

As data structures of a project increases in size and complexity, it becomes harder and harder to preserve test completeness. Testing objects with dozens of attributes or arrays with hundreds of values could turn into a laborious task. Often, programmers let these kind of data partially tested, especially if the required code coverage was already achieved.

In this talk we'll show how to increase test completeness for large data structures by applying data regression testing. We'll be presenting pytest-regressions, a pytest plugin that helps to test large datasets and objects by automatically serializing expected data on disk and later checking test results against it. We'll also show how pytest-regressions make it easier to inspect test data and debug failing tests. The talk shows examples of data regression being applied to numerical algorithms, web APIs, Flask views and SQLAlchemy models.

## Who and Why (Audience)

This talk aims for anyone interested in automated testing and TDD. Audience must have basic knowledge of how to write unit testing to fully comprehend the benefits of the tools and technique that would be presented. A basic understanding of how pytest fixtures work is also desirable.

After the talk, is expected that the audience would be able to use [pytest-regressions](https://pytest-regressions.rtfd.io) to create tests for multiple kinds of data structures (arrays, images and serializeble objedt) that guarantee test data completeness, and in addition, make tests easier to read and maintain. The talk will also introduce the idea for those that wish to implement their own infrastructure for data regression testing.

## Outline

1. Introduction: author bio and what we mean by “data regression testing” (2 minutes).

1. Whetting Your Appetite: shows a 10-lines unit test that checks object attributes being reduced to a one-liner assert using [pytest-regressions](https://pytest-regressions.rtfd.io) plugin. Do the same for a unit test that check the output of a simple machine learning algorithm (1 minute).

1. When “test first” doesn’t fit: propose a simple problem - “implementing a spline algorithm” - where the TDD “test first” rule doesn’t fit since the developer can’t know the exact values it must be testing against beforehand. Show how **pytest-regressions** facilitates the writing of a unit test after the developer manually make sure the spline algorithm is correct. Here we introduce `num_regression` fixture, to do data regression for numerical arrays. Examples would be running “live”, having the slides as backups (5 minutes).

1. Data Regression for Numerical Values: shows in more details the `num_regression` fixture: (i) how it’s an improvement over a naive way of testing for array values, (ii) the generated CSV output that could be visualized in a spreadsheet and (iii) tolerance settings (2 minutes).

1. Data Regression for Text Output: shows the `file_regression` fixture that do data regression for any test where the output can be written to a file. Use a function that generates a CSV as the first example, then shows how to use the fixture to test a Flask view function to compare the generated HTML. Highlights how the test failure message make it easier to debug failing testing results. (3 minutes).

1. Data Regression for Objects: shows how to test a JSON based Web API using the `data_regression` fixture. (1 minute).

1. Data Regression for SQLAlchemy models: shows how we test SQLAlchemy models using [serialchemy](github.org/ESSS/serialchemy), a library for serializing SQLAlchemy models. How we overcome the problem of ID being non-deterministic. (3 minutes).

1. Image Regression: shows how we apply image regression to the spline problem (by comparing a plotted spline with its expected results). Shows also how we can apply image regression to test for 3D rendering engines by using VTK (3 minutes).

1. Supporting for Pandas data frames, automatically regenerating all test data and [pytest-datadir](github.com/gabrielcnr/pytest-datadir) (2 minutes).

1. Conclusion (2 minutes).
