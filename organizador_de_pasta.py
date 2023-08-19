import os, shutil

def organizador_de_arquivos(local):

    for arquivos in os.listdir(local):
        formato = arquivos.rsplit(".")
        local_do_arquivo = local + os.sep + arquivos
        try:
            

            formato_final = (formato[-1])
            if formato_final == (formato[-1]):
                    
                    if formato_final == "pdf" or formato_final == "txt" or formato_final == "epub" or formato_final == "docx" or formato_final == "xlsx":
                        if os.path.exists(local + os.sep +"Arquivos de texto"):
                            shutil.move(local_do_arquivo,local + os.sep +"Arquivos de texto")
                        else:
                            os.mkdir(local + os.sep + "Arquivos de texto")
                            shutil.move(local_do_arquivo,local + os.sep +"Arquivos de texto")
                    
                    if formato_final == "AVI" or formato_final == "WMV" or formato_final == "MOV" or formato_final == "MKV" or formato_final == "mp4" or formato_final == "FLV":
                        if os.path.exists(local + os.sep +"Arquivos de vídeo"):
                            shutil.move(local_do_arquivo,local + os.sep +"Arquivos de vídeo")
                        else:
                            os.mkdir(local + os.sep + "Arquivos de vídeo")
                            shutil.move(local_do_arquivo,local + os.sep +"Arquivos de vídeo")

                    if formato_final == "JPEG" or formato_final == "jpg" or formato_final == "png" or formato_final == "GIF" or formato_final == "BMP":
                        if os.path.exists(local + os.sep +"Arquivos de imagem"):
                            shutil.move(local_do_arquivo,local + os.sep +"Arquivos de imagem")
                        else:
                            os.mkdir(local + os.sep + "Arquivos de imagem")
                            shutil.move(local_do_arquivo,local + os.sep +"Arquivos de imagem")

                    if formato_final == "exe":
                        if os.path.exists(local + os.sep +"Arquivos executáveis"):
                            shutil.move(local_do_arquivo,local + os.sep +"Arquivos executáveis")
                        else:
                            os.mkdir(local + os.sep + "Arquivos executáveis")
                            shutil.move(local_do_arquivo,local + os.sep +"Arquivos executáveis")

                    if formato_final == "zip" or formato_final == "rar":
                        if os.path.exists(local + os.sep +"Arquivos compactados"):
                            shutil.move(local_do_arquivo,local + os.sep +"Arquivos compactados")
                        else:
                            os.mkdir(local + os.sep + "Arquivos compactados")
                            shutil.move(local_do_arquivo,local + os.sep +"Arquivos compactados")

                    else:
                        if  arquivos == "Arquivos executáveis" or arquivos == "Arquivos de texto" or arquivos == "Arquivos compactados" or arquivos == "Arquivos Gerais" or arquivos == "Arquivos de vídeo" or arquivos == "Arquivos de imagem":
                            pass
                        else:
                            if os.path.exists(local + os.sep +"Arquivos Gerais"):
                                shutil.move(local_do_arquivo,local + os.sep +"Arquivos Gerais")
                            else:
                                os.mkdir(local + os.sep + "Arquivos Gerais")
                                shutil.move(local_do_arquivo,local + os.sep +"Arquivos Gerais")

                                         
        except:
            try:
                if arquivos == "Arquivos executáveis" or arquivos == "Arquivos de texto" or arquivos == "Arquivos compactados" or arquivos == "Arquivos Gerais" or arquivos == "Arquivos de vídeo" or arquivos == "Arquivos de imagem":
                    pass
                else:
                    if os.path.exists(local + os.sep +"Arquivos Gerais"):
                        shutil.move(local_do_arquivo,local + os.sep +"Arquivos Gerais")
                    else:
                        os.mkdir(local + os.sep + "Arquivos Gerais")
                        shutil.move(local_do_arquivo,local + os.sep +"Arquivos Gerais")
            
            except:
                continue


organizador_de_arquivos(r'C:\Users\Herik\Downloads')