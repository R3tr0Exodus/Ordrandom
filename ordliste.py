import re
import csv

# Her indsættes stien til den mappe vi arbejder i
the_path = "/Users/kasper/Library/Mobile Documents/com~apple~CloudDocs/_Dokumenter/Odder Højskole/VisualStudioCode/python/"
# the_path = "/Users/kr/Library/Mobile Documents/com~apple~CloudDocs/_Dokumenter/Odder Højskole/VisualStudioCode/python/"

# Skriv filnavn ↓ på den fil der skal bruges (simpel html-fil med <p> og <strong>)
the_textfile = "loremipsum.txt"

# Skriv ønsket filnavn ↓ på den tabel-fil, som skal genereres
generated_csvfile = "loremipsum.csv"

# Her åbnes text-filen
txtfile_imported = open(the_path + the_textfile, "rt")

# Her dannes en liste med de ord i textfilen, som er fremhævet med fed ( html ≈ <strong> )
newfile = txtfile_imported.read()               # Her læses indholdet af filen ind i "newfile"
pattern = "<strong>(.*?)</strong>"              # Her defineres mønsteret
ord_liste = re.findall(pattern, newfile)        # Her dannes listen og gemmes som "ord_list"

print("\nDer er " + str(len(ord_liste)) + " ord i alt.\n")
# print(ord_liste)

# Her dannes filen "generated_csvfile.csv"
ordliste_fil = open(the_path + generated_csvfile, "w")
ordliste_fil.write("")
ordliste_fil.close()

# Her skrives ordene ind i csv-filen - opdelt med 6 ord i hvert sæt
set_counter = 1
word_counter = 0
for i in ord_liste:
    ordliste_fil = open(the_path + generated_csvfile, "a")
    if word_counter % 6 == 0 :
        ordliste_fil.write("-------- set " + str(set_counter) + " ---\n")
        set_counter += 1
    ordliste_fil.write(i+"\n")
    word_counter += 1
    ordliste_fil.close()
