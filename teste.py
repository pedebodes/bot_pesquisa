
from scrapy import addDominiosIgnorados,cadastraPesquisa,getDadosPesquisa,getDadosPesquisa,coletaDadosUrl,getDadosResultadoFalha,retornaPesquisas,retornaDadosResultado,retornaResultadosPesquisa

url = ['https://www.olx.com.br/','https://www.olx.pt','https://www2.camara.leg.br','https://www.zapimoveis.com.br','https://www.tokstok.com.br','https://www.istoedinheiro.com.br','https://www.istoe.com.br','https://www.aluguelemflorianopolis.com.br','https://estadodeminas.lugarcerto.com.br','https://esportes.yahoo.com','https://br.pinterest.com','https://books.google.com.br','https://blumenau.sc.gov.br','https://biblioteca.incaper.es.gov.br','http://www.ceagesp.gov.br','http://www.camarapoa.rs.gov.br','https://www.torcedores.com','https://www.scielo.br','https://www.jornaldenovaodessa.com.br','https://www.espn.com.br','https://www.elo7.com.br','https://www.angra.rj.gov.br','https://piaui.folha.uol.com.br','https://m.futebolinterior.com.br','https://leismunicipais.com.br','https://itu.sp.gov.br','https://cabofrio.rj.gov.br','http://www.iema.ma.gov.br','https://www.ceara.gov.br','https://enit.trabalho.gov.br','https://www.curitiba.pr.gov.br','https://www.gov.br','http://www.adapar.pr.gov.br','http://www.mt.gov.br','http://rigeo.cprm.gov.br','http://www.palmeira.pr.gov.br','https://palmeiradosindios.al.gov.br','https://palmeirasdegoias.go.gov.br','https://turismo.riodoscedros.sc.gov.br','https://www.campos.rj.gov.br','https://www.palmeira.sc.gov.br','https://www.inpa.gov.br','http://repositorio.unis.edu.br','https://nupet.daelt.ct.utfpr.edu.br','https://bibliodigital.unijui.edu.br:8443','http://www.ufal.edu.br','https://sites.unipampa.edu.br','https://www.casasbahia.com.br/','https://www.carrefour.com.br','https://www.alibaba.com/','https://pt.aliexpress.com/','https://www.mercadolivre.com.br/','https://www.uai.com.br/','https://www.globo.com/','https://g1.globo.com/','https://www.terra.com.br/','https://www.uol.com.br/','https://www.facebook.com/','https://instagram.com/','https://twitter.com/','https://www.jusbrasil.com.br/','https://pt.wikipedia.org/','https://www.netshoes.com.br/','https://www.timken.com/','https://esportes.mercadolivre.com.br/','https://lista.mercadolivre.com.br/','https://portuguese.alibaba.com/','https://m.portuguese.alibaba.com','https://www.autopecas-online.pt','https://www.autopecasonline24.pt/','https://www.pecasauto24.pt','https://parts.cat.com','https://www.amazon.com.br/','https://www.americanas.com.br/','https://www.multasbr.com.br/','https://www.reposicaoonline.com.br','https://foegerbicicletas.com.br','https://www.magazineluiza.com.br/','https://pt.ebay.com/','http://cnpj.info','https://www.shoptime.com.br/','https://m.kabum.com.br','https://sead.amapa.gov.br/','https://www.autopecas24.pt/','https://m.topautopecas.pt','https://shop.bpwtrapaco.com/','https://br.linkedin.com/','https://support.google.com','https://www.google.com/','https://maps.google.com','https://policies.google.com','https://produto.mercadolivre.com.br','https://webcache.googleusercontent.com','http://webcache.googleusercontent.com','https://www.youtube.com','https://br.banggood.com','https://nupet.daelt.ctpr.edu.br','https://scholar.google.com','https://www.br.com.br','https://www.buscanarede.com.br','https://www.olx.com.br','https://1000marcassafetybrasil.com.br']




# addDominiosIgnorados(url)# cadastra urls
# item_pesquisa = cadastraPesquisa("abrasivos",1) #retorna id da pesquisa
# getDadosPesquisa(item_pesquisa) # processa as urls da pequisa informada com status pendente de processamento
# getDadosPesquisa(3) # coleta dados a partir de id_pesquisa
# coletaDadosUrl((185))  #Coleta dados informando um id e uma url da tabela resultados
# getDadosResultadoFalha(3) # processar Urls que deram falha a partir de id_pesquisa
# print(retornaPesquisas()) # retorna as pesquisa ja efetuadas
print(retornaResultadosPesquisa(10)) # retorna resultados de uma pesquisa
# print(retornaDadosResultado(1)) #retorna dados do resultado

