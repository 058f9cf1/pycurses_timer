def templates(n):
	f = [1,1,1,1,1,1,1,1,1,1,1,1]
	l = [1,1,1,1,0,0,0,0,0,0,0,0]
	r = [0,0,0,0,0,0,0,0,1,1,1,1]
	g = [1,1,1,1,0,0,0,0,1,1,1,1]

	template_list =[[f,f,g,g,g,g,g,g,f,f],	#0
			[r,r,r,r,r,r,r,r,r,r],	#1
			[f,f,r,r,f,f,l,l,f,f],	#2
			[f,f,r,r,f,f,r,r,f,f],	#3
			[g,g,g,g,f,f,r,r,r,r],	#4
			[f,f,l,l,f,f,r,r,f,f],	#5
			[f,f,l,l,f,f,g,g,f,f],	#6
			[f,f,r,r,r,r,r,r,r,r],	#7
			[f,f,g,g,f,f,g,g,f,f],	#8
			[f,f,g,g,f,f,r,r,f,f]]	#9

	return template_list[n]
