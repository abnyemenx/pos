[app]

# عنوان واسم التطبيق
title = POS Inventory
package.name = posapp
package.domain = org.test

# مسار الملفات والامتدادات المطلوبة
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

# إصدار التطبيق
version = 0.1

# المكتبات البرمجية التي يعتمد عليها الكود
requirements = python3,kivy

# اتجاه الشاشة (عمودي)
orientation = portrait
fullscreen = 0

# المعماريات المدعومة لأجهزة الأندرويد الحديثة
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]

# مستوى تسجيل السجلات والتقارير
log_level = 2
warn_on_root = 1
