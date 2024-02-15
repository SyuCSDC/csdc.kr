from django.views.generic import ListView, CreateView, DetailView , UpdateView
from django.shortcuts import redirect , render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Report , ReportFile , Book
from .forms import ReportForm , ReportFileFormSet , BookRequestForm

class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    context_object_name = 'reports'
    template_name = 'reports/report_list.html'
    # 로그인한 사용자의 보고서만 표시
    def get_queryset(self):
        print(self.request.user)
        return Report.objects.all()


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/report_form.html'
    login_url = '/users/login/'
    success_url = reverse_lazy('report:report_list')  # URL 이름은 프로젝트에 맞게 수정해야 합니다.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['file_formset'] = ReportFileFormSet(self.request.POST, self.request.FILES)
        else:
            context['file_formset'] = ReportFileFormSet(queryset=ReportFile.objects.none())
        return context

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        context = self.get_context_data()
        file_formset = context['file_formset']
        self.object = form.save()
        if file_formset.is_valid() and any(form.cleaned_data.get('file') for form in file_formset.forms):
            self.object = form.save()
            report_files = file_formset.save(commit=False)
            for file in report_files:
                file.report = self.object
                file.save()
            return super().form_valid(form)
        else:
            form.add_error(None, "하나 이상의 파일을 첨부해야 합니다.")
            return self.form_invalid(form)
    

class ReportUpdateView(LoginRequiredMixin, UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/report_update_form.html'
    success_url = reverse_lazy('report:report_list')  # 성공 URL은 필요에 따라 조정

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            # POST 요청시, 현재 Report 인스턴스와 관련된 파일들로 ReportFileFormSet 초기화
            context['file_formset'] = ReportFileFormSet(self.request.POST, self.request.FILES, 
                                                        queryset=ReportFile.objects.filter(report=self.object))
        else:
            # GET 요청시, 동일하게 현재 Report 인스턴스와 관련된 파일들로 초기화
            context['file_formset'] = ReportFileFormSet(queryset=ReportFile.objects.filter(report=self.object))
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        file_formset = context['file_formset']
        if form.is_valid() and file_formset.is_valid():
            self.object = form.save()
            # file_formset에 instance를 설정합니다.
            instances = file_formset.save(commit=False)
            for instance in instances:
                instance.report = self.object  # Report 인스턴스를 ReportFile 인스턴스에 연결합니다.
                instance.save()

            # file_formset에서 'DELETE' 폼을 처리합니다.
            for obj in file_formset.deleted_objects:
                obj.delete()
            # for form in file_formset.deleted_forms:
            #     instance = form.instance
            #     instance.delete()  # 데이터베이스에서 인스턴스를 삭제합니다.
            # 나머지 formset 관리 로직...
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    context_object_name = 'report'
    template_name = 'reports/report_detail.html'


class BookcreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookRequestForm
    template_name = 'reports/book_request.html'
    login_url = '/users/login/'
    success_url = reverse_lazy('report:book_list')  # 성공 URL은 필요에 따라 조정
    def form_valid(self, form):
        # 현재 로그인한 사용자를 requester로 설정
        form.instance.requester = self.request.user
        return super().form_valid(form)

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'reports/book_list.html'
    def get_queryset(self):
        return Book.objects.all()
    

class BookUpdateView(LoginRequiredMixin, UpdateView): 
    model = Book
    form_class = BookRequestForm
    template_name = 'reports/book_update.html'
    success_url = reverse_lazy('report:book_list')  # 성공적으로 업데이트한 후 리디렉션될 URL