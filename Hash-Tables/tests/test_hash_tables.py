import pytest
from hash_tables import HashTable


def test_hash_method1():
  expected = 652
  hash = HashTable()
  actual = hash._HashTable__hash('d')
  assert expected == actual

def test_hash_method2():
  expected = 734
  hash = HashTable()
  actual = hash._HashTable__hash('z')
  assert expected == actual

def test_hash_method3():
  expected = "mahdi"
  hash = HashTable()
  hash.set('name', 'mahdi')
  actual = hash.get('name')
  assert expected == actual

def test_hash_method4():
  expected = None
  hash = HashTable()
  hash.set('name', 'mahdi')
  actual = hash.get('age')
  assert expected == actual

def test_hash_method5():
  expected = ['name', 'gender', 'age']
  hash = HashTable()
  hash.set('name', 'mahdi')
  hash.set('gender', 'male')
  hash.set('age', '25')

  actual = hash.keyss()
  assert expected == actual

def test_hash_method6():
  expected = 'ahmad'
  hash = HashTable()
  hash.set('name', 'mahdi')
  hash.set('name', 'ahmad')
  hash.set('gender', 'male')
  hash.set('age', '25')

  actual = hash.get('name')
  assert expected == actual

def test_hash_method7():
  expected = True
  hash = HashTable()
  hash.set('name', 'mahdi')
  hash.set('name', 'ahmad')

  actual = hash.check_collision('name')
  assert expected == actual

def test_hash_method8():
  expected = False
  hash = HashTable()
  hash.set('name', 'mahdi')
  hash.set('name', 'ahmad')
  hash.set('gender','male')

  actual = hash.check_collision('gender')
  assert expected == actual


def test_hash_method9():
  expected = 1024
  hash = HashTable()
  actual = hash._HashTable__hash('hi')
  assert expected >= actual
