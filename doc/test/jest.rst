===============
Unit Test: Jest
===============

Jest is used to perform unit testing against our reactjs frontend code. Specifically,
our `package.json`, defines a corresponding `script`, which can execute a set of unit
tests. This can easiliest be done from the `browserify` container, provided by the
rancher `development build`_:

.. code:: bash

    root@trusty64:/vagrant# docker build -f dockerfile/browserify.dockerfile -t jeff1evesque/ml-browserify:0.7 .
    root@trusty64:/vagrant# docker run --hostname browserify --name browserify -d jeff1evesque/ml-browserify:0.7
    root@trusty64:/vagrant# docker exec -it browserify /bin/bash
    root@browserify:/var/machine-learning/src/jsx# npm run test

    > reactjs@1.0.0 test /var/machine-learning/src/jsx
    > NODE_ENV=test jest --config jest.config.js

     PASS  __tests__/layout/analysis.test.jsx (11.716s)
      AnalysisLayout Component
        ✓ analysisForm should exist (19ms)
        ✓ url should render DataNewState component (113ms)
        ✓ url should render DataAppendState component (72ms)
        ✓ url should render ModelGenerateState component (25ms)
        ✓ url should render ModelPredictState component (7ms)
        ✓ url should render CurrentResultState component (16ms)
        ✓ url should render ResultsDisplayState component (11ms)

     PASS  __tests__/layout/page.test.jsx
      PageLayout Component
        ✓ should render home route (157ms)
        ✓ should render login route (18ms)
        ✓ should render logout route (18ms)
        ✓ should render register route (21ms)
        ✓ should render analysis route (88ms)

     PASS  __tests__/content/register.test.jsx
      Register Component
        ✓ registerForm should exist (4ms)
        ✓ user[login] field should exist (8ms)
        ✓ [name="user[email]"] field should exist (2ms)
        ✓ [name="user[password]"] field should exist (2ms)
        ✓ submit buttom should exist (2ms)

     PASS  __tests__/content/login.test.jsx
      Login Component
        ✓ loginForm should exist (3ms)
        ✓ user[login] field should exist (3ms)
        ✓ user[password] field should exist (2ms)
        ✓ form submit button should exist (3ms)

    --------------------------|----------|----------|----------|----------|-------------------|
    File                      |  % Stmts | % Branch |  % Funcs |  % Lines | Uncovered Line #s |
    --------------------------|----------|----------|----------|----------|-------------------|
    All files                 |    33.33 |    21.32 |    37.64 |    33.51 |                   |
     animation                |    79.17 |       55 |    64.29 |    79.17 |                   |
      animate.jsx             |    79.17 |       55 |    64.29 |    79.17 |... 34,135,136,139 |
     content                  |    26.85 |    17.44 |       50 |    26.85 |                   |
      home-page.jsx           |      100 |      100 |      100 |      100 |                   |
      login.jsx               |    27.78 |    22.58 |    55.56 |    27.78 |... 46,156,169,183 |
      register.jsx            |    23.91 |    14.55 |    33.33 |    23.91 |... 99,209,219,231 |
     formatter                |        0 |      100 |        0 |        0 |                   |
      transpose.js            |        0 |      100 |        0 |        0 |    47,48,51,52,57 |
     general                  |    35.71 |    15.38 |    27.27 |    36.59 |                   |
      ajax-caller.js          |    53.85 |       50 |       60 |    58.33 |    16,44,46,49,53 |
      breakpoints.js          |      100 |      100 |      100 |      100 |                   |
      colors.js               |      100 |      100 |      100 |      100 |                   |
      range-slider.jsx        |        0 |        0 |        0 |        0 |... 62,63,64,65,67 |
      spinner.jsx             |       50 |      100 |        0 |       50 |                14 |
      submit-button.jsx       |        0 |        0 |        0 |        0 |    23,24,25,26,28 |
     input-data               |        0 |        0 |        0 |        0 |                   |
      supply-dataset-file.jsx |        0 |        0 |        0 |        0 |... 8,90,95,96,113 |
      supply-dataset-url.jsx  |        0 |        0 |        0 |        0 |... 6,88,93,94,112 |
      supply-predictors.jsx   |        0 |        0 |        0 |        0 |... 11,118,119,121 |
     layout                   |    34.21 |    19.51 |    73.33 |    34.21 |                   |
      analysis.jsx            |    30.56 |    19.51 |    69.23 |    30.56 |... 33,234,254,281 |
      login.jsx               |      100 |      100 |      100 |      100 |                   |
      register.jsx            |      100 |      100 |      100 |      100 |                   |
     model                    |       50 |        0 |    66.67 |       50 |                   |
      model-type.jsx          |       50 |        0 |    66.67 |       50 |       27,28,29,31 |
     navigation               |     3.64 |        0 |     6.25 |     3.64 |                   |
      header-menu.jsx         |        0 |        0 |        0 |        0 |... 35,143,150,151 |
      nav-bar.jsx             |      100 |      100 |      100 |      100 |                   |
      user-menu.jsx           |        0 |        0 |        0 |        0 |... 28,229,231,248 |
     navigation/menu-items    |    23.33 |    15.09 |    33.33 |    23.33 |                   |
      current-result.jsx      |       50 |      100 |        0 |       50 |                15 |
      home.jsx                |       50 |      100 |        0 |       50 |                17 |
      login.jsx               |        0 |        0 |        0 |        0 |... 20,123,132,133 |
      register.jsx            |        0 |        0 |        0 |        0 |    25,30,40,44,45 |
      results.jsx             |    52.17 |    44.44 |    83.33 |    52.17 |... 63,64,67,68,92 |
     redux                    |      100 |      100 |      100 |      100 |                   |
      store.jsx               |      100 |      100 |      100 |      100 |                   |
     redux/action             |    23.08 |        0 |       30 |    23.08 |                   |
      current-result.jsx      |        0 |      100 |        0 |        0 |                 7 |
      login.jsx               |        0 |      100 |        0 |        0 |                 7 |
      logout.jsx              |        0 |      100 |        0 |        0 |                 9 |
      page.jsx                |       30 |        0 |    42.86 |       30 |... 26,56,57,62,63 |
     redux/container          |       70 |     38.6 |    68.18 |       70 |                   |
      analysis-layout.jsx     |    63.64 |    33.33 |      100 |    63.64 |... 38,42,43,46,47 |
      current-result.jsx      |       80 |    57.14 |      100 |       80 |             29,30 |
      data-append.jsx         |      100 |      100 |      100 |      100 |                   |
      data-new.jsx            |      100 |      100 |      100 |      100 |                   |
      header-menu.jsx         |    66.67 |      100 |        0 |    66.67 |                18 |
      home-page.jsx           |      100 |      100 |      100 |      100 |                   |
      login-link.jsx          |     37.5 |        0 |        0 |     37.5 |    19,20,22,26,35 |
      login.jsx               |     87.5 |       80 |      100 |     87.5 |                22 |
      model-generate.jsx      |      100 |      100 |      100 |      100 |                   |
      model-predict.jsx       |      100 |      100 |      100 |      100 |                   |
      range-slider.jsx        |    66.67 |      100 |        0 |    66.67 |                18 |
      register-link.jsx       |    33.33 |        0 |        0 |    33.33 |       18,19,21,25 |
      register.jsx            |     87.5 |       80 |      100 |     87.5 |                21 |
      results.jsx             |      100 |      100 |      100 |      100 |                   |
      review-results-link.jsx |    66.67 |    57.14 |      100 |    66.67 |             22,23 |
      user-menu.jsx           |     37.5 |        0 |        0 |     37.5 |    19,20,22,26,35 |
     redux/reducer            |    59.52 |     57.5 |      100 |    59.52 |                   |
      data.jsx                |     37.5 |    36.36 |      100 |     37.5 |    17,18,20,22,29 |
      layout.jsx              |     87.5 |    90.91 |      100 |     87.5 |                38 |
      login.jsx               |     62.5 |    55.56 |      100 |     62.5 |          16,23,25 |
      page.jsx                |    55.56 |    44.44 |      100 |    55.56 |... 32,41,43,69,77 |
     result                   |    31.54 |    32.32 |    43.48 |    31.54 |                   |
      current-result.jsx      |    22.11 |    34.15 |    31.25 |    22.11 |... 80,343,346,349 |
      results.jsx             |    57.14 |    23.53 |    71.43 |    57.14 |... 99,114,115,132 |
     route                    |      100 |      100 |      100 |      100 |                   |
      main-route.jsx          |      100 |      100 |      100 |      100 |                   |
      result-route.jsx        |      100 |      100 |      100 |      100 |                   |
      session-route.jsx       |      100 |      100 |      100 |      100 |                   |
     session-type             |    38.46 |    14.38 |    43.75 |    38.46 |                   |
      data-append.jsx         |    43.94 |     18.6 |    46.15 |    43.94 |... 93,196,197,243 |
      data-new.jsx            |    39.62 |     8.33 |       40 |    39.62 |... 32,136,137,153 |
      model-generate.jsx      |    30.38 |    10.64 |    35.71 |    30.38 |... 18,224,230,280 |
      model-predict.jsx       |    41.94 |    22.22 |    54.55 |    41.94 |... 49,154,165,195 |
     svg                      |        0 |        0 |        0 |        0 |                   |
      svg-books.jsx           |        0 |      100 |        0 |        0 |... 20,21,25,29,33 |
      svg-home.jsx            |        0 |        0 |        0 |        0 |... 32,36,40,44,48 |
      svg-pencil-note.jsx     |        0 |      100 |        0 |        0 |... 21,22,26,30,34 |
      svg-user.jsx            |        0 |      100 |        0 |        0 |... 20,21,25,29,33 |
     validator                |    10.71 |    21.43 |    16.67 |    10.71 |                   |
      valid-email.js          |        0 |      100 |        0 |        0 |            6,7,11 |
      valid-file.js           |        0 |        0 |        0 |        0 |       6,7,8,10,15 |
      valid-float.js          |        0 |        0 |        0 |        0 |... 16,17,19,22,27 |
      valid-password.js       |        0 |      100 |        0 |        0 |          10,11,15 |
      valid-string.js         |       75 |       75 |      100 |       75 |                 9 |
      valid-url.js            |        0 |      100 |        0 |        0 |            6,7,11 |
    --------------------------|----------|----------|----------|----------|-------------------|
    Test Suites: 4 passed, 4 total
    Tests:       21 passed, 21 total
    Snapshots:   0 total
    Time:        20.649s
    Ran all test suites.

**Note:** it is important to remember to run the above command in the same directory,
containing the `package.json`, within the `browserify` docker container.

This frontend testing can be executed manually, as indicated above. However, it is also
implemented within our travis ci. Therefore, each pull request, will verify the integrity
of the reactjs frontend code.

.. _development build: ../installation/rancher
