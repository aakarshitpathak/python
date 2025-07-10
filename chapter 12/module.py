def myFunc():
    print("Hello world!")



if __name__ == "__main__":
    # if this code is excecuted by running the file its present in
    print("We are directly running this code")

    myFunc()
    print(__name__)
    # note: ye if __name__ wala code tabhi run hoga jab tum yaha se
    # run karwao agar import karoge toh nahi run hoga