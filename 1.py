#r=3
#p=3.14
#l=2*p*r
#s=p*r**2
#print(l)
#print(s)
#print('    *')
#print('   ***')
#print('  *****')
#print(' *******')
#s=input('输入多少两：')
#j=int(s)//16
#l=int(s)%16
#print(j,'斤')
#print(l,'两')
#s=input('输入多少秒:')
#h=int(s)//3600
#if h==0
#m=int(s)//60
#else 
#print(h)
#else if se=int(s)-60
#print(h) 
#print(m)
#print(se)
#s=input('输入秒:')
#h=int(s)//3600
#m=(int(s)-h*3600)//60
#se=int(s)-h*3600-m*60
#print('现在是',h,':',m,':',se)
#s=input('输入数字')
#s=int(s)%2
#if s <1 :
#	print('偶数')
#else:
#	print('奇数')
#s=input('输入三位数')
#b=int(s)//100
#sh=(int(s)-int(b)*100)//10
#g=(int(s)-int(sh)*10)-int(b)*100//1
#print('百位数%d,十位数%d,个位数%d'%(b,sh,g))
#s=input('输入三位数')
#if int(s)<=999 and int(s)>=100:
#	b=int(s)//100
#	sh=(int(s)-int(b)*100)//10
#	g=(int(s)-int(sh)*10)-int(b)*100//1
#	if b%7==0:
#		print('含数字７') 
#	elif sh%7==0:
#		print( '含数字７')
#	elif g%7==0:
#		print('含数字７')
#pi=3.14
#i=int(pi)
#f=pi-i
#if　float(f)==0.14:
#	print('相等')
#while True:
#	a=int(input('输入月份'))
#	if a>=1 and a<=3:
#		print('1季度')
#	elif a>=4 and a<=6:
#		print('2季度')
#	elif a>=7 and a<=9:
#		print('3季度')
#	elif a>=10 and a<= 12:
#		print('4季度')
#	else :
#		print('请输入正确月份')
#	if input('退出按空格')==' ':
#		break
#a=int(input('输入分数'))
#if 0<=a<=59:
#	print('不及格')
#elif 60<=a<=79:
#	print('及格')
#elif 80<=a<=89:
#	print('良好')
#elif 90<=a<=100:
#	print('优秀')
#else :
#	print('输入错误')

#while True:
#	s=input('输入三位数(跳出按空格)')
#	if s == ' ':
#         break
#	if int(s)<=999 and int(s)>=100:
#		b=int(s)//100
#		sh=(int(s)-int(b)*100)//10
#		g=(int(s)-int(sh)*10)-int(b)*100//1
#		if b%7==0:
#			print('含数字７') 
#		elif sh%7==0:
#			print( '含数字７')
#		elif g%7==0:
#			print('含数字７')
#		else :
#			print('不含数字７') 
#	else:
#		print('请输入三位数')
#a=input('输入数字')
#a=int(a)
#a>0
#print(a)
#pass
#if a<0:
#	print(-a)
#a=int(float(input('输入公里:')))
#a=a+1
#a<=3
#print('13')
#if 15>=a>3:
#	a=(a-3)*2.3+13
#	print(a)
#a=input ('输入年份:')
#a=int(a)
#b=a%400
#if b==0:
#	print('闰年')
#elif a%100==0:
#	print('平年')
#elif a%4==0:
#	print('闰年')
#else:
#	print('平年')　

#x=input('输入数字')
#x=int(x)
#if x>=0:
#	print (x+(x<<2)) 
#elif x<0: 
#	x=(-x)
#	print(x+(x<<2))
#else:
#	pass

#x=input('输入数字')
#x=int(x)
#if x>=0:
#	print (x+(x<<2)) 
#else : 
#	x=(-x)
#	print(x+(x<<2))

a=input('输入正整数')
a=int(a)+3
if a>2:
	print(a*(' ')+'*')
	print((a-1) *" "+'***')
	print((a-2)*" "+'*****')
	print((a-3)*" "+('*******'))
#else :
#	pass

#a=input('输入账号')
#b=input('输入密码')
#if a=='seven'and b=='123':
#	print('登录成功')
#else:
#	print('你还有两次机会')		
#	a=input('输入账号')
#	b=input('输入密码')
#	if a=='seven'and b=='123':
#		print('登录成功')
#	else:
#		print('你还有一次机会')
#			
#		a=input('输入账号')
#		b=input('输入密码')
#		if a=='seven'and b=='123':
#			print('登陆成功')
#		else:
#			quit()

#i=1
#while i<10:
#	j=1
#	while j<10:
#		print('%s*%s=%s'%(i,j,i*j),end=" ")
#		j+=1
#	i+=1
#	print()

#s='hello'
#for ch in s:
#	print(ch)  



#s=(range (1,5))
#for i in s:
#	print((i*'***').center(5*i))
#	print()


#斐波那契数列
#０　 １　  １　    ２　          ３　                   ５      　
#
#a    b    a+b    a+b+b    (a+b)+(a+b)+b       (a+b+b)+ (a+b)+(a+b)+b  


#for a in range(0,10):
#	a+=1
#	print(a)


for x in range(0,20):
	print(x)



























