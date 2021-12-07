# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


# Sempre que um item é recebido, ele decide uma das seguintes ações -

# Continue processando o item.
# Solte-o do pipeline.
# Pare de processar o item.
# Os pipelines de itens são geralmente usados ​​para os seguintes fins -

# Armazenando itens raspados no banco de dados.
# Se o item recebido for repetido, ele descartará o item repetido.
# Ele irá verificar se o item está com campos direcionados.
# Limpando dados HTML.


from itemadapter import ItemAdapter


class QuotetutorialPipeline:
    def process_item(self, item, spider):
        print('Pipeline: ' + item['title'][0])
        return item
