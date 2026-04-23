
# analisis_ventas.py

from collections import defaultdict

# Carga de datos de ventas con productos de tecnología y gaming actuales
ventas = [
    {"fecha": "2026-03-01", "producto": "GPU RTX 4080", "cantidad": 2, "precio": 1299.99},
    {"fecha": "2026-03-01", "producto": "Teclado mecánico custom", "cantidad": 4, "precio": 189.90},
    {"fecha": "2026-03-02", "producto": "Monitor OLED 27\"", "cantidad": 1, "precio": 749.50},
    {"fecha": "2026-03-02", "producto": "Steam Deck", "cantidad": 3, "precio": 499.00},
    {"fecha": "2026-03-03", "producto": "Suscripción Game Pass", "cantidad": 10, "precio": 14.99},
    {"fecha": "2026-03-03", "producto": "Teclado mecánico custom", "cantidad": 1, "precio": 189.90},
    {"fecha": "2026-03-04", "producto": "Auriculares gaming inalámbricos", "cantidad": 5, "precio": 129.99},
    {"fecha": "2026-03-04", "producto": "GPU RTX 4080", "cantidad": 1, "precio": 1299.99},
    {"fecha": "2026-03-05", "producto": "Monitor OLED 27\"", "cantidad": 2, "precio": 749.50},
    {"fecha": "2026-03-05", "producto": "Steam Deck", "cantidad": 2, "precio": 499.00},
]

ventas_por_producto = defaultdict(int)
precios_por_producto = defaultdict(lambda: (0.0, 0))
ingresos_por_dia = defaultdict(float)
ingresos_por_producto = defaultdict(float)

for venta in ventas:
    fecha = venta["fecha"]
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    ingresos_venta = cantidad * precio

    ventas_por_producto[producto] += cantidad
    total_precio, cantidad_total = precios_por_producto[producto]
    precios_por_producto[producto] = (total_precio + ingresos_venta, cantidad_total + cantidad)
    ingresos_por_dia[fecha] += ingresos_venta
    ingresos_por_producto[producto] += ingresos_venta

ingreso_total_global = sum(venta["cantidad"] * venta["precio"] for venta in ventas)

max_ventas = max(ventas_por_producto.values())
productos_mas_vendidos = [producto for producto, cantidad in ventas_por_producto.items() if cantidad == max_ventas]
producto_mas_vendido = ", ".join(productos_mas_vendidos)

promedios_por_producto = {
    producto: total_precio / cantidad_total if cantidad_total else 0.0
    for producto, (total_precio, cantidad_total) in precios_por_producto.items()
}

resumen_ventas = {
    producto: {
        "cantidad_total": ventas_por_producto[producto],
        "ingresos_totales": ingresos_por_producto[producto],
        "precio_promedio": promedios_por_producto[producto],
    }
    for producto in ventas_por_producto
}

print("\n" + "=" * 64)
print("REPORTE DE ANÁLISIS DE VENTAS")
print("=" * 64)
print("\nLista original de ventas:")
for venta in ventas:
    print(f"- Fecha: {venta['fecha']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: ${venta['precio']:,.2f}")

print("\n" + "-" * 64)
print(f"Ingreso total global: ${ingreso_total_global:,.2f}")
print(f"Producto más vendido: {producto_mas_vendido} ({max_ventas} unidades)")
print("-" * 64)

print("\nDesglose de promedios por producto:")
for producto, promedio in promedios_por_producto.items():
    print(f"- {producto}: precio promedio ${promedio:,.2f}")

print("\nIngresos por día:")
for fecha, ingresos in sorted(ingresos_por_dia.items()):
    print(f"- {fecha}: ${ingresos:,.2f}")

print("\nResumen de ventas por producto:")
for producto, resumen in resumen_ventas.items():
    print(
        f"- {producto}: cantidad total {resumen['cantidad_total']}, "
        f"ingresos totales ${resumen['ingresos_totales']:,.2f}, "
        f"precio promedio ${resumen['precio_promedio']:,.2f}"
    )
