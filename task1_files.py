#!env/bin/python3



def main():
    with open('referat.txt', 'r', encoding='utf-8') as myfile:
        content = myfile.read()
        print(f'Длинна строки {len(content)}')
        wcount = len(content.split())
        print(f'Количество слов {wcount}')
        newcontent = content.replace('.','!')

    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(newcontent)

if __name__ == "__main__":
    main()
