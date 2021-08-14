st = input()
st += ' запретил букву'

letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з',
         'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 
         'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 
         'ъ', 'ы', 'ь', 
         'э', 'ю', 'я']

for i in range(len(letters)):
    if letters[i] not in st:
        continue
    else:
        if st[0] == ' ':
            st = st.replace(' ', '', 1)
        st = st.replace('  ', ' ', 3).strip()
        print(st, letters[i])
        st = st.replace(letters[i], '')