nbessai=int(0)
X = bool(true)
mp1=str("")
while nbessai<3 :
    print=("donner le login")
    input=(login)
    print=("donner le mot de passe")
    input=(mp)
    i=int(-1)
    for i in range (i+1,len(login)+1) :
          if login[i] not in ["a","o","u","e","i","y"]:
          mp1=mp1+login[i+1]
        mp1=mp1+str(len(login))
     i=int(-1)
     Y=bool(true)
     for i in range (i+1,len(login)+1):
           if login[i+1] in ["a","o","u","e","i","y"] and Y= true :
               mp1+=login[i]
               Y=false
                
        if mp!=mp1:
           print("utilisateur non autorisé")
            nbessai+=1
        else:mp=mp1
            print("utilisateur autorisé")
            test=bool(true)
            while test :
                pw1=input("saisir votre nv mdp")
                pw2=input("saisir votre nv mdp")
                if pw1=pw2:
                    print("mdp changé avec succ")
                else pw1!=pw2 :
                    test=false
                     print("essayer de nv")
            
            
