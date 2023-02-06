#primeiro -> upload
# https://docs.aws.amazon.com/pythonsdk/?id=docs_geteway
import boto3
from sagemaker.s3 import S3Uploader

session = boto3.Session()

#verificação de região
#session.region_name

#creando bucket e fazendo upload de aplicação
bucket = 'nome-do-bucket'
session.client('s3').create_bucket(Bucket = bucket,
                                  CreateBucketConfiguration={"LocationConstraint": session.region_name})

#subpasta dentro do bucket
subpasta = "arquivos"
#caminho dos arquivos para upload
#padrão de envio é "s3://{nome do bucket}/{nome da pasta}"
caminho = "s3://{}/{}".format(bucket, subpasta)
#print(caminho)

#identificando o arquivo
s3_upload = S3Uploader.upload("nome do arquivo com extensão.exe", caminho)
print(s3_upload)

#Segundo -> download
bucket = "nome-do-bucket"
s3 = boto3.resource("s3")

#parâmetro de local/nome do arquivo e novo nome do arquivo
s3.Bucket(bucket).download_file("arquivos/digit.png", "digit_download.png")