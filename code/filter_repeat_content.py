#!/usr/bin/env python
import codecs


lines = []
def test():
	f = codecs.open('part2.txt','rb','utf-8')
	for line in f.readlines():
		line = line.replace('\n','').replace('\r','').strip()
		if line not in lines:
			lines.append(line)
			print(line)
			f1= codecs.open('zhidao_question_to_answer_part2.txt','a','utf-8')
			f1.write(line+'\n')
			f1.close()


	f.close()


test()