#!/home/system/anaconda3/envs/py27/bin/python

from Tkinter import *
from monkeylearn import MonkeyLearn
import tkMessageBox

def classifyType ( ):
	m1 = MonkeyLearn ( '44a9385df8e93c0d9166a64e40b0c2cec66fabb4' )
	data = [ t1.get ( 1.0, "end-1c" ) ] 
        model_id = 'cl_UZRztbwF'
	response = m1.classifiers.classify ( model_id, data )
	message = str(response.body [ 0 ] )
	classifications = message [ message.find ( "classifications" ) + 19 : message.find ( "external_id" ) - 5 ]
	cl_list = classifications.split ( ", {" )
	t2.delete ( 1.0, "end-1c" )
	t2.insert ( END, "-----------------------------------------------------------------------------------------------------------------\n" )
	t2.insert ( END, '{:50s}\t{:10s}\t{:20s}\t{:15s}\n'.format("Keywords", "Confidence", " ", " tag_id" ) )
	t2.insert ( END, "-----------------------------------------------------------------------------------------------------------------\n" )
	i=4
	for item in cl_list:
		item = str ( item ) 		
		t_name = item [ item.find ( "tag_name" ) + 13 : item.find ( "confidence") - 5]
		t_conf = item [ item.find ( "confidence" ) + 13 : item.find ( "tag_id") - 4]
		t_id = item [ item.find ( "tag_id" ) + 8 : -1]
		t2.insert (END, '{:50s}\t{:10s}\t{:20s}\t{:15s}\n'.format(t_name, t_conf, " ", t_id ) )
	t2.insert ( END, "-----------------------------------------------------------------------------------------------------------------\n" )
def classifyLevel ( ):
	m1 = MonkeyLearn ( 'bc3474990f89e42c746c312da944cc2e90771c04' )
	data = [ t1.get ( 1.0, "end-1c" ) ] 
        model_id = 'cl_tShCWU7U'
	response = m1.classifiers.classify ( model_id, data )
	message = str(response.body [ 0 ] )
	t2.delete ( 1.0, "end-1c" )
	classifications = message [ message.find ( "classifications" ) + 19 : message.find ( "external_id" ) - 5 ]
	#tkMessageBox.showinfo( "TextAnalyzer", message )
	cl_list = classifications.split ( ", {" )
	t2.delete ( 1.0, "end-1c" )
	t2.insert ( END, "-----------------------------------------------------------------------------------------------------------------\n" )
	t2.insert ( END, '{:50s}\t{:10s}\t{:20s}\t{:15s}\n'.format("Bloom's Taxonomy Keywords", "Confidence", " ", " tag_id" ) )
	t2.insert ( END, "-----------------------------------------------------------------------------------------------------------------\n" )
	i=4
	for item in cl_list:
		item = str ( item ) 		
		t_name = item [ item.find ( "tag_name" ) + 13 : item.find ( "confidence") - 5]
 		t_conf = item [ item.find ( "confidence" ) + 13 : item.find ( "tag_id") - 4]
 		t_id = item [ item.find ( "tag_id" ) + 8 : -1]
		t2.insert (END, '{:50s}\t{:10s}\t{:20s}\t{:15s}\n'.format(t_name, t_conf, " ", t_id ) )
	t2.insert ( END, "-----------------------------------------------------------------------------------------------------------------\n" )

def analyzeText ( ):
	t2.insert ( INSERT,"Text analysis is in progress. Please wait..." )
	if  var.get ( ) == 1 :
		classifyType ( )
	else :
		classifyLevel ( )
	

root = Tk ( )
root.title ( "Text Analyzer" )
var = IntVar ( )
l1 = Label ( root, text = "TEXT INFORMATION ANALYSIS:", font = ("Times", "16", "bold") )
l1.grid ( row = 0,  column = 0, columnspan = 4, sticky = E+W )
l2 = Label ( root, text = "Enter your text below:", font = ("Times", "12", "bold") )
l2.grid ( row = 1, column = 0, sticky = W )
t1 = Text ( root )
t1.grid ( row = 2, column = 0, columnspan = 4, sticky = N+S+E+W )
r1 = Radiobutton ( root, text = "Information_Type_Classifier", variable = var, value = 1)
r1.grid ( row = 3, column = 1 ) 
r2 = Radiobutton ( root, text = "Cognitive_Level_Classifier", variable = var, value = 2) 
r2.grid ( row = 3, column = 2 ) 
b1 = Button ( root, text = "Submit", font = ("Times", "10", "bold"), command = analyzeText )
b1.grid ( row = 3, column = 3 ) 
t2 = Text ( root )
t2.grid ( row = 4, column = 0, columnspan = 4, sticky = N+S+E+W )
root.grid_columnconfigure ( 0, weight = 1 )
root.grid_rowconfigure ( 2, weight = 2 )
root.grid_rowconfigure ( 4, weight = 2 )
var.set(1);
root.mainloop( )	


