graph = {'a':{'e':6,'d':8},
         'b':{'c':4,'d':3},
         'c':{'b':4,'d':4,'e':2},
         'd':{'b':3,'c':4},
         'e':{'c':2,'a':6}}

#graph =  {'s':{'a':7,'b':2,'c':3},
#          'a':{'b':3,'d':4,'s':7},
#          'b':{'h':1,'d':4,'s':2},
#          'd':{'f':5,'b':4,'a':4},
#          'h':{'f':3,'g':2,'b':1},
#          'f':{'h':3,'d':5},
#          'c':{'s':3,'l':2},
#          'g':{'h':2,'e':2},
#          'e':{'g':2,'k':5},
#          'k':{'e':5,'i':4,'j':4},
#          'i':{'k':4,'j':6,'l':4},
#          'j':{'l':4,'i':6,'k':4},
#          'l':{'c':2,'i':4,'j':4}}
 
def dijkstra(graph,mulai,tujuan):
    jalur_cepat = {}
    penghubung = {}
    titik_tdk_terlihat = graph
    infinity = 9999999
    jalur = []
    for titik in titik_tdk_terlihat:
        jalur_cepat[titik] = infinity
    jalur_cepat[mulai] = 0
 
    while titik_tdk_terlihat:
        minTitik = None
        for titik in titik_tdk_terlihat:
            if minTitik is None:
                minTitik = titik
            elif jalur_cepat[titik] < jalur_cepat[minTitik]:
                minTitik = titik
 
        for titikAnak, bobot in graph[minTitik].items():
            if bobot + jalur_cepat[minTitik] < jalur_cepat[titikAnak]:
                jalur_cepat[titikAnak] = bobot + jalur_cepat[minTitik]
                penghubung[titikAnak] = minTitik
        titik_tdk_terlihat.pop(minTitik)
 
    titikSebelumnya = tujuan
    while titikSebelumnya != mulai:
        try:
            jalur.insert(0,titikSebelumnya)
            titikSebelumnya = penghubung[titikSebelumnya]
        except KeyError:
            print('Jalur tidak ditemukan')
            break
    jalur.insert(0,mulai)
    if jalur_cepat[tujuan] != infinity:
        print('Jarak jalur = ' + str(jalur_cepat[tujuan]) + "KM")
        print('Jalur yang dituju ' + str(jalur))
 
start = raw_input("Masukan start = ")
finish = raw_input("Masukan Tujuan = ")

dijkstra(graph, start, finish)
