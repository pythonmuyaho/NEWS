from ex import*
Yahoo = news_head('https://finance.yahoo.com/news?guccounter=1', 'h3', 'Mb(5px)', '')
Naver = clean_n(news_head('https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=262','ul', 'type06_headline', 'a'))
CNN = news_head('https://edition.cnn.com/business/investing', 'div', 'column zn', '')
Kotra = clean_n(news_head('https://news.kotra.or.kr/user/globalBbs/kotranews/5/globalBbsDataList.do?setIdx=244', 'div', 'sub-page-content', 'dt'))
print(Yahoo)
print(Naver)
print(Kotra)
print(CNN)