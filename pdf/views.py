from django.shortcuts import render,redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/reg/user_login')
def resume1(request):

   

    
    pro = Profile.objects.filter(member = request.user.id)
#    pro = Profile.objects.filter(id = request.user.id)
#    pro = Profile.objects.filter(pk=id)
    
    return render(request, 'pdf/pdf.html', {'pro': pro}, )



@login_required(login_url='/reg/user_login')
def accept(request):
    
    if request.method == 'POST':
        #pro1 = Profile()
       # name = request.POST.get("name","")        
        #email = request.POST.get("email","")
       # phone = request.POST.get("phone","")
      #  summary = request.POST.get("summary","")
     #   degree = request.POST.get("degree","")
    #    school = request.POST.get("school","")
   #     university = request.POST.get("university","")
  #      previous_work = request.POST.get("previous_work","")
 #       skill = request.POST.get("skill","")
#        pro1.member = request.user.id

        pro1 = Profile()
        pro1.name = request.POST.get('name')
        pro1.member = request.user.id
        pro1.email = request.POST.get('email')
        pro1.phone = request.POST.get('phone')
        pro1.summary = request.POST.get('summary')
        pro1.degree = request.POST.get('degree')
        pro1.school = request.POST.get('school')
        pro1.university = request.POST.get('university')
        pro1.previous_work = request.POST.get('previous_work')
        pro1.skill = request.POST.get('skill')
        

#        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_work=previous_work, skill=skill)

        pro1.save()
#        profile.save()
        messages.info(request , 'Created Successfully')
        return redirect('/')
    #return render(request,'pdf/accept.html')
    return render(request,'pdf/accept.html')




@login_required(login_url='/reg/user_login')
def resume(request, id):

    user_profile = Profile.objects.get(pk=id)

    template_path = 'pdf/resume.html'
    
#   context = {'myvar': 'This is your template Aniket'}
    context = {'user_profile': user_profile}    

    response = HttpResponse(content_type='application/pdf')

    # if pdf download
#    response['Content-Disposition'] = 'attachment; file="agreement.pdf"'

# if pdf view
    response['Content-Disposition'] = 'file="agreement.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response
    )
    if pisa_status.err:
        return HttpResponse('We had some error <pre>' + html + '</pre>')
    return response




