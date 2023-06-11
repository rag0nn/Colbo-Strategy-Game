class log_tut():
    def __init__(self):
        pass
    
    def log_ekle(self,text):
        with open("log.txt",mode="a") as f:
            f.write(f"{text}\n")
        f.close()
    
    def log_temizle(self):
        with open("log.txt",mode="w") as f:
            pass
        f.close()        
    
    def log_oku(self):
       
        try:
            with open("log.txt",mode="r") as f:
                q = f.readlines()[-7:]
    
            text = f"--- {q[0]} \t {q[1]}\t  {q[2]} \t {q[3]} \t {q[4]} \t {q[5]} \t {q[6]} ---"
            return text
        except:
            pass




