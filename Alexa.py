#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 16:32:16 2018

@author: AppleMoony
"""

import random
def lambda_handler(event, context):
    endSession=True
    sa={}
    output_speech_text="This shouldn't happen"
    
    if event["request"]["type"]=="LaunchRequest":
        output_speech_text="Hello  world"
        
    
    elif event["request"]["type"]=="IntentRequest":
        if event["request"]["intent"]["name"]=="RandomNumberIntent":
            if ("value" in event["request"]["intent"]["slots"]["low"]) and ("value" in event["request"]["intent"]["slots"]["high"]):
                if event["request"]["intent"]["slots"]["low"]["value"]!='?' and event["request"]["intent"]["slots"]["high"]["value"]!='?':
                    value1=event["request"]["intent"]["slots"]["low"]["value"]
                    value2=event["request"]["intent"]["slots"]["high"]["value"]
                    random_num=random.randint(int(value1), int(value2))
                
                elif event["request"]["intent"]["slots"]["low"]["value"]!='?':
                    value1=event["request"]["intent"]["slots"]["low"]["value"]
                    random_num=random.randint(int(value1), 10)

                elif event["request"]["intent"]["slots"]["high"]["value"]!='?':
                    value2=event["request"]["intent"]["slots"]["high"]["value"]
                    random_num=random.randint(0, int(value2))
            
            else:
                random_num=random.randint( 1,10)
        
            output_speech_text="OK, The random number is "+str(random_num)
            
        elif event["request"]["intent"]["name"]=="DoArithmeticIntent":
            if "attributes" in event["session"] and "number" in event["session"]["attributes"]:
                value1=event["session"]["attributes"]["number"]
                if ("value" in event["request"]["intent"]["slots"]["first"]) and not("value" in event["request"]["intent"]["slots"]["second"]):
                    value2=event["request"]["intent"]["slots"]["first"]["value"]
                if event["session"]["attributes"]["operation"]=="add":
                    result=int(value1)+int(value2)
                if event["session"]["attributes"]["operation"]=="multiply":
                    result=int(value1)*int(value2)    
                output_speech_text=str(result)
            else:
                value1=event["request"]["intent"]["slots"]["first"]["value"]
                value2=event["request"]["intent"]["slots"]["second"]["value"]    
                try:
                    if event["request"]["intent"]["slots"]["operation"]["value"]=="add":
                        result=int(value1)+int(value2)
                    if event["request"]["intent"]["slots"]["operation"]["value"]=="multiply":
                        result=int(value1)*int(value2) 
                    output_speech_text=str(result)
                except:
                    if event["request"]["intent"]["slots"]["first"]["value"]=='?':
                        value1=event["request"]["intent"]["slots"]["second"]["value"]
                    else:
                        value1=event["request"]["intent"]["slots"]["first"]["value"]
                    sa["number"]=value1
                    sa["operation"]=event["request"]["intent"]["slots"]["operation"]["value"]
                    output_speech_text="Sorry, I didn't catch the second number, can you repeat it?"
                    endSession=False

                

   
        elif event["request"]["intent"]["name"]=="AMAZON.HelpIntent":
            output_speech_text="Sorry, no help is available"

        else:
            output_speech_text="not going to happen"

    else:
        pass
        
   
    
    output_speech_object={"type":"PlainText", "text":output_speech_text}
    response_object={"outputSpeech": output_speech_object, "shouldEndSession": endSession}
    response={"version": "1.0", "response":response_object, "sessionAttributes": sa }
    return response