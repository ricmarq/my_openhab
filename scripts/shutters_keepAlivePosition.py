#!/usr/bin/python

import sys

#janela
#print str(sys.argv[1])
janela=str(sys.argv[1])

#azimute
#print str(sys.argv[2])
azimute =float(str(sys.argv[2]))
#altitute
#print str(sys.argv[3])
altitute= float(str(sys.argv[3]))
#print 
#print 
#							 az  az  	alt alt  
#							 >=   <     >=  <     angulo perpendicular janala                      
# data = 			[["janelax", 234, 360, 	0,   180  ,300],
                 # ["janelay", 40, 50, 	0,   70   ,1  ],
				 # ["janelay", 45, 55, 	0,   70   ,1  ],
                 # ["janelay", 55, 60, 	0,   60   ,3 ]]
#							 az  az  	alt alt  
#							 >=   <     >=  <     angulo perpendicular janala 
data = 			[["janelax", 234,
							[
#						 az  az  	alt      alt  
#				    	 >= ,  <   ,   >=  	,<     angulo perpendicular janala    
						[234, 	359,   0  ,180],
						[359, 	360,   0  ,180]
							],
				],
                 ["janelax", 40, 50, 	0,   70   ,1  ],
				 ["janelax", 45, 55, 	0,   70   ,1  ],
                 ["janelax", 55, 60, 	0,   60   ,3 ]]

					 
				 
#for l in data:
found=0
for m in data:
	if (m[0] == janela)  :
		for n in m[2] :
			if ((n[0] <= azimute < n[1]) and  (n[2] <= altitute < n[3])) : 
				print "100"
				found=1
			break
		break
	
if found == 0 :
	print "0"

#and  (m[1] <= azimute < m[2]) and  (m[3] <= altitute < m[4]) 
				 
