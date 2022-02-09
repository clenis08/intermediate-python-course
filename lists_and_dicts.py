def main():
    my_list = [1, "hello", True, 4.5]
    my_dict = { "firstname":"Natalia",
                "secondname": "Lenis"
    }

    super_list=[
                {"firstname":"Natalia","secondname": "Lenis"},
                {"firstname":"Ana","secondname": "Castillo"},
                {"firstname":"Juan","secondname": "Zapata"},
                {"firstname":"Rafael","secondname": "Castillo"},
                {"firstname":"Luis","secondname": "Lenis"}
                ]
    super_dict = {
                "natural_nums":[1,2,3,4],
                "integer_nums":[-1,-2,0,5,8],
                "floating_nums":[1.2,1.6,9.8,7.3]
    }

    for dicc in super_list :
        print(dicc.items(),">" ,dicc["firstname"], "-", dicc["secondname"])
    # for dicc in super_list :
    #     for key,value in dicc.items():
    #         print(key, "-", value)

    for key,value in super_dict.items():
        print(key, "-", value)



if __name__ == '__main__': ## Punto de entrada
    main()