from datetime import datetime
from SinhalaGrammarRules import sinhala
from nltk import grammar, parse
import json
import string
import numpy as np
import requests
from requests.structures import CaseInsensitiveDict

def checkGrammar(sentence):
    try:
        singram = grammar.FeatureGrammar.fromstring(sinhala)
        parser = parse.FeatureEarleyChartParser(singram)
        strLine = sentence
        
        url = "https://easysinhalaunicode.com/Api/convert"

        headers = CaseInsensitiveDict()
        headers["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        data = "data="+strLine
        print('strLine is : '+strLine)
        print('data is : '+data)
         
        res = requests.post(url, headers=headers, data=data)
        print('singlish API response : '+res.text)
        
        sinhalaText = res.text
        print('Sinhala is : '+sinhalaText)

        tokens = sinhalaText.split()
        trees = parser.parse(tokens)

        chkStrgFirst = "Test"
        chkStrgFinal = "Test"

        print('tokens & length : '+str(tokens))
        print(len(tokens))

        if len(tokens) > 1:
            i = 0
            for tree in trees:
                for node in tree:
                    for nodenode in node:
                        print(str(node))
                        if i == 0:
                            chkStrgFirst = str(nodenode)
                            print(str(nodenode) + '\n')
                        i = i + 1
                        chkStrgFinal = str(nodenode)

        print(chkStrgFirst)
        print(chkStrgFinal)

        chkStrgFirstArry = chkStrgFirst.split("[")
        chkStrgFirst = chkStrgFirstArry[1]
        chkStrgFirstArry = chkStrgFirst.split("]")
        chkStrgFirst = chkStrgFirstArry[0]
        print(chkStrgFirst)

        chkStrgFinalArry = chkStrgFinal.split("[")
        chkStrgFinal = chkStrgFinalArry[1]
        chkStrgFinalArry = chkStrgFinal.split("]")
        chkStrgFinal = chkStrgFinalArry[0]
        print(chkStrgFinal)

        jstre = json.dumps(tree)
        jsting = json.loads(jstre)
        newstr = str(jsting)
        newstr02 = newstr.replace("[", "")
        newstr03 = newstr02.replace("]", "")
        print(newstr03)

        tense = "test"
        singular_plural = "test"
        gramr = "Correct grammar"

        if "TENSE='Npast'" in chkStrgFinal:
            tense = "present"
        if "TENSE='past'" in chkStrgFinal:
            tense = "past"
        if "NUM='pl'" in chkStrgFirst and "NUM='pl'" in chkStrgFinal:
            singular_plural = "plural"
        if "NUM='sg'" in chkStrgFirst and "NUM='sg'" in chkStrgFinal:
            singular_plural = "singular"
        if tense == "test" or singular_plural == "test":
            gramr = "Wrong grammar"

        jObj = {}
        jObj["inputText"] = strLine
        jObj["sinhalaText"] = sinhalaText
        jObj["isCorrectGrammar"] = gramr
        jObj["tense"] = tense
        jObj["numberOfGrammar"] = singular_plural

    except Exception as e:
        print (e)
        tense = "Wrong tense"
        singular_plural = "Wrong grammar number"
        gramr = "Wrong grammar"
        jObj = {}
        jObj["inputText"] = strLine
        jObj["sinhalaText"] = sinhalaText
        jObj["isCorrectGrammar"] = gramr
        jObj["tense"] = tense
        jObj["numberOfGrammar"] = singular_plural

    print(jObj)
    return jObj
