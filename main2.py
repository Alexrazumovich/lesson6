class Test():
    def public_func(self):
        print("This is a public function.")
    def _protected_func(self):
        print("This is a protected function.")
    def __private_func(self):
        print("This is a private function.")
    def test_private_func(self):
        self.__private_func()
test=Test()
test.public_func()
test._protected_func()
test.test_private_func()