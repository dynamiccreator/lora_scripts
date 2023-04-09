import sys
import os

#####USAGE
#python create-data-set-txt2txt.py filename cut_off_words
#Example: python create-data-set-txt2txt.py raw.txt 100 
#// 100 words cut_off_words is good for 256 tokens cut_off_length in lora fine tuning

cut_off_words=int(sys.argv[2])

f = open(sys.argv[1])
lines = f.readlines()
f.close()

output_file = open(sys.argv[1]+'_output.txt', 'w')
output_data=[]

lines = [line[:-1].rstrip('\n') for line in lines]
all_words=""

text=[]

print("reading...")
for li,l in enumerate(lines):
	w_arr="\\n"+l
	text.extend(w_arr.split(" "))

t_arr=[""]
i=0
rest=""
len_text_w=len(text)
progress=0

print("writing...")
for xi,x in enumerate(text):
	#print(x)
	if(i+1>len(t_arr)):
		t_arr.append(rest)
		rest=""
	t_arr[i]=str(t_arr[i])+" "+x
	split_t=t_arr[i].split(" ")
	if(len(split_t)==cut_off_words):
		i=i+1
		j=len(split_t)-1

		while(j>=0 and split_t[j].find(".")==-1
		and split_t[j].find("?")==-1
		and split_t[j].find("!")==-1
		and split_t[j].find(",")==-1
		and split_t[j].find(":")==-1
		and split_t[j].find(";")==-1
		and split_t[j].find("\\n")==-1):
			rest=split_t[j]+" "+rest
			j=j-1
		#print("REST= "+rest+"\n\n")
		temp_split_t=""
		ycount=0
		for y in split_t:
			if(ycount>j):
				break
			temp_split_t=temp_split_t.strip()+" "+y
			ycount=ycount+1
		t_arr[i-1]=temp_split_t

	if(int(100*(xi/len_text_w))>progress):
		print(str(progress)+" % written")
		progress=progress+1

for k in t_arr:
	output_file.write(k+"\n")
        
output_file.close()
	
print('Done')	
