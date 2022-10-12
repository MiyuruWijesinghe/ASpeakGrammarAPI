sinhala = """

% start S

# S expansion productions
S -> NP[NUM=?n, GEN=?G, PER=?P, DEF=?TF] VP[NUM=?n, GEN=?G, PER=?P, CASE=?CS] 

# NP expansion productions 
NP[NUM=?n, CASE=?CS, GEN=?G, DEF=?TF] 	-> N[NUM=?n, CASE=?CS, GEN=?G] 
NP[NUM=?n, CASE=?CS, GEN=?G, PER=?P] 	-> PrN[NUM=?n, CASE=?CS, GEN=?G, PER=?P] 
NP[NUM=?n, CASE=?CS] 					-> PropN[NUM=?n, CASE=?CS] 
NP[NUM=?n, CASE=?CS, GEN=?G, DEF=?TF]  	-> Det N[NUM=?n, CASE=?CS, GEN=?G] 
NP[NUM=?n, CASE=?CS, GEN=?G, DEF=?TF]  	-> ADJP N[NUM=?n, CASE=?CS, GEN=?G] 
NP[NUM=?n, CASE=?CS, GEN=?G, DEF=?TF]  	-> Det ADJP N[NUM=?n, CASE=?CS, GEN=?G] 


# VP expansion productions
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> IV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> TV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> NP TV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> NP IV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> NP  NP TV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> NP  NP IV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> NP NP ADVP TV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> ADVP IV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> ADVP TV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> NP ADVP IV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]
VP[TENSE=?t, NUM=?n, GEN=?G, PER=?P] -> NP  ADVP TV[TENSE=?t, NUM=?n, GEN=?G, PER=?P]


# ADJP expansion productions 
ADJP -> Adj 
ADJP -> Adj ADJP  


# ADVP expansion productions
ADVP -> Adv[ADV=?A]
ADVP -> Adv[ADV=?A]Adv[ADV=?A]
ADVP -> Adv[ADV=?A]Adv[ADV=?A]Adv[ADV=?A]
ADVP -> Adv[ADV=?A]Adv[ADV=?B]
ADVP -> Adv[ADV=?A]Adv[ADV=?B]Adv[ADV=?C]
ADVP -> Adv[ADV=?A]Adv[ADV=?B]Adv[ADV=?A]
ADVP -> Adv[ADV=?A]Adv[ADV=?A]Adv[ADV=?B]
ADVP -> Adv[ADV=?A]Adv[ADV=?B]Adv[ADV=?B]
ADVP -> Adv[ADV=?A]Adv[ADV=?A]Adv[ADV=?B]Adv[ADV=?C]


# ###################
# Lexical Productions
# ###################

N[NUM=sg, GEN=MA, CASE=F1, DEF=TRue]   ->  'මිනිසා' | 'හොරා' 
N[NUM=sg, GEN=MA, CASE=F1, DEF=False]   -> 'මිනිසෙක්' | 'හොරෙක්' 
N[NUM=sg, GEN=MA, CASE=F2, DEF=TRue]   -> 'බල්ලා' | 'බුදුන්' 
N[NUM=sg, GEN=MA, CASE=F3, DEF=TRue]   -> 'මිනිසාට' | 'හොරාට' 
N[NUM=sg, GEN=MA, CASE=F3, DEF=False]   -> 'මිනිසෙක්ට' | 'හොරෙක්ට' 
N[NUM=sg, GEN=MA, CASE=F4, DEF=TRue]   -> 'මිනිසාගේ' | 'හොරාගේ' 
N[NUM=sg, GEN=MA, CASE=F4, DEF=False]   -> 'මිනිසෙක්ගේ' | 'හොරෙක්ගේ'
N[NUM=sg, GEN=MA, CASE=F5, DEF=TRue]   -> 'මිනිසාගෙන්' | 'හොරාගෙන්' 
N[NUM=sg, GEN=MA, CASE=F5, DEF=False]   -> 'මිනිසෙක්ගෙන්' | 'හොරෙක්ගෙන්'
N[NUM=sg, GEN=FE, CASE=F1, DEF=TRue]   -> 'කාන්තාව' | 'හෙර'  
N[NUM=sg, GEN=FE, CASE=F1, DEF=False]   -> 'කාන්තාවක්' | 'හෙරක්' 
N[NUM=sg, GEN=FE, CASE=F2, DEF=TRue]   -> 'ගැහැණිය' 
N[NUM=sg, GEN=FE, CASE=F2, DEF=False]   -> 'ගැහැණියක' 
N[NUM=sg, GEN=FE, CASE=F3, DEF=TRue]   -> 'කාන්තාවට' | 'හෙරට' 
N[NUM=sg, GEN=FE, CASE=F3, DEF=False]   -> 'කාන්තාවකට' | 'හෙරකට'  
N[NUM=sg, GEN=FE, CASE=F4, DEF=TRue]   -> 'කාන්තාවගේ' | 'හෙරගේ' 
N[NUM=sg, GEN=FE, CASE=F4, DEF=False]   -> 'කාන්තාවකගේ' | 'හෙරකගේ' 
N[NUM=sg, GEN=FE, CASE=F5, DEF=TRue]   -> 'කාන්තාවගෙන්' | 'හෙරගෙන්' 
N[NUM=sg, GEN=FE, CASE=F5, DEF=False]   -> 'කාන්තාවකගෙන්' | 'හෙරකගෙන්'
N[NUM=sg, GEN=NE, CASE=F1, DEF=TRue]   -> 'සමාජය' | 'වෙලාව' | 'ඇග' | 'ගෙදර'
N[NUM=sg, GEN=NE, CASE=F1, DEF=False]   -> 'සමාජයක්' | 'වෙලාවක්' | 'ඇගක්' | 'ගෙදරක්'
N[NUM=sg, GEN=NE, CASE=F3, DEF=TRue]   -> 'සමාජයට' | 'වෙලාවට' | 'ඇගට' | 'ගෙදරට'
N[NUM=sg, GEN=NE, CASE=F3, DEF=False]   -> 'සමාජයකට' | 'වෙලාවකට' | 'ඇගකට' | 'ගෙදරකට'
N[NUM=sg, GEN=NE, CASE=F4, DEF=TRue]   -> 'සමාජයේ' | 'වෙලාවේ' | 'ඇගේ' | 
N[NUM=sg, GEN=NE, CASE=F4, DEF=False]   -> 'සමාජයක' | 'වෙලාවක' | 'ඇගක' | 'ගෙදරක'
N[NUM=sg, GEN=NE, CASE=F5, DEF=TRue]   -> 'සමාජයෙන්' | 'වෙලාවෙන්' | 'ඇගෙන්' | 'ගෙදරෙන්'
N[NUM=sg, GEN=NE, CASE=F5, DEF=False]   -> 'සමාජයකින්' | 'වෙලාවකින්' | 'ඇගකින්' | 'ගෙදරකින්'
N[NUM=pl, GEN=MA, CASE=F1]   -> 'මිනිස්සු' | 'හොරු' 
N[NUM=pl, GEN=MA, CASE=F2]   -> 'මිනිසුන්' | 'හොරුන්' 
N[NUM=pl, GEN=MA, CASE=F3]   -> 'මිනිසුන්ට' | 'හොරුන්ට'  
N[NUM=pl, GEN=MA, CASE=F4]   -> 'මිනිසුන්ගේ' | 'හොරුන්ගේ' 
N[NUM=pl, GEN=MA, CASE=F5]   -> 'මිනිසුන්ගෙන්' | 'හොරුන්ගෙන්' 
N[NUM=pl, GEN=FE, CASE=F1]   -> 'කාන්තාවෝ' 
N[NUM=pl, GEN=FE, CASE=F2]   -> 'කාන්තාවන්' 
N[NUM=pl, GEN=FE, CASE=F3]   -> 'කාන්තාවන්ට' 
N[NUM=pl, GEN=FE, CASE=F4]   -> 'කාන්තාවන්ගේ' 
N[NUM=pl, GEN=FE, CASE=F5]   -> 'කාන්තාවන්ගෙන්' 
N[NUM=pl, GEN=NE, CASE=F1]   -> 'සල්ලී' | 'පව්' 
N[NUM=pl, GEN=NE, CASE=F3]   -> 'සල්ලීවලට' | 'පව්වලට' 
N[NUM=pl, GEN=NE, CASE=F4]   -> 'සල්ලීවල' | 'පව්වල' 
N[NUM=pl, GEN=NE, CASE=F5]   -> 'සල්ලීවලින්' | 'පව්වලින්' 
PropN[NUM=sg, GEN=MA, CASE=F1] -> 'ජයසේන' 
PropN[NUM=sg, GEN=MA, CASE=F3] -> 'ජයසේනට'
PropN[NUM=sg, GEN=FE, CASE=F1] -> 'නන්දා' 
PropN[NUM=sg, GEN=FE, CASE=F3] -> 'නන්දාට' 
PrN[NUM=sg, GEN=MA, CASE=F1, PER=T] -> 'ඔහු' | 'එයා'  
PrN[NUM=sg, GEN=MA, CASE=F2, PER=T] -> 'ඔහුව' | 'එයාව' 
PrN[NUM=sg, GEN=MA, CASE=F3, PER=T] -> 'ඔහුට' | 'එයාට'  
PrN[NUM=sg, GEN=MA, CASE=F4, PER=T] -> 'ඔහුගේ' | 'එයාගේ' 
PrN[NUM=sg, GEN=MA, CASE=F5, PER=T] -> 'ඔහුගෙන්' | 'එයාගෙන්' 
PrN[NUM=sg, GEN=FE, CASE=F1, PER=T] -> 'ඇය' 
PrN[NUM=sg, GEN=FE, CASE=F2, PER=T] -> 'ඇයව' 
PrN[NUM=sg, GEN=FE, CASE=F3, PER=T] -> 'ඇයට' 
PrN[NUM=sg, GEN=FE, CASE=F4, PER=T] -> 'ඇයගේ' 
PrN[NUM=sg, GEN=FE, CASE=F5, PER=T] -> 'ඇයගෙන්' 
PrN[NUM=pl, CASE=F1, PER=T] -> 'ඒගොල්ලො' 
PrN[NUM=pl, CASE=F2, PER=T] -> 'ඔවුන්' | 'ඒගොල්ලන්' 
PrN[NUM=pl, CASE=F3, PER=T] -> 'ඔවුන්ට' | 'ඒගොල්ලන්ට' 
PrN[NUM=pl, CASE=F4, PER=T] -> 'ඔවුන්ගේ' | 'ඒගොල්ලන්ගේ' 
PrN[NUM=pl, CASE=F5, PER=T] -> 'ඔවුන්ගෙන්' | 'ඒගොල්ලන්ගෙන්' 
PrN[NUM=sg, CASE=F1, PER=S] -> 'ඔබ' | 'ඔයා' 
PrN[NUM=sg, CASE=F2, PER=S] -> 'ඔබව' | 'ඔයාව' 
PrN[NUM=sg, CASE=F3, PER=S] -> 'ඔබ‍ට' | 'ඔයාට' 
PrN[NUM=sg, CASE=F4, PER=S] -> 'ඔබගේ' | 'ඔයාගේ' 
PrN[NUM=sg, CASE=F5, PER=S] -> 'ඔබගෙන්' | 'ඔයාගෙන්' 
PrN[NUM=pl, CASE=F1, PER=S] -> 'ඔබලා' 
PrN[NUM=pl, CASE=F2, PER=S] -> 'ඔබලා' 
PrN[NUM=pl, CASE=F3, PER=S] -> 'ඔබලාට' 
PrN[NUM=pl, CASE=F4, PER=S] -> 'ඔබලාගේ' 
PrN[NUM=pl, CASE=F5, PER=S] -> 'ඔබලාගෙන්' 
PrN[NUM=sg, CASE=F1, PER=F] -> 'මම' 
PrN[NUM=sg, CASE=F2, PER=F] -> 'මා' 
PrN[NUM=sg, CASE=F3, PER=F] -> 'මට' 
PrN[NUM=sg, CASE=F4, PER=F] -> 'මගේ' 
PrN[NUM=sg, CASE=F5, PER=F] -> 'මගෙන්' 
PrN[NUM=pl, CASE=F1, PER=F] -> 'අපි' 
PrN[NUM=pl, CASE=F2, PER=F] -> 'අප' 
PrN[NUM=pl, CASE=F3, PER=F] -> 'අපට' 
PrN[NUM=pl, CASE=F4, PER=F] -> 'අපගේ' | 'අපේ' 
PrN[NUM=pl, CASE=F5, PER=F] -> 'අපගෙන්' | 'අපෙන්' 
Det -> 'ඒ' | 'මේ' | 'අර' | 'ඔය' | 'සමහර' | 'ඇතැම්' 
Adj -> 'අඳුරු' | 'ලා' | 'පරක්කු' 

IV[TENSE=Npast,  NUM=sg, GEN=MA, VLT=True, PER=T] -> 'යනවා' | 'කනවා' | 'බොනවා' | 'එනවා' | 'ඉන්නවා' | 'හොයනවා' | 'සෝදනවා' | 'කරනවා'
IV[TENSE=Npast,  NUM=sg, GEN=FE, VLT=True, PER=T] -> 'යනවා' | 'කනවා' | 'බොනවා' | 'එනවා' | 'ඉන්නවා' | 'හොයනවා' | 'සෝදනවා' | 'කරනවා'
IV[TENSE=Npast,  NUM=sg, GEN=MA, VLT=False, PER=T] -> 'යනවා' | 'කනවා' | 'බොනවා' | 'එනවා' | 'ඉන්නවා' | 'හොයනවා' | 'සෝදනවා' | 'කරනවා'
IV[TENSE=Npast,  NUM=sg, GEN=NE, VLT=False, PER=T] -> 'යනවා' | 'කනවා' | 'බොනවා' | 'එනවා' | 'ඉන්නවා' | 'හොයනවා' | 'සෝදනවා' | 'කරනවා'
IV[TENSE=Npast,  NUM=pl, VLT=True, PER=T] -> 'යනවා' | 'කනවා' | 'බොනවා' | 'එනවා' | 'ඉන්නවා' | 'හොයනවා' | 'සෝදනවා' | 'කරනවා'
IV[TENSE=Npast,  NUM=sg, VLT=True, PER=S] -> 'යන්න' | 'කන්න' | 'බොන්න' | 'එන්න' | 'ඉන්න' | 'හොයන්න' | 'සෝදන්න' | 'කරන්න'
IV[TENSE=Npast,  NUM=pl, VLT=True, PER=S] -> 'යනවාද' | 'කනවාද' | 'බොනවාද' | 'එනවාද' | 'ඉන්නවාද' | 'හොයනවාද' | 'සෝදනවාද' | 'කරනවාද' | 'කොහෙද' | 'කාගෙද'
IV[TENSE=Npast,  NUM=sg, VLT=True, PER=F] -> 'යනවා' | 'යන්නම්' | 'කනවා' | 'කන්නම්' | 'බොනවා' | 'බොන්නම්' | 'එනවා' | 'එන්නම්' | 'ඉන්නවා' | 'ඉන්නම්' | 'හොයනවා' | 'හොයන්නම්' | 'සෝදනවා' | 'සෝදන්නම්' | 'කරනවා' | 'කරන්නම්'
IV[TENSE=Npast,  NUM=pl, VLT=True, PER=F] -> 'යමු' | 'යනවා' | 'යන්නම්' | 'කමු' | 'කනවා' | 'කන්නම්' | 'බොමු' | 'බොනවා' | 'බොන්නම්' | 'එමු' | 'එනවා' | 'එන්නම්' | 'ඉමු' | 'ඉන්නවා' | 'ඉන්නම්' | 'හොයමු' | 'හොයනවා' | 'හොයන්නම්' | 'සෝදමු' | 'සෝදනවා' | 'සෝදන්නම්' | 'කරමු' | 'කරනවා' | 'කරන්නම්'

IV[TENSE=past,  NUM=sg, GEN=MA, VLT=True, PER=T] -> 'ගියා' | 'කෑවා' | 'බිව්වා' | 'ආවා' | 'හිටියා' | 'හෙව්වා' | 'සේදුවා' | 'කරා'
IV[TENSE=past,  NUM=sg, GEN=FE, VLT=True, PER=T] -> 'ගියා' | 'කෑවා' | 'බිව්වා' | 'ආවා' | 'හිටියා' | 'හෙව්වා' | 'සේදුවා' | 'කරා'
IV[TENSE=past,  NUM=sg, VLT=False, PER=T] -> 'ගියා' | 'කෑවා' | 'බිව්වා' | 'ආවා' | 'හිටියා' | 'හෙව්වා' | 'සේදුවා' | 'කරා'
IV[TENSE=past,  NUM=pl, VLT=True, PER=T] -> 'ගියා' | 'කෑවා' | 'බිව්වා' | 'ආවා' | 'හිටියා' | 'හෙව්වා' | 'සේදුවා' | 'කරා'
IV[TENSE=past,  NUM=sg, VLT=True, PER=S] -> 'ගියාද' | 'කෑවාද' | 'බිව්වාද' | 'ආවාද' | 'හිටියාද' | 'හෙව්වාද' | 'සේදුවාද' | 'කරාද' | 'කොහෙද' | 'කාගෙද'
IV[TENSE=past,  NUM=pl, VLT=True, PER=S] -> 'ගියාද' | 'කෑවාද' | 'බිව්වාද' | 'ආවාද' | 'හිටියාද' | 'හෙව්වාද' | 'සේදුවාද' | 'කරාද' | 'කොහෙද' | 'කාගෙද'
IV[TENSE=past,  NUM=sg, VLT=True, PER=F] -> 'ගියා' | 'කෑවා' | 'බිව්වා' | 'ආවා' | 'හිටියා' | 'හෙව්වා' | 'සේදුවා' | 'කරා'
IV[TENSE=past,  NUM=pl, VLT=True, PER=F] -> 'ගියා' | 'කෑවා' | 'බිව්වා' | 'ආවා' | 'හිටියා' | 'හෙව්වා' | 'සේදුවා' | 'කරා'

TV[TENSE=Npast,  NUM=sg, GEN=MA, VLT=True, PER=T] -> 'යයි' | 'කයි' | 'බොයි' | 'එයි' | 'ඉදියි' | 'හොයයි' | 'සෝදයි' | 'කරයි'
TV[TENSE=Npast,  NUM=sg, GEN=FE, VLT=True, PER=T] -> 'යයි' | 'කයි' | 'බොයි' | 'එයි' | 'ඉදියි' | 'හොයයි' | 'සෝදයි' | 'කරයි'
TV[TENSE=Npast,  NUM=sg, VLT=False] -> 'යනවා' | 'කනවා' | 'බොනවා' | 'එනවා' | 'ඉන්නවා' | 'හොයනවා' | 'සෝදනවා' | 'කරනවා'
TV[TENSE=Npast,  NUM=pl, VLT=False] -> 'යනවා' | 'කනවා' | 'බොනවා' | 'එනවා' | 'ඉන්නවා' | 'හොයනවා' | 'සෝදනවා' | 'කරනවා'
TV[TENSE=Npast,  NUM=pl, VLT=True, PER=T] -> 'යනවා' | 'කනවා' | 'බොනවා' | 'එනවා' | 'ඉන්නවා' | 'හොයනවා' | 'සෝදනවා' | 'කරනවා'
TV[TENSE=Npast,  NUM=sg, VLT=True, PER=S] -> 'යනවාද' | 'කනවාද' | 'බොනවාද' | 'එනවාද' | 'ඉන්නවාද' | 'හොයනවාද' | 'සෝදනවාද' | 'කරනවාද' | 'කොහෙද' | 'කාගෙද'
TV[TENSE=Npast,  NUM=pl, VLT=True, PER=S] -> 'යනවාද' | 'කනවාද' | 'බොනවාද' | 'එනවාද' | 'ඉන්නවාද' | 'හොයනවාද' | 'සෝදනවාද' | 'කරනවාද' | 'කොහෙද' | 'කාගෙද'
TV[TENSE=Npast,  NUM=sg, VLT=True, PER=F] -> 'යනවා' | 'යන්නම්' | 'කනවා' | 'කන්නම්' | 'බොනවා' | 'බොන්නම්' | 'එනවා' | 'එන්නම්' | 'ඉන්නවා' | 'ඉන්නම්' | 'හොයනවා' | 'හොයන්නම්' | 'සෝදනවා' | 'සෝදන්නම්' | 'කරනවා' | 'කරන්නම්'
TV[TENSE=Npast,  NUM=pl, VLT=True, PER=F] -> 'යමු' | 'යනවා' | 'යන්නම්' | 'කමු' | 'කනවා' | 'කන්නම්' | 'බොමු' | 'බොනවා' | 'බොන්නම්' | 'එමු' | 'එනවා' | 'එන්නම්' | 'ඉමු' | 'ඉන්නවා' | 'ඉන්නම්' | 'හොයමු' | 'හොයනවා' | 'හොයන්නම්' | 'සෝදමු' | 'සෝදනවා' | 'සෝදන්නම්' | 'කරමු' | 'කරනවා' | 'කරන්නම්'

TV[TENSE=past,  NUM=sg, GEN=MA, VLT=True, PER=T] -> 'ගියා' | 'කෑවා' | 'බිව්වා' | 'ආවා' | 'හිටියා' | 'හෙව්වා' | 'සේදුවා' | 'කරා'
TV[TENSE=past,  NUM=sg, GEN=FE, VLT=True, PER=T] -> 'ගියා' | 'කෑවා' | 'බිව්වා' | 'ආවා' | 'හිටියා' | 'හෙව්වා' | 'සේදුවා' | 'කරා'
TV[TENSE=past,  NUM=sg, GEN=MA, VLT=False, PER=T] -> 'ගියා' | 'කෑවා' | 'බිව්වා' | 'ආවා' | 'හිටියා' | 'හෙව්වා' | 'සේදුවා' | 'කරා'
TV[TENSE=past,  NUM=pl, VLT=True, PER=T] -> 'ගියා' | 'කෑවා' | 'බිව්වා' | 'ආවා' | 'හිටියා' | 'හෙව්වා' | 'සේදුවා' | 'කරා'
TV[TENSE=past,  NUM=sg, VLT=True, PER=S] -> 'ගියාද' | 'කෑවාද' | 'බිව්වාද' | 'ආවාද' | 'හිටියාද' | 'හෙව්වාද' | 'සේදුවාද' | 'කරාද' | 'කොහෙද' | 'කාගෙද'
TV[TENSE=past,  NUM=pl, VLT=True, PER=S] -> 'ගියාද' | 'කෑවාද' | 'බිව්වාද' | 'ආවාද' | 'හිටියාද' | 'හෙව්වාද' | 'සේදුවාද' | 'කරාද' | 'කොහෙද' | 'කාගෙද'
TV[TENSE=past,  NUM=sg, VLT=True, PER=F] -> 'ගියා' | 'කෑවා' | 'බිව්වා' | 'ආවා' | 'හිටියා' | 'හෙව්වා' | 'සේදුවා' | 'කරා'
TV[TENSE=past,  NUM=pl, VLT=True, PER=F] -> 'ගියා' | 'කෑවා' | 'බිව්වා' | 'ආවා' | 'හිටියා' | 'හෙව්වා' | 'සේදුවා' | 'කරා'

Adv -> 'ඊයේ' | 'හෙට' | 'අද' | 'අනිද්දා' | 'පෙරේදා' | 'අදින්' | 'හෙටින්' | 'පිරිසිදු'

"""
