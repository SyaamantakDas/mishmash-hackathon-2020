from nltk.tag.stanford import StanfordPOSTagger
import os
java_path = "C:\Program Files\Java\jdk1.8.0_60"
os.environ['JAVAHOME'] = java_path
import tkinter as tk
from tkinter import *
import tkinter.font
import tkinter.scrolledtext as ScrolledText
import collections
from word_forms.word_forms import get_word_forms
global a
#creating a class called MyApp
class MyApp(tk.Tk):
    #first window gets created where we can type the input text to be analyzed
    def __init__(self):
        tk.Tk.__init__(self)
        #setting the size of the tkinter box that appears
        self.geometry('600x600+0+0')
        h = tk.Label(self, text="TEXT INFORMATION ANALYSIS:",font=('Helvetica', 14, 'bold'))
        h.pack(anchor=CENTER, side=TOP, pady=20)
        #creating a label to instruct the user what to do
        w = tk.Label(self, text="Enter your text below:", font=('Helvetica', 12, ' bold italic'))
        w.pack(anchor=NW, side=TOP, pady=20)
        #creating a scrollable input text box
        self.ScrolledText = ScrolledText.ScrolledText(self)
        self.ScrolledText.pack(anchor=W, side=TOP, fill=X, expand = YES)
        #pressing the submit button calls the win2 method
        close_button = tk.Button(self, text="Submit", command=self.win2)
        close_button.pack(anchor=CENTER)
        self.string = ""
    #second text window called win2 gets created below first window and shows the required result in it    
    def win2(self):
        #obtaining the input string
        self.string = self.ScrolledText.get('1.0',END)
        #assigning the input string to a variable 'a'
        a= self.string
        #creating a scrollable text box where the result is shown
        self.ScrolledText = ScrolledText.ScrolledText(self)
        self.ScrolledText.pack(anchor=E, side=BOTTOM, fill=X, expand = YES)
        #Groups of bloom's taxonomy keywords and signal words stored as separate lists
        Description_Concept_Definition=[
                                            " above ",
                                            "Above ",
                                            " an example ",
                                            "An example ",
                                            " appears to be ", 
                                            " behind ",
                                            "Behind ",
                                            " belongs to ", 
                                            " characteristics ",
                                            "Characteristics ",
                                            " defined as ", 
                                            " for example ",
                                            "For example, ",
                                            " for instance ",
                                            "For instance, ",
                                            " identified as ", 
                                            "Imagine that ", 
                                            " including ", 
                                            " is a characteristic of ", 
                                            " is a feature of ", 
                                            " is like ", 
                                            " looks like ", 
                                            " most important ",
                                            "Most important ",
                                            " refers to ", 
                                            " such as ", 
                                            " to illustrate ",
                                            "To illustrate, "
                                        ]
        Procedure_Sequence=[
                            " after ",
                            "After ",
                            " afterward ",
                            " at last ",
                            "At last, ",
                            " at the same time ",
                            "At the same time, ",
                            " before ",
                            "Before ",
                            " during ",
                            "During ",
                            " eventually ",
                            "Eventually, ",
                            " finally ",
                            "Finally, ",
                            " first ",
                            " first of all ",
                            "First of all, ",
                            " following ",
                            "Following ",
                            "Immediately ",
                            " immediately ",
                            "In the first place, ",
                            " in the first place ",
                            " initially ",
                            "Initially, ",
                            "Last ",
                            " last ",
                            " later ",
                            "Later, ",
                            "Meanwhile, ",
                            " meanwhile ",
                            " next ",
                            "Next ",
                            " not long after ",
                            "Not long after ",
                            " now ",
                            "Now ",
                            " preceding ",
                            "Preceding ",
                            "Previously, ",
                            " previously ",
                            "Recently ",
                            " recently ",
                            "Second ",
                            " second ",
                            "Since, ",
                            " since ",
                            " soon ",
                            "Soon ",
                            " then ",
                            "Then ",
                            " third ",
                            "Third ",
                            " to begin with ",
                            "To begin with ",
                            " when ",
                            "When ",
                            "Whenever ",
                            " whenever "
                            ]
        Comparison_Contrast=[
                             " alike ",
                             " also ",
                             "Also, ",
                             " although ",
                             " as opposed to ",
                             "As opposed to ",
                             " as well as",
                             " both ",
                             "Both ",
                             " comparatively ",
                             "Comparatively ",
                             " compared with ",
                             "Compared with ",
                             " different from ",
                             "Either ",
                             " either ",
                             " or ",
                             "Or ",
                             " however ",
                             "However ",
                             " in common ",
                             " in comparison ",
                             "In comparison ",
                             " in contrast ",
                             "In Contrast ",
                             " in the same way ",
                             "In the same way ",
                             " instead of ",
                             "Instead of ",
                             "just as ",
                             " Just as ",
                             " just like ",
                             " less than ",
                             " like ",
                             "Like ",
                             " likewise ",
                             " much as ",
                             " nevertheless ",
                             "Nevertheless ",
                             " on the other hand ",
                             " opposite ",
                             " same as ",
                             " similar ",
                             " similar too ",
                             " similarly ",
                             " though ",
                             "Though ",
                             " unlike ",
                             "Unlike ",
                             " whereas ",
                             " yet ",
                             "Yet, "]
        Cause_Effect=[" accordingly ",
                      "Accordingly ",
                      " as a consequence ",
                      "As a consequence ",
                      " as a result of ",
                      "As a result of ",
                      " as illustrated by ",
                      "As illustrated by ",
                      " because ",
                      "Becasue ",
                      " because of ",
                      " consequently ",
                      "Consequently ",
                      "Due to ",
                      " due to ",
                      " effect of ",
                      " for ",
                      "For ",
                      " for this reason ",
                      "For this reason ",
                      " hence ",
                      "Hence ",
                      " if ",
                      "If ",
                      " then ",
                      "Then ",
                      " in conclusion ",
                      "In conclusion ",
                      " in order ",
                      "In order "
                      " is caused by ",
                      " leads to ",
                      " reasons why ",
                      "Reasons why ",
                      " since, ",
                      "Since, ",
                      " so that",
                      " therefore ",
                      "Therefore ",
                      " thus ",
                      "Thus, "]
        Problem_Solution_Presentation=[
                                        "Dilemma is ",
                                        "For the given question ",
                                        "One solution can be ",
                                        " problem is ",
                                        "Problem is",
                                        "Question is ",
                                        " question is ",
                                        " response ",
                                        " solution ",
                                        "Solution ",
                                        "The puzzle is ",
                                        " the puzzle is ",
                                        "The result would be ",
                                        " the result would be ",
                                        " to fix the problem ",
                                        "To fix the problem ",
                                        "To solve this ",
                                        " to solve this "] 
        Remember_Knowledge=[
                            " arrange ",
                            " define ",
                            " describe ",
                            " duplicate ",
                            " enumerate ",
                            " examine ",
                            " identify ",
                            " label ",
                            " list ",
                            " locate ",
                            " match ",
                            " memorize ",
                            " name ",
                            " observe ",
                            " omit ",
                            " order ",
                            " outline ",
                            " quote ",
                            " read ",
                            " recall ",
                            " recite ",
                            " recognize ",
                            " record ",
                            " relate ",
                            " repeat ",
                            " reproduce ",
                            " retell ",
                            " select ",
                            " state ",
                            " tabulate ",
                            " tell ",
                            " visualize ",
                            "Arrange ",
                            "Define ",
                            "Describe ",
                            "Duplicate ",
                            "Enumerate ",
                            "Examine ",
                            "Identify ",
                            "Label ",
                            "List ",
                            "Locate ",
                            "Match ",
                            "Memorize ",
                            "Name ",
                            "Observe ",
                            "Omit ",
                            "Order ",
                            "Outline ",
                            "Quote ",
                            "Read ",
                            "Recall ",
                            "Recite ",
                            "Recognize ",
                            "Record ",
                            "Relate ",
                            "Repeat ",
                            "Reproduce ",
                            "Retell ",
                            "Select ",
                            "State ",
                            "Tabulate ",
                            "Tell ",
                            "Visualize "]
        Comprehension_Understand=[
                                    " ask ",
                                    " associate ",
                                    " cite ",
                                    " classify ",
                                    " compare ",
                                    " contrast ",
                                    " convert ",
                                    " defend ",
                                    " describe ",
                                    " differentiate ",
                                    " discover ",
                                    " discuss ",
                                    " distinguish ",
                                    " estimate ",
                                    " explain ",
                                    " express ",
                                    " extend ",
                                    " generalize ",
                                    " give examples ",
                                    " group ",
                                    " identify ",
                                    " illustrate ",
                                    " indicate ",
                                    " infer ",
                                    " interpret ",
                                    " judge ",
                                    " locate ",
                                    " observe ",
                                    " order ",
                                    " paraphrase ",
                                    " predict ",
                                    " recognize ",
                                    " relate ",
                                    " report ",
                                    " represent ",
                                    " research ",
                                    " restate ",
                                    " review ",
                                    " rewrite ",
                                    " select ",
                                    " show ",
                                    " summarize ",
                                    " trace ",
                                    " transform ",
                                    " translate ",
                                    "Associate ",
                                    "Cite ",
                                    "Classify ",
                                    "Compare ",
                                    "Contrast ",
                                    "Convert ",
                                    "Defend ",
                                    "Describe ",
                                    "Differentiate ",
                                    "Discover ",
                                    "Discuss ",
                                    "Distinguish ",
                                    "Estimate ",
                                    "Explain ",
                                    "Express ",
                                    "Extend ",
                                    "Generalize ",
                                    "Give Examples ",
                                    "Group ",
                                    "Identify ",
                                    "Illustrate ",
                                    "Indicate ",
                                    "Infer ",
                                    "Interpret ",
                                    "Judge ",
                                    "Locate ",
                                    "Observe ",
                                    "Order ",
                                    "Paraphrase ",
                                    "Predict ",
                                    "Recognize ",
                                    "Relate ",
                                    "Report ",
                                    "Represent ",
                                    "Research ",
                                    "Restate ",
                                    "Review ",
                                    "Rewrite ",
                                    "Select ",
                                    "Show ",
                                    "Summarize ",
                                    "Trace ",
                                    "Transform ",
                                    "Translate "
                                    ]
        Application=[   " act ",
                                " administer ",
                                " apply ",
                                " articulate ",
                                " calculate ",
                                " change ",
                                " chart ",
                                " choose ",
                                " collect ",
                                " complete ",
                                " compute ",
                                " construct ",
                                " determine ",
                                " develop ",
                                " discover ",
                                " dramatize ",
                                " employ ",
                                " establish ",
                                " examine ",
                                " experiment ",
                                " explain ",
                                " interpret ",
                                " compute ",
                                " demonstrate ",
                                " discover ",
                                " dramatize ",
                               " employ ",
                               " illustrate ",
                               " interpret ",
                               " manipulate ",
                               " modify ",
                               " judge ",
                               " operate ",
                               " practice ",
                               " predict ",
                               " prepare ",
                               " produce ",
                               " record ",
                               " relate ",
                               " report ",
                               " schedule ",
                               " show ",
                               " simulate ",
                               " sketch ",
                               " solve ",
                               " teach ",
                               " transfer ",
                               " use ",
                               " write ",
                                "Act ", "Administer ", "Apply ", "Articulate ", "Calculate ", "Change ", "Chart ", "Choose ", "Collect ", "Complete ", "Compute ", "Construct ", "Determine ", "Develop ", "Discover ", "Dramatize ", "Employ ", "Establish ", "Examine ", "Experiment ", "Explain ", "Interpret ", 
"Compute ", "Demonstrate ", "Discover ",
"Dramatize ", "Employ ",
"Illustrate ",
"Interpret ", "Manipulate ", "Modify ", 
"Judge ", 
"Operate ",
"Practice ", 
"Predict ", 
"Prepare ", 
"Produce ", 
"Record ", 
"Relate ",
"Report ", 
"Schedule ", 
"Show ", 
"Simulate ", "Sketch ", 
"Solve ", 
"Teach ", 
"Transfer ", 
"Use ", 
"Write "
]
        Analysis=[" advertise ",
                  " analyze ",
                  " appraise ",
                  " breakdown ",
                  " calculate ",
                  " categorize ",
                  " compare ",
                  " contrast ",
                  " criticize ",
                  " diagram ",
                  " differentiate ",
                  " discriminate ",
                  " distinguish ",
                  " examine ",
                  " experiment ",
                  " identify ",
                  " illustrate ",
                  " classify ",
                  " conclude ",
                  " connect ",
                  " correlate ",
                  " deduce ",
                  " devise ",
                  " dissect ",
                  " divide ",
                  " estimate ",
                  " evaluate ",
                  " explain ",
                  " focus ",
                  " infer ",
                  " model ",
                  " outline ",
                  " point out ",
                  " question ",
                  " relate ",
                  " order ",
                  " organize ",
                  " plan ",
                  " prioritize ",
                  " select ",
                  " separate ",
                  " subdivide ",
                  " survey ",
                  " test ",
                  "Analyze ",
                  "Appraise ",
                  "Breakdown ",
                  "Calculate ",
                  "Categorize ",
                  "Compare ",
                  "Contrast ",
                  "Criticize ",
                  "Diagram ",
                  "Differentiate ",
                  "Discriminate ",
                  "Distinguish ",
                  "Examine ",
                  "Experiment ",
                  "Identify ",
                  "Illustrate ", 
"Classify ",
"Conclude ",
"Connect ",
"Correlate ",
"Deduce ",
"Devise ",
"Dissect ",
"Divide ",
"Estimate ",
"Evaluate ",
"Explain "
"Focus ",
"Infer ",
"Model ", 
"Outline ", 
"Point out ","Question ", "Relate ", 
"Order ",
"Organize ",
"Plan ",
"Prioritize ",
"Select ",
"Separate ",
"Subdivide ", "Survey ","Test ",
]
        Evaluation=[" appraise ",
                            " argue ",
                    " arrange ", " assemble ", " categorize ", " collect ", " combine ", " comply ", " compose ", " construct ", " create "," assess "," choose "," compare "," conclude "," consider "," convince "," criticize "," critique "," debate "," decide "," defend "," design ", " develop ", " devise "," discriminate "," distinguish "," editorialize "," estimate "," evaluate "," explain ", " formulate ", " generate "," find errors "," grade "," judge "," justify "," measure "," order "," persuade "," plan "," predict "," prepare ", " rearrange ", " reconstruct ", " relate ", " reorganize ", " revise "," rewrite ", " set up ", " summarize ", " synthesize ", " tell "," write "," rank "," rate "," recommend "," reframe "," score "," select "," summarize "," support "," test "," weigh ",
                    "Appraise ",
"Argue ",
 "Arrange ", "Assemble ", "Categorize ", "Collect ", "Combine ", "Comply ", "Compose ", "Construct ", "Create ", 
"Assess ",
"Choose ",
"Compare ",
"Conclude ",
"Consider ",
"Convince ",
"Criticize ",
"Critique ",
"Debate ",
"Decide ",
"Defend ",
"Design ", "Develop ", "Devise ", 
"Discriminate ",
"Distinguish ",
"Editorialize ",
"Estimate ",
"Evaluate ",
"Explain ", "Formulate ", "Generate ", 
"Find Errors ",
"Grade ",
"Judge ",
"Justify ",
"Measure ",
"Order ",
"Persuade ",
"Plan ", 
"Predict ",
"Prepare ", "Rearrange ", "Reconstruct ", "Relate ", "Reorganize ", "Revise ", 
"Rewrite ",
 "Set up ", "Summarize ", "Synthesize ",
 "Tell ", 
"Write ",
"Rank ",
"Rate ",
"Recommend ",
"Reframe ",
"Score ",
"Select ",
"Summarize ",
"Support ",
"Test ",
"Weigh "
]
        Synthesis_Create=[" adapt "," anticipate "," appraise "," argue "," assemble "," assess ",  " attach "," choose ", " compare ", " conclude ", " contrast ", " defend ", " describe ", " discriminate ", " estimate ", " evaluate ", " explain "," collaborate "," combine "," compile "," compose "," construct "," create "," design "," develop "," devise "," express "," facilitate "," formulate "," generalize "," hypothesize "," infer "," integrate "," intervene "," invent "," judge "," justify "," interpret ", " relate "," manage "," modify "," negotiate "," originate "," plan "," predict ", " prepare "," produce "," propose "," rate ", " rearrange "," reorganize "," report "," revise "," rewrite "," role-play "," select ", " summarize ", " support "," simulate "," solve "," speculate "," structure "," test "," validate "," value "," write ", "Adapt ",
"Anticipate ",
"Appraise ",
"Argue ", 
"Assemble ",
"Assess ",  "Attach ", 
"Choose ", "Compare ", "Conclude ", "Contrast ", "Defend ", "Describe ", "Discriminate ", "Estimate ", "Evaluate ", "Explain ",
"Collaborate ",
"Combine ",
"Compile ",
"Compose ",
"Construct ",
"Create ",
"Design ",
"Develop ",
"Devise ",
"Express ",
"Facilitate ",
"Formulate ",
"Generalize ",
"Hypothesize ",
"Infer ",
"Integrate ",
"Intervene ",
"Invent ",
"Judge ", 
"Justify ",
"Interpret ", "Relate ", 
"Manage ",
"Modify ",
"Negotiate ",
"Originate ",
"Plan ",
"Predict ", 
"Prepare ",
"Produce ",
"Propose ",
"Rate ", 
"Rearrange ",
"Reorganize ",
"Report ",
"Revise ",
"Rewrite ",
"Role-play ",
"Select ", "Summarize ", "Support ",
"Simulate ",
"Solve ",
"Speculate ",
"Structure ",
"Test ",
"Validate ",
"Value ",
"Write "
] 

        #initializing counter variables for each group as zero
        DCDco=0
        PSco=0
        CCco=0
        CEco=0
        PSolco=0
        Rco=0
        Uco=0
        Apco=0
        Anco=0
        Eco=0
        Crco=0
        def Punctuation(a):
            b=a
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            b=b.lower()
            for x in b:
                if x in punctuations:
                    b = b.replace(x, "") 
            return b
  
        str1=set((Punctuation(a)).split(" "))

        #counting and displaying the number of words in the text
        num_words=len((Punctuation(a)).split(" "))
        self.ScrolledText.insert(END, "Number of words : ")
        self.ScrolledText.insert(END, num_words)
        self.ScrolledText.insert(END, "\n")
        #counting and displaying the number of sentences in the text
        sentences=a.count('.')+a.count('!')+a.count('?')
        self.ScrolledText.insert(END, "Number of sentences : ")
        self.ScrolledText.insert(END, sentences)
        self.ScrolledText.insert(END, "\n")
        #Counting average number of words per sentences
        avWords=num_words/sentences
        self.ScrolledText.insert(END, "Average number of words per sentence : ")
        self.ScrolledText.insert(END, avWords)
        self.ScrolledText.insert(END, "\n")

        #English POStagger
        english_postagger = StanfordPOSTagger('C:/Users\CET\Desktop\PhD Data\stanford-postagger-2014-08-27\models\english-bidirectional-distsim.tagger', 'C:/Users\CET\Desktop\PhD Data\stanford-postagger-2014-08-27\stanford-postagger.jar')
        en=english_postagger.tag(a.split())

        k=[]
        for i in range(0,len(en)):
            if "VB" in en[i]:
                self.ScrolledText.insert(END, en[i])
                self.ScrolledText.insert(END, "\n")
                k.append(en[i])
            elif "VBD" in en[i]:
                self.ScrolledText.insert(END, en[i])
                self.ScrolledText.insert(END, "\n")
                k.append(en[i])
            elif "VBG" in en[i]:
                self.ScrolledText.insert(END, en[i])
                self.ScrolledText.insert(END, "\n")
                k.append(en[i])
            elif "VBN" in en[i]:
                self.ScrolledText.insert(END, en[i])
                self.ScrolledText.insert(END, "\n")
                k.append(en[i])
            elif "VBP" in en[i]:
                self.ScrolledText.insert(END, en[i])
                self.ScrolledText.insert(END, "\n")
                k.append(en[i])

        
        self.ScrolledText.insert(END, "\n\n")
        BT_verb_list_2=[]
        for i in range(0,len(Description_Concept_Definition)):
            if Description_Concept_Definition[i] in a:                
                DCDco=DCDco+1
        for i in range(0,len(Procedure_Sequence)):
            if Procedure_Sequence[i] in a:
                PSco=PSco+1
        for i in range(0,len(Comparison_Contrast)):
            if Comparison_Contrast[i] in a:
                CCco=CCco+1
        for i in range(0,len(Cause_Effect)):
            if Cause_Effect[i] in a:
                CEco=CEco+1
        for i in range(0,len(Problem_Solution_Presentation)):
            if Problem_Solution_Presentation[i] in a:
                PSolco=PSolco+1


        self.ScrolledText.insert(END,  "\n\nVB list 2\n\n")
        for i in range(0,len(Remember_Knowledge)):
            if Remember_Knowledge[i] in a:
                Rco=Rco+1
                
        for i in range(0,len(Remember_Knowledge)):
            for j in range(0,len(k)):
                xx=str(Remember_Knowledge[i])
                yy=str(k[j][0])
                xx=xx.lstrip()
                xx=xx.rstrip()
                yy=yy.lstrip()
                yy=yy.rstrip()
                ll=get_word_forms(xx)
                flag=False
                if yy in ll['n']:
                    flag=True
                if yy in ll['a']:
                    flag=True
                if yy in ll['r']:
                    flag=True
                if yy in ll['v']:
                    flag=True
                ll=get_word_forms(yy)
                if xx in ll['n']:
                    flag=True
                if xx in ll['a']:
                    flag=True
                if xx in ll['r']:
                    flag=True
                if xx in ll['v']:
                    flag=True
                    
                
                if flag:
                    #print(xx in yy)
                    self.ScrolledText.insert(END,  xx)
                    self.ScrolledText.insert(END,  "  Remember / Knowledge")
                    self.ScrolledText.insert(END,  "\n")
                
                
                
        for i in range(0,len(Comprehension_Understand)):
            if Comprehension_Understand[i] in a:
                Uco=Uco+1
                
        for i in range(0,len(Comprehension_Understand)):
            for j in range(0,len(k)):
                xx=str(Comprehension_Understand[i])
                yy=str(k[j][0])
                xx=xx.lstrip()
                xx=xx.rstrip()
                yy=yy.lstrip()
                yy=yy.rstrip()
                flag=False
                ll=get_word_forms(xx)
                if yy in ll['n']:
                    flag=True
                if yy in ll['a']:
                    flag=True
                if yy in ll['r']:
                    flag=True
                if yy in ll['v']:
                    flag=True
                ll=get_word_forms(yy)
                if xx in ll['n']:
                    flag=True
                if xx in ll['a']:
                    flag=True
                if xx in ll['r']:
                    flag=True
                if xx in ll['v']:
                    flag=True

                if flag:
                    #print(xx in yy)
                    self.ScrolledText.insert(END,  xx)
                    self.ScrolledText.insert(END,  "  Comprehension / Understand")
                    self.ScrolledText.insert(END,  "\n")
                
                    
        for i in range(0,len(Application)):
            if Application[i] in a:
                Apco=Apco+1
                
        for i in range(0,len(Application)):
            for j in range(0,len(k)):
                xx=str(Application[i])
                yy=str(k[j][0])
                xx=xx.lstrip()
                xx=xx.rstrip()
                yy=yy.lstrip()
                yy=yy.rstrip()
                ll=get_word_forms(xx)
                flag=False
                if yy in ll['n']:
                    flag=True
                if yy in ll['a']:
                    flag=True
                if yy in ll['r']:
                    flag=True
                if yy in ll['v']:
                    flag=True
                ll=get_word_forms(yy)
                if xx in ll['n']:
                    flag=True
                if xx in ll['a']:
                    flag=True
                if xx in ll['r']:
                    flag=True
                if xx in ll['v']:
                    flag=True    
                
                if flag:
                    #print(xx in yy)
                    self.ScrolledText.insert(END,  xx)
                    self.ScrolledText.insert(END,  "  Application")
                    self.ScrolledText.insert(END,  "\n")
                
                
        for i in range(0,len(Analysis)):
            if Analysis[i] in a:
                Anco=Anco+1
                
        for i in range(0,len(Analysis)):
            for j in range(0,len(k)):
                xx=str(Analysis[i])
                yy=str(k[j][0])
                xx=xx.lstrip()
                xx=xx.rstrip()
                yy=yy.lstrip()
                yy=yy.rstrip()
                ll=get_word_forms(xx)
                flag=False
                if yy in ll['n']:
                    flag=True
                if yy in ll['a']:
                    flag=True
                if yy in ll['r']:
                    flag=True
                if yy in ll['v']:
                    flag=True
                ll=get_word_forms(yy)
                if xx in ll['n']:
                    flag=True
                if xx in ll['a']:
                    flag=True
                if xx in ll['r']:
                    flag=True
                if xx in ll['v']:
                    flag=True   
                
                if flag:
                    #print(xx in yy)
                    self.ScrolledText.insert(END,  xx)
                    self.ScrolledText.insert(END,  "  Analysis")
                    self.ScrolledText.insert(END,  "\n")
               
                    
        for i in range(0,len(Evaluation)):
            if Evaluation[i] in a:
                Eco=Eco+1
                
        for i in range(0,len(Evaluation)):
            for j in range(0,len(k)):
                xx=str(Evaluation[i])
                yy=str(k[j][0])
                xx=xx.lstrip()
                xx=xx.rstrip()
                yy=yy.lstrip()
                yy=yy.rstrip()
                ll=get_word_forms(xx)
                flag=False
                if yy in ll['n']:
                    flag=True
                if yy in ll['a']:
                    flag=True
                if yy in ll['r']:
                    flag=True
                if yy in ll['v']:
                    flag=True
                ll=get_word_forms(yy)
                if xx in ll['n']:
                    flag=True
                if xx in ll['a']:
                    flag=True
                if xx in ll['r']:
                    flag=True
                if xx in ll['v']:
                    flag=True    
                
                if flag:
                    #print(xx in yy)
                    self.ScrolledText.insert(END,  xx)
                    self.ScrolledText.insert(END,  "  Evaluation")
                    self.ScrolledText.insert(END,  "\n")
               

                
        for i in range(0,len(Synthesis_Create)):
            if Synthesis_Create[i] in a:
                Crco=Crco+1
                
        for i in range(0,len(Synthesis_Create)):
            for j in range(0,len(k)):
                xx=str(Synthesis_Create[i])
                yy=str(k[j][0])
                xx=xx.lstrip()
                xx=xx.rstrip()
                yy=yy.lstrip()
                yy=yy.rstrip()
                ll=get_word_forms(xx)
                flag=False
                if yy in ll['n']:
                    flag=True
                if yy in ll['a']:
                    flag=True
                if yy in ll['r']:
                    flag=True
                if yy in ll['v']:
                    flag=True
                ll=get_word_forms(yy)
                if xx in ll['n']:
                    flag=True
                if xx in ll['a']:
                    flag=True
                if xx in ll['r']:
                    flag=True
                if xx in ll['v']:
                    flag=True    
                
                if flag:
                    #print(xx in yy)
                    self.ScrolledText.insert(END,  xx)
                    self.ScrolledText.insert(END,  "  Synthesis / create")
                    self.ScrolledText.insert(END,  "\n")
                
       
        
        
        
        #finding the total number of bloom's taxonomy keywords present        
        blsum=Rco+Uco+Apco+Anco+Eco+Crco
        #if the total number of bloom's taxonomy keywords is greater than zero the further operations on bloom's taxonomy keywords are carried out 
        if blsum>0:
            #calculating the percentage of each group present in the input string
            Rcop=Rco/blsum*100
            Ucop=Uco/blsum*100
            Apcop=Apco/blsum*100
            Ancop=Anco/blsum*100
            Ecop=Eco/blsum*100
            Crcop=Crco/blsum*100
            #printing the output in a tabular form
            data = [["Bloom's Taxonomy Keywords", "Count", "Percentage(%)"],['Remember Knowledge', Rco, Rcop],['Comprehension Understand', Uco, Ucop],['Application', Apco, Apcop],['Analysis', Anco, Ancop],['Evaluation', Eco, Ecop],['Synthesis Create', Crco, Crcop]]
            dash = '-' * 65

            for i in range(len(data)):
                if i == 0:
                    self.ScrolledText.insert(END, dash)
                    self.ScrolledText.insert(END, '\n')
                    self.ScrolledText.insert(END, '{:<35s}{:<15s}{:<12s}'.format(data[i][0],data[i][1],data[i][2]))
                    self.ScrolledText.insert(END, '\n')
                    self.ScrolledText.insert(END, dash)
                    self.ScrolledText.insert(END, '\n')
                else:
                    self.ScrolledText.insert(END, '{:<35s}{:<15d}{:<12f}'.format(data[i][0],data[i][1],data[i][2]))
                    self.ScrolledText.insert(END, '\n')
        #total number of signal words is calculated
        sigsum=DCDco+PSco+CCco+CEco+PSolco 
        #if the total number of signal words is greater than zero then further operations on signal words are carried out
        if sigsum>0:
            #calculating the percentage of each group present in the input string
            DCDp=DCDco/sigsum*100
            PSp=PSco/sigsum*100            
            CCp=CCco/sigsum*100
            CEp=CEco/sigsum*100
            PSolp=PSolco/sigsum*100
            #printing the output in a tabular form
            data2 = [["Signal words", "Count", "Percentage(%)"],['Description Concept Definition', DCDco, DCDp],['Procedure of Sequence', PSco, PSp],['Comparison Contrast', CCco, CCp],['Cause Effect Explanation', CEco, CEp],['Problem solution presentation', PSolco, PSolp]]
            dash = '-' * 65

            for j in range(len(data2)):
                if j == 0:
                    self.ScrolledText.insert(END, dash)
                    self.ScrolledText.insert(END, '\n')
                    self.ScrolledText.insert(END, '{:<35s}{:<15s}{:<12s}'.format(data2[j][0],data2[j][1],data2[j][2]))
                    self.ScrolledText.insert(END, '\n')
                    self.ScrolledText.insert(END, dash)
                    self.ScrolledText.insert(END, '\n')
                else:
                    self.ScrolledText.insert(END, '{:<35s}{:<15d}{:<12f}'.format(data2[j][0],data2[j][1],data2[j][2]))
                    self.ScrolledText.insert(END, '\n')
        #counting the number of words from each group present in the input string
        para=a.split("\n")
        for p in range(0, len(para)):
            f=0        
            dict={}  
            for i in range(0,len(Description_Concept_Definition)):
              if Description_Concept_Definition[i] in para[p]:
                f=1  
                index = 0
                while index < len(a):
                    index = para[p].find(Description_Concept_Definition[i], index)
                    if index == -1:
                        break
                    s1="--->" + Description_Concept_Definition[i]+ "(Description_Concept_Definition)"
                    dict[index]=s1
                    index += 2
            for i in range(0,len(Procedure_Sequence)):
              if Procedure_Sequence[i] in para[p]:
                f=1
                index = 0
                while index < len(a):
                    index = para[p].find(Procedure_Sequence[i], index)
                    if index == -1:
                        break
                    s2="--->" + Procedure_Sequence[i]+ "(Procedure_Sequence)"
                    dict[index]=s2
                               
                    index += 2

            for i in range(0,len(Comparison_Contrast)):
              if Comparison_Contrast[i] in para[p]:
                f=1
                index = 0
                while index < len(a):
                    index = para[p].find(Comparison_Contrast[i], index)
                    if index == -1:
                        break
                    s3="--->" + Comparison_Contrast[i]+ "(Comparison_Contrast)"
                    dict[index]=s3
                 
                    index += 2
            for i in range(0,len(Cause_Effect)):
              if Cause_Effect[i] in para[p]:
                f=1
                index = 0
                while index < len(a):
                    index = para[p].find(Cause_Effect[i], index)
                    if index == -1:
                        break
                    s4="--->" + Cause_Effect[i]+ "(Cause_Effect)"
                    dict[index]=s4
                    
                    index += 2
                    
            for i in range(0,len(Problem_Solution_Presentation)):
              if Problem_Solution_Presentation[i] in para[p]:
                f=1
                index = 0
                while index < len(a):
                    index = para[p].find(Problem_Solution_Presentation[i], index)
                    if index == -1:
                        break
                    s5="--->" + Problem_Solution_Presentation[i]+ "(Problem_Solution_Presentation)"
                    dict[index]=s5
                    
                    index += 2
            for i in range(0,len(Remember_Knowledge)):
              if Remember_Knowledge[i] in para[p]:
                f=1
                index = 0
                while index < len(a):
                    index = para[p].find(Remember_Knowledge[i], index)
                    if index == -1:
                        break
                    s6="--->" + Remember_Knowledge[i]+ "(Remember_Knowledge)"
                    dict[index]=s6
                    
                    index += 2                

            for i in range(0,len(Comprehension_Understand)):
              if Comprehension_Understand[i] in para[p]:
                f=1   
                index = 0
                while index < len(a):
                    index = para[p].find(Comprehension_Understand[i], index)
                    if index == -1:
                        break
                    s7="--->" + Comprehension_Understand[i]+ "(Comprehension_Understand)"
                    dict[index]=s7
                    
                    index += 2
            for i in range(0,len(Application)):
              if Application[i] in para[p]:
                f=1 
                index = 0
                while index < len(a):
                    index = para[p].find(Application[i], index)
                    if index == -1:
                        break
                    s8="--->" + Application[i]+ "(Application)"
                    dict[index]=s8
                    
                    index += 2
            for i in range(0,len(Analysis)):
              if Analysis[i] in para[p]:
                f=1
                index = 0
                while index < len(a):
                    index = para[p].find(Analysis[i], index)
                    if index == -1:
                        break
                    s9="--->" + Analysis[i]+ "(Analysis)"
                    dict[index]=s9
                    
                    index += 2
            for i in range(0,len(Evaluation)):
              if Evaluation[i] in para[p]:
                f=1  
                index = 0
                while index < len(a):
                    index = para[p].find(Evaluation[i], index)
                    if index == -1:
                        break
                    s10="--->" + Evaluation[i]+ "(Evaluation)"
                    dict[index]=s10
                    
                    index += 2
            for i in range(0,len(Synthesis_Create)):
              if Synthesis_Create[i] in para[p]:
                f=1  
                index = 0
                while index < len(a):
                    index = para[p].find(Synthesis_Create[i], index)
                    if index == -1:
                        break
                    s11="--->" + Synthesis_Create[i]+ "(Synthesis_Create)"
                    dict[index]=s11
                                        
                    index += 2
            if(f==1):
                    self.ScrolledText.insert(END, 'para ')
                    self.ScrolledText.insert(END, p)
                    self.ScrolledText.insert(END, '\n')
                    self.ScrolledText.insert(END, '\n')                    
            dict = collections.OrderedDict(sorted(dict.items()))
            for key in sorted(dict):
              self.ScrolledText.insert(END, dict[key])          
              self.ScrolledText.insert(END, '\n')
        #sentence wise      
        sentence=a.split(".")
        for p in range(0, len(sentence)):
            f=0        
            dict={}  
            for i in range(0,len(Description_Concept_Definition)):
              if Description_Concept_Definition[i] in sentence[p]:
                f=1  
                index = 0
                while index < len(a):
                    index = sentence[p].find(Description_Concept_Definition[i], index)
                    if index == -1:
                        break
                    s1="--->" + Description_Concept_Definition[i]+ "(Description_Concept_Definition)"
                    dict[index]=s1
                    index += 2
            for i in range(0,len(Procedure_Sequence)):
              if Procedure_Sequence[i] in sentence[p]:
                f=1
                index = 0
                while index < len(a):
                    index = sentence[p].find(Procedure_Sequence[i], index)
                    if index == -1:
                        break
                    s2="--->" + Procedure_Sequence[i]+ "(Procedure_Sequence)"
                    dict[index]=s2
                               
                    index += 2

            for i in range(0,len(Comparison_Contrast)):
              if Comparison_Contrast[i] in sentence[p]:
                f=1
                index = 0
                while index < len(a):
                    index = sentence[p].find(Comparison_Contrast[i], index)
                    if index == -1:
                        break
                    s3="--->" + Comparison_Contrast[i]+ "(Comparison_Contrast)"
                    dict[index]=s3
                 
                    index += 2
            for i in range(0,len(Cause_Effect)):
              if Cause_Effect[i] in sentence[p]:
                f=1
                index = 0
                while index < len(a):
                    index = sentence[p].find(Cause_Effect[i], index)
                    if index == -1:
                        break
                    s4="--->" + Cause_Effect[i]+ "(Cause_Effect)"
                    dict[index]=s4
                    
                    index += 2
                    
            for i in range(0,len(Problem_Solution_Presentation)):
              if Problem_Solution_Presentation[i] in sentence[p]:
                f=1
                index = 0
                while index < len(a):
                    index = sentence[p].find(Problem_Solution_Presentation[i], index)
                    if index == -1:
                        break
                    s5="--->" + Problem_Solution_Presentation[i]+ "(Problem_Solution_Presentation)"
                    dict[index]=s5
                    
                    index += 2
            for i in range(0,len(Remember_Knowledge)):
              if Remember_Knowledge[i] in sentence[p]:
                f=1
                index = 0
                while index < len(a):
                    index = sentence[p].find(Remember_Knowledge[i], index)
                    if index == -1:
                        break
                    s6="--->" + Remember_Knowledge[i]+ "(Remember_Knowledge)"
                    dict[index]=s6
                    
                    index += 2                

            for i in range(0,len(Comprehension_Understand)):
              if Comprehension_Understand[i] in sentence[p]:
                f=1   
                index = 0
                while index < len(a):
                    index = sentence[p].find(Comprehension_Understand[i], index)
                    if index == -1:
                        break
                    s7="--->" + Comprehension_Understand[i]+ "(Comprehension_Understand)"
                    dict[index]=s7
                    
                    index += 2
            for i in range(0,len(Application)):
              if Application[i] in sentence[p]:
                f=1 
                index = 0
                while index < len(a):
                    index = sentence[p].find(Application[i], index)
                    if index == -1:
                        break
                    s8="--->" + Application[i]+ "(Application)"
                    dict[index]=s8
                    
                    index += 2
            for i in range(0,len(Analysis)):
              if Analysis[i] in sentence[p]:
                f=1
                index = 0
                while index < len(a):
                    index = sentence[p].find(Analysis[i], index)
                    if index == -1:
                        break
                    s9="--->" + Analysis[i]+ "(Analysis)"
                    dict[index]=s9
                    
                    index += 2
            for i in range(0,len(Evaluation)):
              if Evaluation[i] in sentence[p]:
                f=1  
                index = 0
                while index < len(a):
                    index = sentence[p].find(Evaluation[i], index)
                    if index == -1:
                        break
                    s10="--->" + Evaluation[i]+ "(Evaluation)"
                    dict[index]=s10
                    
                    index += 2
            for i in range(0,len(Synthesis_Create)):
              if Synthesis_Create[i] in sentence[p]:
                f=1  
                index = 0
                while index < len(a):
                    index = sentence[p].find(Synthesis_Create[i], index)
                    if index == -1:
                        break
                    s11="--->" + Synthesis_Create[i]+ "(Synthesis_Create)"
                    dict[index]=s11
                                        
                    index += 2
            if(f==1):
                    self.ScrolledText.insert(END, 'sentence ')
                    self.ScrolledText.insert(END, p)
                    self.ScrolledText.insert(END, '\n')
                    self.ScrolledText.insert(END, '\n')                    
            dict = collections.OrderedDict(sorted(dict.items()))
            for key in sorted(dict):
              self.ScrolledText.insert(END, dict[key])          
              self.ScrolledText.insert(END, '\n')            
            

    #defining the mainloop method
    def mainloop(self):
        tk.Tk.mainloop(self)
        return self.string
#calling the class called MyApp
MyApp()
#calling mainloop 
mainloop()

#english_postagger = StanfordPOSTagger('C:/Users\CET\Desktop\PhD Data\stanford-postagger-2014-08-27\models\english-bidirectional-distsim.tagger', 'C:/Users\CET\Desktop\PhD Data\stanford-postagger-2014-08-27\stanford-postagger.jar')
#en=english_postagger.tag(a.split())
