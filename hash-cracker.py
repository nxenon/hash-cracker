#!/usr/bin/env python3

'''
Hash Cracker Working with WordList
'''

from packages.HashGenerator.HashGenerator import HashTool
word_list = ""
error_code = None
while True:
    error_code = 1
    all_options = ["1","2","3","4","5","6","7","8","9","10","11","md5","sha256","sha512","sha3_256","sha3_384","sha3_224","sha3_512","sha1","sha384","sha224","test all"]
    print("\n Options :")
    print("\t1)MD5")
    print("\t2)sha256")
    print("\t3)sha512")
    print("\t4)sha3_256")
    print("\t5)sha3_384")
    print("\t6)sha3_224")
    print("\t7)sha3_512")
    print("\t8)sha1")
    print("\t9)sha384")
    print("\t10)sha224")
    print("\t11)test all")
    print("")

    hash_type = input("Hash type number :").lower()
    hash_text = input("Your hash :")
    print()

    if hash_type not in all_options :
        print("Invalid option")
        again = input("again ? (y) :").lower()
        if again == "y" or again == "yes":
            continue
        else:
            break

    with open("word-list.txt" , "r") as texts :
        word_list_processing = texts.read()
        word_list = word_list_processing.split("\n")
        print("Number of words in (word-list.txt) file : " + str(len(word_list)))
        print("")

    if hash_type != "11" or hash_type != "test all" :

        for word in word_list :
            generated_hash = ""
            hash_connection = HashTool(word)

            if hash_type == "md5" or hash_type == "1":
                generated_hash = hash_connection.md5_encrypt()

            elif hash_type == "sha256" or hash_type == "2":
                generated_hash = hash_connection.sha256_encrypt()

            elif hash_type == "sha512" or hash_type == "3":
                generated_hash = hash_connection.sha512_encrypt()

            elif hash_type == "sha3_256" or hash_type == "4":
                generated_hash = hash_connection.sha3_256_encrypt()

            elif hash_type == "sha3_384" or hash_type == "5":
                generated_hash = hash_connection.sha3_384_encrypt()

            elif hash_type == "sha3_224" or hash_type == "6":
                generated_hash = hash_connection.sha3_224_encrypt()

            elif hash_type == "sha3_512" or hash_type == "7":
                generated_hash = hash_connection.sha3_512_encrypt()

            elif hash_type == "sha1" or hash_type == "8":
                generated_hash = hash_connection.sha1_encrypt()

            elif hash_type == "sha384" or hash_type == "9":
                generated_hash = hash_connection.sha384_encrypt()

            elif hash_type == "sha224" or hash_type == "10":
                generated_hash = hash_connection.sha224_encrypt()

            if generated_hash == hash_text :
                print("Hash cracked :)")
                print("+--------------------------------------------------------------+")
                print("Hash :" + hash_text)
                print("")
                print("string :" + word)
                print("+--------------------------------------------------------------+")
                error_code = 0
                input("Press enter to continue ..")
                break

    if (hash_type == "11") or (hash_type == "test all") :
        for word in word_list :
            hash_connection = HashTool(word)
            alg_list = [hash_connection.md5_encrypt(),hash_connection.sha256_encrypt(),hash_connection.sha512_encrypt(),hash_connection.sha3_256_encrypt(),hash_connection.sha3_384_encrypt(),hash_connection.sha3_224_encrypt(),hash_connection.sha3_512_encrypt(),hash_connection.sha1_encrypt(),hash_connection.sha3_384_encrypt(),hash_connection.sha224_encrypt()]
            for all in alg_list :
                generated_hash = all
                if generated_hash == hash_text :
                    print("Hash cracked :)")
                    print("+--------------------------------------------------------------+")
                    print("Hash :" + hash_text)
                    print("")
                    print("string :" + word)
                    print("+--------------------------------------------------------------+")
                    error_code = 0
                    input("Press enter to continue ..")
                    break

    if error_code == 1 :
        print("Nothing found in word-list that is equal to the hash :(")
        input("Press enter to continue ..")

input()