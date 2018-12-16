import subprocess
import sys 

def getRND(num):
	cmd = ("sudo dd status=noxfer if=/dev/hwrng bs=1 count={} 2>/dev/null | od -t x1".format(num))
	tmp = subprocess.Popen(
		cmd,stdout=subprocess.PIPE,
		shell=True).stdout.readlines()
	eles = []
	for ele in tmp:
		ele = ele.decode('utf-8').strip().split(' ')
		ele.pop(0)
		eles.append(ele)
	eles = [int(ee,16) for ele in eles for ee in ele] #flatten
	return eles
		
if __name__=='__main__':
	args = sys.argv
	if len(args)==2:
		num = args[1]
	else:
		num = 128
	
	arr = getRND(num)
	print(arr)

