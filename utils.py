import settings as s

def unicode_converter():
    # ingresar en 'fileIn.txt' el texto ue quieren convertir. 
    try:
        in_file = open('./files/fileIn.txt', encoding="utf8").read() # ruta archivo de entrada
        out_file = open('./files/fileOut.txt', 'w') # ruta archivo de salida

        # for i in s.UNICODE_DICT.keys():
        #   in_file = in_file.replace(i, s.UNICODE_DICT[i])
        # txt_modified: str = in_file.encode('utf8').__str__()
        # out_file.write(txt_modified)
        
        for i in s.CHAR_DICT:
            in_file = in_file.replace(i, (r'\u{:04X}'.format(ord(i))))
        out_file.write(in_file)
        out_file.close()
        print("¡Cambio realizado!")
    except ValueError:
        print("No se pudo convertir unicode.")  
    except OSError as err:
        print("OS error: {0}".format(err))
    except BaseException as error:
        print(f"Inesperado {error=}, {type(error)=}")
        raise