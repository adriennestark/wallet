{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "JSONDecodeError",
     "evalue": "Expecting value: line 1 column 1 (char 0)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mJSONDecodeError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-26bef6a60526>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0mp_status\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwait\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m \u001b[0mkeys\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mjson\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mloads\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moutput\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkeys\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/json/__init__.py\u001b[0m in \u001b[0;36mloads\u001b[0;34m(s, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)\u001b[0m\n\u001b[1;32m    355\u001b[0m             \u001b[0mparse_int\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mparse_float\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;32mand\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    356\u001b[0m             parse_constant is None and object_pairs_hook is None and not kw):\n\u001b[0;32m--> 357\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0m_default_decoder\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdecode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    358\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mcls\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    359\u001b[0m         \u001b[0mcls\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mJSONDecoder\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/json/decoder.py\u001b[0m in \u001b[0;36mdecode\u001b[0;34m(self, s, _w)\u001b[0m\n\u001b[1;32m    335\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    336\u001b[0m         \"\"\"\n\u001b[0;32m--> 337\u001b[0;31m         \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mraw_decode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0midx\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0m_w\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    338\u001b[0m         \u001b[0mend\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_w\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    339\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mend\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/json/decoder.py\u001b[0m in \u001b[0;36mraw_decode\u001b[0;34m(self, s, idx)\u001b[0m\n\u001b[1;32m    353\u001b[0m             \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscan_once\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0midx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    354\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mStopIteration\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 355\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mJSONDecodeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Expecting value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    356\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mJSONDecodeError\u001b[0m: Expecting value: line 1 column 1 (char 0)"
     ]
    }
   ],
   "source": [
    "import subprocess\n",
    "import json\n",
    "\n",
    "command = './derive -g --mnemonic=\"oblige monkey actual pudding ramp affair unveil nut belt input dust happy\" --cols=path,address,privkey,pubkey --format=json'\n",
    "\n",
    "p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)\n",
    "output, err = p.communicate()\n",
    "p_status = p.wait()\n",
    "\n",
    "keys = json.loads(output)\n",
    "print(keys)\n"
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
