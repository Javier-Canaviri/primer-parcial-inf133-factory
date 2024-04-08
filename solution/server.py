from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import parse_qs, urlparse  

orders={}
class Order:
    def __init__(self,id,client,status,payment,order_type):
        self.id=id
        self.client=client
        self.status=status
        self.payment=payment
        self.order_type=order_type

class Fisico(Order):
    def __init__(self,id,client,status,payment,shipping,products,order_type):
        super.__init__(self,id,client,status,payment,order_type)
        self.shipping=shipping
        self.products=products

class Digital(Order):
    def __init__(self,id,client,status,payment,code,expiration,order_type):
        super.__init__(self,id,client,status,payment,order_type)
        self.code=code
        self.expiration =expiration
class OrdersFactory:
    @staticmethod
    def crear_orden(id,client,status,payment,order_type,code,expiration,shipping,products):
        if order_type=="Fisico":
            return Fisico(id,client,status,payment,order_type,code,expiration,shipping,products)
        elif order_type=="Digital":
            return Digital(id,client,status,payment,order_type,code,expiration,code,expiration)
        else:
            return "tipo no valida"

class OrdersServices:
    def __init__(self):
        self.fabrica = OrdersFactory()
    @staticmethod
    def crear_orden(self,data):
        orden_id = len(orders)+1
        orden_client = data.get("client",None)
        orden_status = data.get("status",None) 
        orden_payment = data.get("payment",None)
        orden_tipo = data.get("tipo",None)
        orden_shippnig = data.get("shipping",None)
        orden_products = data.get("products",None)
        orden_code = data.get("code",None)
        orden_expiration = data.get("expiration",None)
        
        order = self.fabrica.crear_orden(orden_id,orden_client,orden_status,orden_payment,orden_tipo,orden_code,orden_expiration,orden_shippnig,orden_products)
        orders[orden_id] = order
        return order
    
    def buscar_por_id(self,id):
        pedido =next((pedido for pedido in pedidos if pedido.id==id),None)
        return pedido

    def buscar_por_estado(self,status):
        lista_pedidos=[pedido for pedido in pedidos if pedido.status==status]
        return lista_pedidos
'''
    def actualizar_orden(self,id,data):
        
    def eliminar_orden()'''


class HTTPDataHandler:
    @staticmethod
    def handler_respons(handler,status,data):
        handler.send_response(status)
        handler.send_header("Content-type","application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))
    
    @staticmethod
    def handler_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        data = handler.rfile.read(content_length)
        return json.loads(data.decode("utf-8"))

class RestRequestHanlder(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if parsed_path.path == "/orders":
            if "status" in query_params:
                estado = query_params["status"][0]
                ordenes_estado = self.orders.buscar_por_estado(estado)
                if ordenes_estado:
                    HTTPDataHandler.handler_respons(self,200,ordenes_estado)
                else:
                    HTTPDataHandler.handler_respons(self,404,{"Error":"estado no existente"})
            
            else:
                response_data = self.orders
                HTTPDataHandler.handler_respons(self,404,response_data)
                    
        else:
            HTTPDataHandler.handler_respons(self,404,{"mensaje":"Ruta no encontrada"})
    
    def do_POST(self):
        if self.path == "/orders":
            data = HTTPDataHandler.handler_reader(self)
            response_data = self.orders.crear_orden(data)
            HTTPDataHandler.handler_respons(self,201,response_data.__dict__)
        else:
            HTTPDataHandler.handler_respons(self,404,{"mensaje":"Ruta no existente"})
    def do_PUT(self):
        if self.path.startswith("/orders/"):
            orden_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handler_reader(self)
            response_data = self.orders.actualizar_orden(orden_id,data)
            if response_data:
                HTTPDataHandler.handler_respons(self,200,response_data.__dict__)
            else:
                HTTPDataHandler.handler_respons(self,404,{"mensaje":"Orden no existente"})
        else:
            HTTPDataHandler.handler_respons(self,404,{"mensaje":"Ruta no existente"})
        
    def do_DELETE(self):
        if self.path.startswith("/orders/"):
            order_id = int(self.path.split("/")[-1])
            response_data = self.orders.eliminar_orden(orden_id)
            if response_data:
                HTTPDataHandler.handler_respons(self,200,response_data)
            else:
                HTTPDataHandler.handler_respons(self,404,{"mensaje":"Orden no existente"})


def run(port=8000,server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print (f"Inciando servidor en {port}")
    httpd.serve_forever()

if __name__=="__main__":
    run()






































