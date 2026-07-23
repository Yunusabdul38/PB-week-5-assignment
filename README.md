# Programming Bitcoin - Week 5

## Overview
This week, you'll learn about P2SH scripts in Bitcoin and how to implement them in Python.

## Solution Requirements

You need to complete the Python scripts and notebook to pass.

## Local Testing

### Prerequisites
 > [!TIP]
 > It is recommended to use a virtual environment, to avoid messing up your system level python installation.
 > You can also use an existing `.venv` folder from previous exercises, to avoid re-downloading all the dependencies.

- Install Python from [here](https://www.python.org/downloads/).

- Setup the virtual python environment, and install all dependencies.
  ```shell
  python3 -m venv .venv
  source .venv/bin/activate
  pip3 install -r requirements.txt
  ```
- In your IDE, set the jupyter notebook's `kernel path` to `./venv/bin/python3`. (if the path differs in your system, locate the `python3` executable in the `.venv` folder)

- Run the first cell of the notebook. If all goes well it should run without any error.


### Testing Steps
- Run all the cells in `Chapter8.ipynb`. If all the cells run without errors, you have successfully completed the challenge and are ready to submit your solution.

### Common Issues
- If you are facing issues with solving the assignment locally, you can use [Google Colab](https://colab.research.google.com) to run in browser.
- Linux and MacOS are the recommended operating systems for this challenge. If you are using Windows, you may face compatibility issues.
- If you are unable to run the test script locally, you can submit your solution and check the results on the Github.
- The autograder will run the submission on an Ubuntu 24.04 environment. Make sure your script is compatible with this environment.


## Submission

- Edit the required files.
- Commit your changes and push to the main branch:
  - Add your changes by running `git add *`.
  - Commit the changes by running `git commit -m "Solution"`.
  - Push the changes by running `git push origin main`.
- The autograder will run your submission to verify the functionality.
- Check the status of the autograder on the Github Classroom portal to see if it passed successfully or failed. Once you pass the autograder with a score of 100, you have successfully completed the challenge.
- You can submit multiple times before the deadline. The last submission before the deadline will be considered your final submission. Check deadline and other details from the [classroom dashboard](https://classroom.github.com/classrooms/166743040-programming-bitcoin).


## Evaluation Criteria
Your submission will be evaluated based on:
- **Autograder**: Your code must pass the autograder tests.
- **Explainer Comments**: Include comments explaining each step of your code.
- **Code Quality**: Your code should be well-organized, commented, and adhere to best practices.

### Plagiarism Policy
Our plagiarism detection checker thoroughly identifies any instances of copying or cheating. Participants are required to publish their solutions in the designated repository, which is private and accessible only to the individual and the administrator. Solutions should not be shared publicly or with peers. In case of plagiarism, both parties involved will be directly disqualified to maintain fairness and integrity.

### AI Usage Disclaimer
You may use AI tools like ChatGPT to gather information and explore alternative approaches, but avoid relying solely on AI for complete solutions. Verify and validate any insights obtained and maintain a balance between AI assistance and independent problem-solving.

## Why These Restrictions?
These rules are designed to enhance your understanding of the technical aspects of Bitcoin. By completing this assignment, you gain practical experience with the technology that secures and maintains the trustlessness of Bitcoin. This challenge not only tests your ability to develop functional Bitcoin applications but also encourages deep engagement with the core elements of Bitcoin technology.
