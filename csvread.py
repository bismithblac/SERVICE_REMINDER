import csv
import codecs

def csvRead(filename):
	raw1 = csv.DictReader(codecs.open(filename, 'rU', 'utf-16'),delimiter='\t')
	filename=filename.split('.')
	filename=filename[0].strip()	
	files=open(filename+'Refined.txt','w+')
	#raw2=csv.reader(raw1,delimiter='\t')
	for line in raw1:
		files.write(line['Mobile Phone']+','+(line['Contact First Name']).replace(',',' ').replace('.','')+','+line['License Number']+'\n')

	files.close()	
	return

