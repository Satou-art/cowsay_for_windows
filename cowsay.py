from time import sleep
#TODO : this gonna show a cow that say something


def main():
    def cowsay(som):   
        s = " " + (len(som) + 2) * "_" + " \n" + "(" + (len(som) + 2) * " " + ")\n" + "( " + som + " )\n" + "(" + (len(som) + 2) * " " + ")\n" + " " + (len(som) + 2) * "-"
        cow = f"""{len(som)*" "}\\   ^__^
{len(som)*" "}  \\  (oo)\________
{len(som)*" "}     (__)\        )\\/\\
{len(som)*" "}         ||-----w |
{len(som)*" "}         ||      ||\n"""
        print(s, "\n",  cow)
    cowsay(input())
    sleep(2.5)


if __name__ == '__main__':
    main()
    exit()
