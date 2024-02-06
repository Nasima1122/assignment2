#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
text = 'Python Excercises, PHP excercises.'
print(re.sub("[,.]",":",text))


# In[2]:


import pandas as pd
import re
data={'SUMMARY':['hello,world!','     test','123four,five:;six']}
df=pd.DataFrame(data)
df['SUMMARY']=df['SUMMARY'].apply(lambda x:re.sub(r'[^\w\s]','',x))
print(df)


# In[3]:


import re
text='Do not bite the hand that feeds you.'
print(re.findall(r"\b\w{4,}\b",text))


# In[5]:


import re
text='An apple a day keeps the doctor away.'
print(re.findall(r"\b\w{3,5}\b",text))


# In[1]:


import re
text="ImportanceOfRegularExpressionInPython"
print(re.findall('[A-Z][^A-Z]*',text))


# In[4]:


import re
def capital_words_spaces(str1):
    pattern=r'(\d+)([A-Za-z]+)'
    result=re.sub(pattern,r' \1\2',str1)
    return result

text="RegularExpression1IsAn2ImportantTopic3InPython"
output=capital_words_spaces(text)
print(output)


# In[23]:


import re
def insert_spaces(text):
    
    pattern=r'([A-Z] [a-z 0-9] + |\d+)'
    
    result = re.sub (pattern, r' \1', text)
    
    result = result.strip()
    return result

sample_text ="RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_spaces(sample_text)
print(output)


# In[25]:


import re
def string_match(text):
    patterns='^[a-zA-Z0-9_]*$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return('Not matched!')
    
    
print(string_match("BHUFESTO is the new era of grandmother storytelling"))
print(string_match("Python_Exercises_1"))


# In[26]:


import re
def match_num(string):
    text=re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
print(match_num('5-2345861'))
print(match_num('6-2345861'))


# In[27]:


import re
ip ="192.268.0.0.001"
string=re.sub('\.[0]*','.',ip)
print(string)


# In[33]:


import re
sample_text="On August 15th 1947 thatIndia was declared independent from British colonialism,and the reins of control were handed over to the leaders of the country."
pattern=r"\b([A-Z][a-z]+) \d{1,2}(?:st|nd|rd|th)? \d{4}\b"

result=re.findall(pattern, sample_text)
print(result)


# In[40]:


import re
words = ['fox','dog','horse']
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in words:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern, text):
        print('matched!')
        
    else:
        print('not matched!')


# In[41]:


import re
pattern= 'fox'
text= 'The quick brown fox jumps over the lazy dog.'
match=re.search(pattern, text)
s=match.start()
e=match.end()
print('Found "%s" in "%s" from %d to %d'%\
     (match.re.pattern,match.string, s,e))


# In[42]:


import re
text = 'Python exercises,PHP exercises, C# exercises'
pattern='exercises'
for match in re.findall(pattern,text):
    print('Found "%s"' % match)


# In[44]:


import re
text= 'vista  chain kleen, vista chain lube, vista spray,vista spray'
pattern='vista'
for match in re.finditer(pattern, text):
    s= match.start()
    e=match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))


# In[45]:


import re
def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1',dt)
date1= "2024-02-05"
print("Original date in YYY-MM-DD Format: ",date1)
print("New date in DD-MM-YYY Format: ",change_date_format(date1))


# In[47]:


import re

def find_decimal_number(string):
    pattern= re.compile(r'\d+\.\d{1,2}')
    decimal_numbers = re.findall(pattern, string)
    return decimal_numbers

sample_text="01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
output=find_decimal_number(sample_text)
print(output)


# In[1]:


import re
text="My marks in each semester are:947, 896, 926, 524, 734, 950, 642"

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())


# In[5]:


import re

input ='My marks in each semester are:947, 896, 926, 524, 734, 950, 642'

value = re.findall(r'\d+',input)
value = [int(value) for value in value]

max_value =max(value)
print(max_value)


# In[6]:


import re
def capitalworld_space(str1):
    return re.sub(r"(\w)([A-Z])",r"\1 \2", str1)
print(capitalworld_space("RegularExpressionIsAnImportantTopicInPython"))


# In[7]:


import re
def text_match(text):
    patterns= '[A-Z]+[a-z]+$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return('Not match!')
    
print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
    


# In[13]:


import re
def removeDuplicateWords(input):
    reg= r'\b(\w+)(?:\W+\1\b)+'
    
    return re.sub(reg, r'\1', input, flags=re.IGNORECASE)

str1 = "Hello hello world world"
print(removeDuplicateWords(str1))


# In[ ]:




