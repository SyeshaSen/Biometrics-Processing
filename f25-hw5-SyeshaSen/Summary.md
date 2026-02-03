# SUMMARY TEMPLATE

Answer all the questions. Please put your answers _after_ the italicized instructions.

## Parameter Selection Rationale  
_Explain how you decided on your default values for the maximum number of tries and the error threshold. Why did you choose these particular thresholds? How do they balance security, usability, and fairness?_  

- The default number for the maximum number of tries is set to 3. This is fair because it ensures that someone who actually is the correct user, can enter their fingerprint up to three times, which I feel can accomodate for any mishaps in external factors like positioning of the finger, or a dirty surface to enter the password. In case someone is not the valid user, 3 guesses should not give them enough to be able to change their fingerprint or mess with any settings.

## Stakeholder-value Matrix
_Please put a stakeholder-value matrix for fingerprint-based login systems. Include at least five stakeholders and at least three values, one of which should be Privacy._

                            Privacy                         Safety                             Fairness

User                Does not want fingerprint       Can have many accounts/personal         Want to be treated equally
                    data to be shared               data compromised if misused             no matter socioeconomic status


App developer       Wants to keep fingerprint       Might compromse user data/safety        May treat certain users as more 
                    data to themselves              if benefitial to the app profits        important based on profits/benefits


Company             Wants to keep fingerprint       Might compromse user data/safety        May treat certain users as more 
                    data to themselves              if benefitial to the app profits        important based on profits/benefits


Disabled people     Might be unable to use the      May feel uncomfortable/unsafe           May not think it is fair for the
                    fingerprint software            with no option to avoid using           software to use fingerprints when they
                                                    fingerprint                             are unable to


IT help desk
---

## Citations

### Who did you work with and how?  
_Discussing the assignment with people not on your team is fine as long as you don't share code._  
_Please include any people or other sources who helped you, and any students whom you helped._  
_For each source, make sure to include how they helped you (or how you helped them)._  

* _“I discussed the authentication loop design with classmate Alice Smith and clarified how to break out of the while loop.”_  
* _“I showed Bob Lee my test plan for mocking input and he suggested using `side_effect` in `unittest.mock.patch`.”_  
* _If you did not talk to anybody about the assignment, please state that._

I did not talk to anybody regarding this assignment.
---

### What resources did you use?  
_Please give specific URLs (not “Stack Overflow” or “Google”) and state which ones were particularly helpful._  

* _https://docs.python.org/3/library/unittest.mock.html – for guidance on `patch` and `side_effect`._  
* _If you did not consult any external resources, please state that._

---

https://www.geeksforgeeks.org/python/readline-in-python/ 
- Helped with understanding readline which helped me read a sinle line of from a file and use that in my code

https://www.geeksforgeeks.org/python/python-isinstance-method/
- Helped me restablish what isinstance of means, and how it can be used to check whether an object is an instance of the given class.

## Logistics

### Did you successfully implement everything that was requested?  
_Answer “Yes”, or state here which parts did not work or which tests did not pass._  
Tests passed: 0 / 1

❌ test_login.TestLoginExactMatch-20251030045507.test_exact_match
Traceback (most recent call last):
  File "/home/runner/_work/f25-hw5-SyeshaSen/f25-hw5-SyeshaSen/pawtograder-grading/tests/test_login.py", line 15, in test_exact_match
    result = login_system.authenticate(test_fp, match_threshold=0.9)
  File "/home/runner/_work/f25-hw5-SyeshaSen/f25-hw5-SyeshaSen/pawtograder-grading/src/login.py", line 31, in authenticate
    if fp == self.original:
  File "/home/runner/_work/f25-hw5-SyeshaSen/f25-hw5-SyeshaSen/pawtograder-grading/src/fingerprint.py", line 89, in __eq__
    if self._data[row][col] == other._data[row][col]:
IndexError: list index out of range

Tests passed: 0 / 1

❌ test_login.TestLoginSuccessfulAuthentication-20251030045507.test_successful_authentication
Traceback (most recent call last):
  File "/home/runner/_work/f25-hw5-SyeshaSen/f25-hw5-SyeshaSen/pawtograder-grading/tests/test_login.py", line 24, in test_successful_authentication
    result = login_system.authenticate(test_fp, match_threshold=0.9)
  File "/home/runner/_work/f25-hw5-SyeshaSen/f25-hw5-SyeshaSen/pawtograder-grading/src/login.py", line 31, in authenticate
    if fp == self.original:
  File "/home/runner/_work/f25-hw5-SyeshaSen/f25-hw5-SyeshaSen/pawtograder-grading/src/fingerprint.py", line 89, in __eq__
    if self._data[row][col] == other._data[row][col]:
IndexError: list index out of range

Tests passed: 0 / 1

❌ test_login.TestLoginResetAfterSuccess-20251030045507.test_reset_after_success
Traceback (most recent call last):
  File "/home/runner/_work/f25-hw5-SyeshaSen/f25-hw5-SyeshaSen/pawtograder-grading/tests/test_login.py", line 91, in test_reset_after_success
    result = login_system.authenticate(successful_fp, match_threshold=0.9)
  File "/home/runner/_work/f25-hw5-SyeshaSen/f25-hw5-SyeshaSen/pawtograder-grading/src/login.py", line 31, in authenticate
    if fp == self.original:
  File "/home/runner/_work/f25-hw5-SyeshaSen/f25-hw5-SyeshaSen/pawtograder-grading/src/fingerprint.py", line 89, in __eq__
    if self._data[row][col] == other._data[row][col]:
IndexError: list index out of range


### How long did the assignment take?  
_Rather than giving a range, if you are unsure, give the average of the range._  

4.5 Hours

---

## Reflections  
_Give **one or more paragraphs** reflecting on your experience with the assignment, including answers to all of these questions:_  
* What was the most difficult part of the assignment?  
* What was the most rewarding part of the assignment?  
* What did you learn doing the assignment?  
* Constructive and actionable suggestions for improving assignments, office hours, and lecture are always welcome.  

I think that the most difficult part of the assignment was understanding how to go through the data given in the files. Especially when we trying to make variables through reading particular lines in the files. But I was able to understand this in more detail when I understood the readline() function. The most rewarding part of the assignment was that it was so advanced, and I would not have thoougt that I would be making such complicated code in first semester of college. However, I thought it was really awesome that I was able to code this, because I realized all that I have learnt. While I was doing this assignment, the most significant thing I learnt about was the readline() function, and I think it is really useful in projects like this, where certain lines from the file are important. I think that it would be helpful if we had more coding practice problems in the class lectures itself, so that we can immediately apply what we just learnt. This would condition our learning and keep us refreshed for the homework.


---
