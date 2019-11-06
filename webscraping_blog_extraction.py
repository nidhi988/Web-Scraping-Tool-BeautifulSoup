{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                            links\n",
      "title                                            \n",
      "Amit Agarwal               http://www.labnol.org/\n",
      "Jyotsna Kamat  http://www.kamat.com/jyotsna/blog/\n",
      "Amit Varma             http://www.indiauncut.com/\n",
      "Sidin Vadukut              http://www.whatay.com/\n",
      "Hawkeye           http://hawkeyeview.blogspot.in/\n",
      "363 rows written\n",
      "{'blogspot': 106, 'wordpress': 49, 'others': 208}\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup, Comment\n",
    "import pandas as pd\n",
    "import re\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "url='https://indianbloggers.org/'\n",
    "content = requests.get(url).text\n",
    "\n",
    "\n",
    "\n",
    "#initalizing an empty dictionary that would be written as Pandas Dataframe and then CSV\n",
    "d = {'title':[],'links':[]}\n",
    "\n",
    "#initializing blog hosting category\n",
    "cat = {'blogspot':0,'wordpress':0,'others':0}\n",
    "\n",
    "\n",
    "soup = BeautifulSoup(content, \"html.parser\")\n",
    "\n",
    "\n",
    "for link in soup.find_all('a',):\n",
    "    if len(link.text.strip()) > 1 and bool(re.match('^http',link['href'])) and not bool(re.search('indianbloggers|twitter|facebook',link['href'])):\n",
    "        d['title'].append(link.text)\n",
    "        d['links'].append(link['href'])\n",
    "        #finding the blog hosting type\n",
    "        if re.search('blogspot',link['href']):\n",
    "            cat['blogspot']+=1\n",
    "        elif re.search('wordpress',link['href']):\n",
    "            cat['wordpress']+=1\n",
    "        else:\n",
    "            cat['others']+=1\n",
    "        #d['len'].append(len(link.text.strip()))\n",
    "    \n",
    "blog_list = pd.DataFrame(d).set_index('title')\n",
    "\n",
    "\n",
    "print(blog_list.head())\n",
    "\n",
    "blog_list.to_csv('blog_list.csv', encoding='utf-8')\n",
    "\n",
    "print(str(len(blog_list.index))+' rows written')\n",
    "\n",
    "print(cat)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
