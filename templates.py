def templates(n):
	f = [1,1,1,1,1,1,1,1,1,1,1,1]
	l = [1,1,1,1,0,0,0,0,0,0,0,0]
	r = [0,0,0,0,0,0,0,0,1,1,1,1]
	g = [1,1,1,1,0,0,0,0,1,1,1,1]

	template_list =[[f,g,g,g,f],	#0
					[r,r,r,r,r],	#1
					[f,r,f,l,f],	#2
					[f,r,f,r,f],	#3
					[g,g,f,r,r],	#4
					[f,l,f,r,f],	#5
					[f,l,f,g,f],	#6
					[f,r,r,r,r],	#7
					[f,g,f,g,f],	#8
					[f,g,f,r,f]]	#9

	return template_list[n]
