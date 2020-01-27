import libreria as c

def test_suma():
    assert c.suma([2,1],[4,1]) == [6,2],'Debe ser 6+2i'
def test_resta():
    assert c.resta([3,1],[2,1]) == [1,0],'Debe ser 1+0i'
def test_producto():
    assert c.producto([3,4],[2,1]) == [2,11],'Debe ser 2+11i'
def test_fase():
    assert c.fase([5,8]) == 57.9946167919165,'Debe ser 57.9946167919165'
def test_conjugado():
    assert c.conjugado([4,3]) == [4,-3],'Debe ser 4-3i'
def test_division():
    assert c.division([3,4],[2,1]) == [2,1],'Debe ser 2+i'
def test_convertirCaPo():
    assert c.convertirCaPo([8,2]) == [8.246211251235321,14.036243467926479],'Debe ser [8.246211251235321,14.036243467926479]'
def test_convertirPoCa():
    assert c.convertirPoCa([8.246211251235321,14.036243467926479]) == [8.0, 2.0],'Debe ser [8.0, 2.0]'
def test_modulo():
    assert c.modulo([-4,8])== 8.94427190999916,'Debe ser 8.94427190999916'
def test_potencia():
    assert c.potencia([2,4],2)==[20,126],'Debe ser [20,126]'


if __name__=='__main__':
    test_suma()
    test_resta()
    test_producto()
    test_fase()
    test_conjugado()
    test_division()
    test_convertirCaPo()
    test_convertirPoCa()
    test_modulo()
    test_potencia()
    print('Prueba exitosa')
    

