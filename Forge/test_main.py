
import pytest
from main import (
    getLowStockProducts,
    addProduct,
    searchProduct,
    updateProduct
)


# --------------------------------
# 1. getLowStockProducts() tests
# --------------------------------

def test_empty_inventory():
    assert getLowStockProducts([]) == []


def test_all_products_adequately_stocked():
    products = [
        {"name": "Mouse", "Quantity": 20, "ReorderLevel": 5},
        {"name": "Keyboard", "Quantity": 15, "ReorderLevel": 5}
    ]

    assert getLowStockProducts(products) == []


def test_product_below_reorder_level():
    products = [
        {"name": "Mouse", "Quantity": 3, "ReorderLevel": 5}
    ]

    assert getLowStockProducts(products) == products


def test_product_exactly_at_reorder_level():
    products = [
        {"name": "Keyboard", "Quantity": 5, "ReorderLevel": 5}
    ]

    assert getLowStockProducts(products) == products


def test_multiple_low_stock_products():
    products = [
        {"name": "Mouse", "Quantity": 3, "ReorderLevel": 5},
        {"name": "Keyboard", "Quantity": 10, "ReorderLevel": 5},
        {"name": "Monitor", "Quantity": 5, "ReorderLevel": 5},
        {"name": "Webcam", "Quantity": 2, "ReorderLevel": 4}
    ]

    expected = [products[0], products[2], products[3]]

    assert getLowStockProducts(products) == expected


# --------------------------------
# 2. addProduct() tests
# --------------------------------

def test_add_product_successfully(monkeypatch):
    products = []

    inputs = iter(["Mouse", "SKU101", "499.99", "20", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = addProduct(products)

    assert result == {
        "name": "Mouse",
        "SKU": "SKU101",
        "Price": 499.99,
        "Quantity": 20,
        "ReorderLevel": 5
    }


def test_add_duplicate_sku(monkeypatch, capsys):
    products = [
        {"name": "Mouse", "SKU": "SKU101", "Price": 499.99,
         "Quantity": 20, "ReorderLevel": 5}
    ]

    inputs = iter(["Keyboard", "SKU101", "999", "10", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = addProduct(products)

    assert result is None
    assert "SKU already found!" in capsys.readouterr().out


# --------------------------------
# 3. searchProduct() tests
# --------------------------------

def test_search_existing_product(capsys):
    products = [
        {"name": "Mouse", "SKU": "SKU101", "Price": 499.99,
         "Quantity": 20, "ReorderLevel": 5}
    ]

    searchProduct("SKU101", products)

    output = capsys.readouterr().out

    assert "Mouse" in output
    assert "SKU101" in output


def test_search_nonexistent_product(capsys):
    products = []

    searchProduct("SKU999", products)

    output = capsys.readouterr().out

    assert "Product wasn't found!" in output


# --------------------------------
# 4. updateProduct() tests
# --------------------------------

def test_update_existing_product():
    products = [
        {"name": "Mouse", "SKU": "SKU101", "Price": 499.99,
         "Quantity": 20, "ReorderLevel": 5}
    ]

    updateProduct("SKU101", 50, products)

    assert products[0]["Quantity"] == 50


def test_update_nonexistent_product():
    products = [
        {"name": "Mouse", "SKU": "SKU101", "Price": 499.99,
         "Quantity": 20, "ReorderLevel": 5}
    ]

    original_quantity = products[0]["Quantity"]

    updateProduct("SKU999", 50, products)

    assert products[0]["Quantity"] == original_quantity


def test_update_does_not_modify_other_products():
    products = [
        {"name": "Mouse", "SKU": "SKU101", "Price": 499.99,
         "Quantity": 20, "ReorderLevel": 5},
        {"name": "Keyboard", "SKU": "SKU102", "Price": 999.99,
         "Quantity": 10, "ReorderLevel": 3}
    ]

    updateProduct("SKU101", 50, products)

    assert products[0]["Quantity"] == 50
    assert products[1]["Quantity"] == 10
