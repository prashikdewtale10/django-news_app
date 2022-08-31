from django.shortcuts import render
import requests

# Create your views here.
def Index(request):
	r=requests.get('http://api.mediastack.com/v1/news?access_key=e776d866c25d1a769a3f4187ad5751e7&categories=health,-sports')
	res=r.json()
	data=res['data']
	title=[]
	description=[]
	image=[]
	url=[]
	# print()
	for i in data:
		title.append(i['title'])
		description.append(i['description'])
		image.append(i['image'])
		url.append(i['url'])
	# print(url)
	news = zip(title,description,image,url) #zip[(t1,d1,i1,u1),(t2,d2,i2,u2)]
	return render(request,'index.html',{'news':news})

def Sports(request):
	r=requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=b96e6a4afdb046e7850e2db9de5282f1')
	res=r.json()
	data=res['articles']
	title=[]
	description=[]
	image=[]
	url=[]
	for i in data:
		title.append(i['title'])
		description.append(i['description'])
		image.append(i['urlToImage'])
		url.append(i['url'])
	# print(url)
	news = zip(title,description,image,url) #zip[(t1,d1,i1,u1),(t2,d2,i2,u2)]
	return render(request,'newsapi.html',{'news':news})

def Bitocoin(request):
	# r=requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=b96e6a4afdb046e7850e2db9de5282f1')
	r=requests.get('https://newsapi.org/v2/everything?q=bitcoin&apiKey=b96e6a4afdb046e7850e2db9de5282f1')
	res=r.json()
	data=res['articles']
	title=[]
	description=[]
	image=[]
	url=[]
	# print()
	for i in data:
		title.append(i['title'])
		description.append(i['description'])
		image.append(i['urlToImage'])
		url.append(i['url'])
	# print(url)
	news = zip(title,description,image,url) #zip[(t1,d1,i1,u1),(t2,d2,i2,u2)]
	return render(request,'newsapi.html',{'news':news})

def Business(request):
	# r=requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=b96e6a4afdb046e7850e2db9de5282f1')
	r=requests.get('https://newsapi.org/v2/top-headlines/sources?category=business&apiKey=b96e6a4afdb046e7850e2db9de5282f1')
	res=r.json()
	data=res['articles']
	title=[]
	description=[]
	image=[]
	url=[]
	# print()
	for i in data:
		title.append(i['title'])
		description.append(i['description'])
		image.append(i['urlToImage'])
		url.append(i['url'])
	# print(url)
	news = zip(title,description,image,url) #zip[(t1,d1,i1,u1),(t2,d2,i2,u2)]
	return render(request,'newsapi.html',{'news':news})






