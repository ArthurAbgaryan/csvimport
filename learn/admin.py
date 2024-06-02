from django.contrib import admin
from .models import Book,BookImport
from .forms import BookImportForm
from django.shortcuts import render,reverse
from django.urls import path
from django.contrib import messages
from django.http import HttpResponseRedirect
import csv
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# класс обработки данных
# class BookResource(resources.ModelResource):
#
#     class Meta:
#         model = Book
#
# # вывод данных на странице
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
#     resource_classes = [BookResource]
    list_display = ['name','author','date_published']
#
# admin.site.register(Book, BookAdmin)

    def get_urls(self):
        urls = super().get_urls()
        urls.insert(-1,path('csv-upload/', self.csv_upload))
        return urls

    def csv_upload(self,request):
        if request.method == 'POST':
            form = BookImportForm(request.POST, request.FILES)
            opts = Book._meta
            field_1 = [field for field in opts.get_fields()]
            fields = field_1[1:]
            fields_name = [field_name.name for field_name in fields ]
            if form.is_valid():
                form_object = form.save()
                with form_object.csv_file.open('r') as csv_file:
                    rows = csv.reader(csv_file, delimiter=',')
                    dict_reader = csv.DictReader(csv_file)
                    if next(rows) != ['name', 'author', 'date_published']:
                        messages.warning(request, 'Не правильные заголовки')
                        return HttpResponseRedirect(request.path_info)
                    #for row in rows: #т.к. выше мы применили метод next(rows)то здесь он продолжается с того места
                    books = [Book(**row) for row in dict_reader]
                    Book.objects.bulk_create(books)
                        


                messages.success(request, 'Файл успешно загружен')
                return HttpResponseRedirect(reverse('admin:index'))
        else:
            form = BookImportForm()
        return render(request, 'admin/csv_import_page.html',{'form':form})

@admin.register(BookImport)
class BookImport(admin.ModelAdmin):
    list_display = ['csv_file','date_added']

# Register your models here.
