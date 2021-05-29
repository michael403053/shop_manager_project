import pdb
from models.reciept import Reciept


from models.product import Product
import repositories.products_repository as products_repository


from models.staff import Staff


from models.manufacturer import Manufacturer
import repositories.manufacturers_repository as manufacturers_repository


manufacturer_2 = Manufacturer("Beakers", "0473t23846")
manufacturers_repository.save(manufacturer_2)

product_1 = Product("Ed", "Lots of Ed", 3, 4, 5, manufacturer_2)
products_repository.save(product_1)

product_1_update = Product("Edward", "Heaps of Ed", 30, 40, 500, manufacturer_2)
products_repository.update(product_1_update)


pdb.set_trace()

