import random
import hashlib as hl
import time as t

def banner_hash():
    hash_no = random.randrange(0,2)
    if hash_no == 0:
        print('Password hasher by Vyshnav')

    elif hash_no == 1:
        print('Password hasher by Vyshnav')

if __name__ == '__main__':
    banner_hash()

def process():
    print('Processing .......')


def box_1():
    print('''                                                                          
▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀  
    ''')


if __name__ == '__main__':
    process()
    box_1()

banner_hash()

list_of_hashes = ['Md5','Sha1', 'Sha224', 'Sha256', 'sha384', 'sha512' ]
def value(inp):
    inp = inp

    def options():
        print('''
                                  [+] Choose a Hashing option for Encryption :
                                             __________
                                                |
                                    1) Md5      |   2) SHA1
                                                |
                                    3) SHA224   |   4) SHA256
                                                |
                                    5) SHA384   |   6) SHA512
                                                |
                                           _____|______
                ''')

        option = input(" : ")
        list_of_hashes = len(option)
        if list_of_hashes == 0:
            print("[-] Umm! I think you forgot to enter the option")
            return options()
        elif option == "1":
            process()
            md5_hash = hl.md5(inp.encode()).hexdigest()
            t.sleep(0.4)
            return "md5 of {} = {}".format(inp, md5_hash)
        elif option == "2":
            process()
            print()
            sha1_hash = hl.sha1(inp.encode()).hexdigest()
            t.sleep(0.4)
            return "sha1 of {} = {}".format(inp, sha1_hash)
        elif option == "3":
            process()
            print()
            sha224_hash = hl.sha224(inp.encode()).hexdigest()
            t.sleep(0.5)
            return "sha224 of {} = {}".format(inp, sha224_hash)
        elif option == "4":
            process()
            print()
            sha256_hash = hl.sha256(inp.encode()).hexdigest()
            t.sleep(0.5)
            return "sha256 of {} = {}".format(inp, sha256_hash)
        elif option == "5":
            process()
            print()
            sha384_hash = hl.sha384(inp.encode()).hexdigest()
            t.sleep(0.6)
            return "sha384 of {} = {}".format(inp, sha384_hash)
        elif option == "6":
            process()
            print()
            sha512_hash = hl.sha512(inp.encode()).hexdigest()
            t.sleep(0.7)
            return "sha512 of {} = {}".format(inp, sha512_hash)
        else:
            print("[-] You chose a wrong value")
            return options()

    if __name__ == '__main__':
        box_1()
        print(options())
        box_1()


def main():
    print("[+]  Enter the value for Encryption - \n")
    inp = input(" : ")
    len_inp = len(inp)
    if len_inp == 0:
        print("[-] Umm! I think you forgot to enter the value\n")
        return main()
    else:
        value(inp)
    return again()


def again():
    again = input("Hash again? y(yes) n(no) : ")
    if len(again) == 0:
        print("Ops! You didn't chose any option! Choose y or n : \n")
        return again()
    elif again == "yes" or again == "y" or again == "Y":
        print("Ok then. \n")
        return main()
    elif again == "no" or again == "N" or again == "n":
        print("Thanks to use VYHash..")
        return None
    else:
        print("[-] You did something wrong. Do it right :p \n")
        return again()


if __name__ == '__main__':
    main()