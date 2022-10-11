from datetime import datetime
from flask import Flask
from flask import Response
from SinhalaGrammarRules import sinhala
from nltk import grammar, parse
from flask import request
import json
import string
import numpy as np
import requests
from requests.structures import CaseInsensitiveDict
import urllib.request

app = Flask(__name__)

@app.route('/check-grammar', methods=['GET', 'POST'])
def upload():
    try:
        singram = grammar.FeatureGrammar.fromstring(sinhala)
        parser = parse.FeatureEarleyChartParser(singram)
        strLine = request.json['inputText']
        
        #****************************
        url = "https://easysinhalaunicode.com/Api/convert"

        #headers = CaseInsensitiveDict()
        #headers["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        #headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"

        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        content_type = 'application/x-www-form-urlencoded; charset=UTF-8'
        headers = {'User-Agent': user_agent, 'Content-Type': content_type}
        #data = strLine
        print('strLine is : '+strLine)
        #print('data is : '+data)
        print(url)
        print(headers)

        values = {'data': strLine }
        print(values)
        data = urllib.parse.urlencode(values)
        print(data)
        data = data.encode('utf-8')
        print(data)
        res = urllib.request.urlopen(url, data, headers)
        print('***********')
        #resdata = res.read()
        print(res)

        #res = requests.post(url, headers=headers, data=data)
        #jsonData = res.json()
        #for data in jsonData:
        #    print(data)
        
        print(res.text)
        sinhalaText = res.text
        print('Singlish : '+sinhalaText)

        #**************************

        tokens = strLine.split()
        trees = parser.parse(tokens)

        chkStrgFirst = "Test"
        chkStrgFinal = "Test"

        sentenceSize = []

        print('tokens : '+str(tokens))
        print(len(tokens))

        if len(tokens) == 2:
            print('in 2nd node')
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

        if len(tokens) == 3:
            print('in 3rd node')
            i = 0
            for tree in trees:

                for node in tree:

                    for nodenode in node:
                        if i == 0:
                            chkStrgFirst = str(nodenode)
                            print(str(nodenode) + '\n')
                        i = i + 1
                        chkStrgFinal = str(nodenode)

        if len(tokens) == 4:
            print('in 4th node')
            i = 0
            for tree in trees:
                for node in tree:

                    for nodenode in node:

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

        print("***************")

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
        gramr = "correct grammar"

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

        #print(sentenceSize)

        jObj = {}
        jObj["inputText"] = strLine
        jObj["isCorrectGrammar"] = gramr
        jObj["tense"] = tense
        jObj["numberOfGrammar"] = singular_plural

    except Exception as e:
        print (e)
        tense = "Wrong tense."
        singular_plural = "Wrong grammar number."
        gramr = "Wrong grammar."
        jObj = {}
        jObj["inputText"] = strLine
        jObj["isCorrectGrammar"] = gramr
        jObj["tense"] = tense
        jObj["numberOfGrammar"] = singular_plural

    return Response(json.dumps(jObj), mimetype='application/json')


@app.route('/test', methods=['GET', 'POST'])
def res_massage():
    return "Hello User!"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
