class Notebook:
    def __init__(self,title,username,likes) -> None:
        self.title,self.username,self.likes=title,username,likes
    
    def __repr__(self) -> str:
        return 'Notebook <"{}/{}", {} likes>'.format(self.username,self.title,self.likes)
    
nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5,nb6, nb7, nb8, nb9]

def compare_likes(nb1,nb2):
    if nb1.likes>nb2.likes:
        return 'lesser'
    elif nb1.likes==nb2.likes:
        return 'equal'
    elif nb1.likes<nb2.likes:
        return 'greater'