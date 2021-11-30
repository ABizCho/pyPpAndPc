# pyPpAndPc
pyPpAndPc, python-Paragraphing-and-PlagiarismChecker, had been planned to make a program 'paragraping scripts' and 'checking plagiarism in the scripts', at first.
However, the program's main functions was replaced with 'AI Writing'.
<br>

This project made for horiz.d's business.
<br><br>


## Main Process
This program is consist of 5 main processes
<br><br><br>


#### PROC1 : Get Input from user
Input is consist of sessionTopic and 5-sessionKeywords.
<br><br>

#### PROC2 : Write script(article) on the basis of user inputs'
Writting article automatically, based on user input, using rytr service controling window by using pyautogui.
I'm planning to replace process using pyautogui with rytrAPI, I have requested Alpha-API to rytr management team.
  *  Process library - rytr ,pyautogui
<br>

#### PROC3 : Extract related-keywords from the AI article'
I have to extract 5 related keywords from my article,not to overlap existing user keywords. To satisfy these, I adopted Yake, NLP lib, not only to created article but to user' input keywords. article-keywords will be extracted satisfying some requirements like "Selected keyword must be compounded" and "Selected keyword should satisfy over relation-criteria 0.01". After all, program will compare two keyword lists which were returned from before process and will extract 5 keywords randomly.
  * Process library - NLP( Yake ),
<br>

#### PROC4 : Frame and save in an word, docx,file
Save the results, script and related-keywords , in docx satisfying a submit-standard
  * Process library - pyautogui
<br>


