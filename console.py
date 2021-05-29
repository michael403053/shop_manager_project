import pdb
from models.reciept import Reciept


from models.product import Product
import repositories.products_repository as products_repository


from models.staff import Staff
import repositories.staff_repository as staff_repository


from models.manufacturer import Manufacturer
import repositories.manufacturers_repository as manufacturers_repository

from models.reciept import Reciept
import repositories.reciept_repository as reciept_repository


manufacturer_2 = Manufacturer("Beakers", "0473t23846")
manufacturers_repository.save(manufacturer_2)

staff_1 = Staff("Gregory")
staff_repository.save(staff_1)

product_1 = Product("Ed", "Lots of Ed", 3, 4, 5, manufacturer_2)
products_repository.save(product_1)

reciept_1 = Reciept(product_1, staff_1, "03:04:05", 56)
reciept_repository.save(reciept_1)

# product_1_update = Product("Edward", "Heaps of Ed", 30, 40, 500, manufacturer_2)
# products_repository.update(product_1_update)


pdb.set_trace()

