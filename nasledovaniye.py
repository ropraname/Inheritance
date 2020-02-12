class PaySystem:
    def __init__(self):
        self.paid = 0

    def spend(self, pay_object):
        print("Spent {} rubles to {}".format(pay_object.count_money(), pay_object.name))
        self.paid += pay_object.count_money()

class CommonEmployee(PaySystem):
	def __init__(self, name):
		self.base = 500
		self.name = name

	def name(self):
		return self.name

	def count_money(self):
		return self.base

class CommissionEmployee(CommonEmployee):
	def __init__(self, name):
		super().__init__(name)
		self.taxes = 200

	def name(self):
		return self.name

	def count_money(self):
		return self.base + self.taxes

class HourlyEmployee(CommonEmployee):
	def __init__(self, name, hours):
		super().__init__(name)
		self.hours = hours

	def name(self):
		return self.name

	def count_money(self):
		return super().count_money() + 100*self.hours

class CompetitiveEmployee(CommissionEmployee):
	def __init__(self, name, sell_items):
		super().__init__(name)
		self.sell_items = sell_items

	def name(self):
		return self.name

	def count_money(self):
		return self.base + self.taxes* self.sell_items

class Taxes:
	def __init__(self):
		self.name = 'Taxes'

	def count_money(self):
		return 150


# этот код менять нельзя
# BaseEmployee tests
def test_base_employee():
    be_name = 'Alice'
    be = BaseEmployee(name=be_name)
    assert be.name == be_name
    assert be.get_worker_type() == 'BaseEmployee'
    assert be.count_money() == 500
    print('Test passed')

# OfficialEmployee tests
def test_official_employee():
    oe_name = 'Bob'
    oe = OfficialEmployee(name=oe_name)
    assert oe.name == oe_name
    assert oe.get_worker_type() == 'OfficialEmployee'
    assert oe.count_money() == 610
    print('Test passed')

# HourlyEmployee tests
def test_hourly_employee():
    he_name = 'Carol'
    he = HourlyEmployee(name=he_name, hours=8)
    assert he.name == he_name
    assert he.get_worker_type() == 'HourlyEmployee'
    assert he.count_money() == 650
    print('Test passed')

# CompetitiveEmployee tests
def test_competitive_employee():
    ce_name = 'Dave'
    ce = CompetitiveEmployee(name=ce_name, sold_items=10)
    assert ce.name == ce_name
    assert ce.get_worker_type() == 'CompetitiveEmployee'
    assert ce.count_money() == 850
    print('Test passed')

test_base_employee()
test_official_employee()
test_hourly_employee()
test_competitive_employee()
print('Tests OK')