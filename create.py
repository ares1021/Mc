import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [
{
  "品名":"樂事起司口味樂事洋芋片",
  "口味":"起司口味",
  "介紹":"樂事只選用當令新鮮馬鈴薯，鮮切成金黃香脆洋芋片；以剛剛好的調味與天然薯香搭成完美絕配。最好吃的樂事洋芋片，隨時享受簡單的快樂！樂事金黃香脆的洋芋片，搭配瑞士香濃起司調味，一吃就停不下來!",
},
{
  "品名":"樂事九州岩燒海苔洋芋片",
  "口味":"海苔口味",
  "介紹":"樂事只選用當令新鮮馬鈴薯，鮮切成金黃香脆洋芋片；以剛剛好的調味與天然薯香搭成完美絕配。最好吃的樂事洋芋片，隨時享受簡單的快樂！樂事金黃香脆的洋芋片，搭配九州岩燒海苔，一吃就停不下來!",
},
{
  "品名":"樂事經典原味洋芋片",
  "口味":"原味口味",
  "介紹":"以精選新鮮天然的馬鈴薯、黃金比例切片製成佐以薄鹽調味，金黃香酥的天然原味享受片片的歡樂美味",
},
{  
  "品名":"樂事波樂香烤肋排洋芋片",
  "口味":"香烤肋排",
  "介紹":"厚切馬鈴薯餅片配上炭火香烤的美味肋排，一入口就能享受天然薯香及濃郁美味的香脆爽勁，享受香脆爽勁的極致美味。",
},
{  
  "品名":"樂事大波浪椒香嫩雞",
  "口味":"椒香嫩雞",
  "介紹":"樂事大波浪洋芋片，爆脆口感搭配椒香嫩雞味，震撼的味蕾衝擊，越吃越帶勁!",
},
{  
  "品名":"樂事原切地瓜片洋芋片",
  "口味":"原切地瓜片",
  "介紹":"樂事精選台灣本產台農57號地瓜, 整顆原切鮮炸完美原切比例 入口更薄脆  自然釋發更濃郁地瓜香!不添加味精、人工防腐劑、人工色素與人工甜味劑 融合清爽糖粉與鹽的經典調味  吃出更自然香甜的美味",
},
{  
  "品名":"樂事自然滋味海鹽洋芋片",
  "口味":"自然滋味海鹽",
  "介紹":"選用當令新鮮馬鈴薯，鮮切成金黃香脆洋芋片。簡單海鹽調味，與天然薯香搭成完美絕配。最好吃的Simply Good 自然滋味，隨時享受簡單自然的快樂！",
},
{  
  "品名":"樂事韓式辣醬炸雞口味洋芋片",
  "口味":"韓式辣醬炸雞",
  "介紹":"一口咬下，韓式甜辣醬開始在舌尖蔓延。緊接著，炸雞的濃厚香味撲鼻而來，尾韻留下甜辣醬與濃厚肉味鹹甜交錯的多層次口感，每一口都是味蕾的絕大滿足。",
},
{  
  "品名":"樂事自然滋味海鹽洋芋片",
  "口味":"自然滋味海鹽",
  "介紹":"選用當令新鮮馬鈴薯，鮮切成金黃香脆洋芋片。簡單海鹽調味，與天然薯香搭成完美絕配。最好吃的Simply Good 自然滋味，隨時享受簡單自然的快樂！",
},
{  
  "品名":"樂事神戶厚切牛排洋芋片",
  "口味":"厚切牛排",
  "介紹":"神戶厚切牛排口味新上市入口後四溢的炙烤牛油花香，慢慢在口中擴散細嚼後，可以感受到濃厚的鮮甜肉味鎖住牛排肉汁的洋芋片融合濃郁薯香，口感層次豐富如現烤般微鹹的香甜口感，一片接一片也不膩口令人難忘的神戶牛排絕品美味，宅在家追劇也能輕鬆享受！",
},
{  
  "品名":"樂事青檸口味洋芋片",
  "口味":"青檸",
  "介紹":"神戶厚切牛排口味新上市入口後四溢的炙烤牛油花香，慢慢在口中擴散細嚼後，可以感受到濃厚的鮮甜肉味鎖住牛排肉汁的洋芋片融合濃郁薯香，口感層次豐富如現烤般微鹹的香甜口感，一片接一片也不膩口令人難忘的神戶牛排絕品美味，宅在家追劇也能輕鬆享受！",
},
{  
  "品名":"樂事四重風味鹽口味洋芋片",
  "口味":"四重風味鹽",
  "介紹":"搭配自岩鹽、海鹽、湖鹽及玫瑰鹽四重風味交織於口中絕妙的層次感讓人沉浸其中",
},
{  
  "品名":"樂事烘焙波浪普羅旺斯風味鹽洋芋片",
  "口味":"普羅旺斯風味鹽",
  "介紹":"非油炸餅片，脂肪減少30%加上風味鹽點綴吃起來更有層次!",
},
{  
  "品名":"樂事北海道奶香焗烤口味洋芋片",
  "口味":"奶香焗烤",
  "介紹":"來自盛產鮮奶的北海道，黃金微焦的焗烤散發濃濃香氣，再結合片片薯香，豐富濃郁的口感讓人無法抵擋",
},
{  
  "品名":"樂事烘焙波浪普羅旺斯風味鹽洋芋片",
  "口味":"普羅旺斯風味鹽",
  "介紹":"非油炸餅片，脂肪減少30%加上風味鹽點綴吃起來更有層次!",
},
{ 
  "品名":"樂事蒜爆椒鹽蝦口味洋芋片",
  "口味":"蒜爆椒鹽蝦",
  "介紹":"紓壓時刻，就想鬆一下! 下酒絕配，蒜爆椒鹽蝦口味登場!開袋引爆濃郁蒜香，最對台灣人的味蕾! 金黃脆口的大波浪餅片，再融合鹹香帶勁的椒鹽蝦，重口味滿足感瞬間爆表，讓人越吃越涮嘴，越咬越紓壓!",
},
]

collection_ref = db.collection("樂事餅乾")
for doc in docs:
  collection_ref.add(doc)

