from time import sleep
#TODO : this gonna show a cow that say something


def main():
    def cowsay(som):   
        s = f"""
 ______________
(              )
(     {som}    )
(              )
 --------------
        """
        print(s)
    cowsay(input())
    sleep(2.5)


if __name__ == '__main__':
    main()
    exit()
