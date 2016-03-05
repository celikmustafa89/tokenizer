# Tokenizer
Verilen bir text dokümanının, tüm tokenlarının, word tokenlarının ve punctuation tokenlarının sayımı gerçekleştirilir.
Bu sayım toplam tokenlar ve unique(distinct) olarak ayrı ayrı yapılır. 
Elde edilen tokenlar:
all_tokens.txt  --> tüm tokenların bulunduğu dosya,
word_tokens.txt --> sadece kelimelerin bulunduğu dosya,
punc_tokens.txt --> sadece noktalama işaretlerinin bulunduğu dosya, 

olarak 3 farklı şekilde dosyaya yazdırılır.

Token sayıları da her kategori için ayrı ayrı console çıktısı olarak gösterilir.

Not: noktalama çıktıları, işlemin hızlı yapılabilmesi için sadece unique tokenları göstermektedir.
