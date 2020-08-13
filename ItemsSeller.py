import sys
import requests
import prettytable

# api-endpoint
UrlBase =  "https://api.mercadolibre.com"
UrlItemsSeller = UrlBase + "/sites/MLA/search"
UrlCategories = UrlBase + "/categories/"
  
#Preguntar si es usuario simple o texto
sellersIdListad = ['179571326']

def get_CategoryName_Result(category_id):
    # Obtencion de categoria por id
    responseCategories = requests.get(url = UrlCategories + category_id)
    if responseCategories.status_code == 200:
        datajson = responseCategories.json()
        category_name = datajson['name'] 
        responseCategories.close()
        return category_name
    else:
        responseCategories.raise_for_status()

def get_ItemSeller_Result(sellerId):
    # Obtencion de items por vendedor
    responseItemsSeller = requests.get(url = UrlItemsSeller, params={'seller_id':sellerId}) 

    if responseItemsSeller.status_code == 200:
        datajson = responseItemsSeller.json()
        datajsonResults = datajson['results']
        resultTable = prettytable.PrettyTable(["Id", "Title", "Category_Id", "Category_Name"])
        for datajsonResult in datajsonResults:
            category_id = datajsonResult['category_id'] 
            resultRow = []
            resultRow.append(datajsonResult['id'])
            resultRow.append(datajsonResult['title'])
            resultRow.append(datajsonResult['category_id'])
            resultRow.append(get_CategoryName_Result(category_id))
            resultTable.add_row(resultRow)
        responseItemsSeller.close()
        return resultTable.get_string() 
    else:
        responseItemsSeller.raise_for_status()

def log_items(sellerId):
        try:
            outputFileName = sellerId + "_log" + ".txt"
            print("Generando... " + outputFileName)                                
            result = get_ItemSeller_Result(sellerId)
            outputFile = open(outputFileName,"w")
            outputFile.write(result)
            outputFile.close()
        except requests.exceptions.HTTPError as httpError:
            print(httpError)
        except IOError as IOerr:
            print("Error al generar archivo" +  IOerr)
        except Exception as ex:
            print("Ha ocurrido un error: " + ex)
        finally:
            print("COMPLETADO")

def main():
    sellersIdList = list(input("Ingrese Id de vendedores: ").split()) 
    for sellerId in sellersIdList:
        log_items(sellerId)

main()

