import json
from django.contrib import admin
from .models import Book,BookImport,Catalog,color_group,color,product_test_1
from .forms import BookImportForm,CatalogImportForm
from django.shortcuts import render,reverse
from django.urls import path
from django.contrib import messages
from django.http import HttpResponseRedirect
import csv
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# класс обработки данных
class BookResource(resources.ModelResource):
    class Meta:
        model = Book

# вывод данных на странице
#@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_classes = [BookResource]
    list_display = ['name','author','date_published']
#
admin.site.register(Book, BookAdmin)
    #
    # def get_urls(self):
    #     urls = super().get_urls()
    #     urls.insert(-1,path('csv-upload/', self.csv_upload))
    #     return urls
    #
    # def csv_upload(self,request):
    #     if request.method == 'POST':
    #         form = BookImportForm(request.POST, request.FILES)
    #         opts = Book._meta
    #         field_1 = [field for field in opts.get_fields()]
    #         fields = field_1[1:]
    #         fields_name = [field_name.name for field_name in fields ]
    #         if form.is_valid():
    #             form_object = form.save()
    #             with form_object.csv_file.open('r') as csv_file:
    #                 rows = csv.reader(csv_file, delimiter=',')
    #                 dict_reader = csv.DictReader(csv_file)
    #                 #if next(rows) != ['name', 'author', 'date_published']:
    #                     #messages.warning(request, 'Не правильные заголовки')
    #                     #return HttpResponseRedirect(request.path_info)
    #                 #for row in rows: #т.к. выше мы применили метод next(rows)то здесь он продолжается с того места
    #                 next(rows)
    #                 books = [Book(**row) for row in dict_reader]
    #                 Book.objects.bulk_create(books)
    #
    #
    #
    #             messages.success(request, 'Файл успешно загружен')
    #             return HttpResponseRedirect(reverse('admin_rename:index'))
    #     else:
    #         form = BookImportForm()
    #     return render(request, 'admin_rename/csv_import_page.html',{'form':form})

@admin.register(BookImport)
class BookImport(admin.ModelAdmin):
    list_display = ['csv_file','date_added']

# class CatalogResource(resources.ModelResource):
#     class Meta:
#         model = Catalog
#
# # вывод данных на странице
# #@admin.register(Book)
# class CatalogAdmin(ImportExportModelAdmin):
#     resource_classes = [CatalogResource]
#     list_display = ['title','parent_id','lft','rgt']
# #
# admin.site.register(Catalog, CatalogAdmin)
@admin.register(color_group)
class color_group_admin(admin.ModelAdmin):
    list_display = ['id','title','position']

@admin.register(product_test_1)
class product_test_admin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(color)
class colorAdmin(admin.ModelAdmin):
    list_display = ['id','color_group_id','title','picture','position']


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['id','title','parent_id','lft','rgt']

    def get_urls(self):
        urls = super().get_urls()
        urls.insert(-1,path('json_upload/', self.json_upload))
        return urls
    def json_upload(self,request):
        if request.method == 'POST' and request.FILES['json_file']:
            form = CatalogImportForm(request.POST,request.FILES)
            if form.is_valid():
                form_object = form.save()
                with form_object.json_file.open('r') as json_file1:
                    data = json.load(json_file1)
                    data_keys = data.keys()
                    data_values = data.values()
                    for keys in data_keys:
                        work_class = globals()[keys]
                        work_class.objects.bulk_create([work_class(**row) for row in data[keys]]) #создаем обьект класса по данным переданным с помошью ключа
                    messages.success(request, 'файл успешно загружен')
                    return HttpResponseRedirect(reverse('admin:index'))
        else:
            form = CatalogImportForm()
        return render (request, 'admin/json_import.html',{'form':form})
