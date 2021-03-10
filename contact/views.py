from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        agent_email = request.POST['agent_email']
        agent_name = request.POST['agent_name']
         #Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
            agent_email=agent_email,
            agent_name=agent_name
        )
        contact.save()

        full_message = f"""
        Received message below from {name}, {email}
        ___________________________
        {message}

        """
        
        
        send_mail(
            subject='Davis Estate - Property Listing Inquiry',
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[agent_email, settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
          
        )

        messages.success(
            request, 'You request has been submitted, the agent will get back to you soon')

        return redirect('/listings/'+listing_id)
