# from django.views.generic import ListView, CreateView, DetailView
# from django.shortcuts import redirect
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin

# from .models import Report
# from .forms import ReportFileForm 
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Report, ReportFile
from .forms import ReportForm, ReportFileFormSet


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
        if file_formset.is_valid():
            report_files = file_formset.save(commit=False)
            for file in report_files:
                file.report = self.object
                file.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)
        
class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    context_object_name = 'report'
    template_name = 'reports/report_detail.html'
