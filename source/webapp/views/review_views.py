from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView

from webapp.models import Review


class IssueForProjectCreateView(PermissionRequiredMixin, UserPassesTestMixin, CreateView):
    model = Review
    template_name = 'reviews/create.html'
    form_class = ProjectIssueForm
    permission_required = 'webapp.add_issue'
    permission_denied_message = '403 Access Denied!'

    def test_func(self):
        project_users = []
        for user in self.get_project().users.all():
            project_users.append(user)
            print(user)
        return self.request.user in project_users

    def dispatch(self, request, *args, **kwargs):
        self.project = self.get_project()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = self.project.issues.create(
            created_by=self.request.user,
            **form.cleaned_data
        )
        return redirect('webapp:project_view', pk=self.project.pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if hasattr(self, 'object'):
            kwargs.update({'project': self.get_project()})
        return kwargs

    def get_project(self):
        project_pk = self.kwargs.get('pk')
        return get_object_or_404(Project, pk=project_pk)
