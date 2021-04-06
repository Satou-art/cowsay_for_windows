from time import sleep
import sys
#TODO : this gonna show a cow that say something





args = sys.argv
args.remove(sys.argv[0])
if len(args) < 1 :
    print("Usage: \n\tcowsay.py [the words you want the cow say]")
    exit()
else:
    string = " ".join(args)






def main():
    def cowsay(som):   
        s = " " + (len(som) + 2) * "_" + " \n" + "(" + (len(som) + 2) * " " + ")\n" + "( " + som + " )\n" + "(" + (len(som) + 2) * " " + ")\n" + " " + (len(som) + 2) * "-"
        cow = f"""{len(som)*" "}\\   ^__^
{len(som)*" "}  \\  (oo)\________
{len(som)*" "}     (__)\        )\\/\\
{len(som)*" "}         ||-----w |
{len(som)*" "}         ||      ||\n"""
        print(s, "\n",  cow)
    cowsay(string)
    sleep(2.5)


if __name__ == '__main__':
    main()
    exit()
