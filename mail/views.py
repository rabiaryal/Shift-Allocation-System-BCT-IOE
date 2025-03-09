from django.http import HttpResponse
from .utils import send_mail_with_attachment
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import os

# def send_email_view(request): 
#     send_mail_with_attachment(
#         subject="Shift Allocated Table",
#         message="Please find the allocated shifts attached.",
#         file_path = "C:\\django\\SAS_final\\SAS\\Updated_Schdeule.csv",
#     )
#     return HttpResponse("Email sent successfully!")


# class SendEmailView(APIView):
#     def post(self, request):
#         # recipient_email = request.data.get("email")
#         # subject = request.data.get("subject", "Default Subject")
#         # message = request.data.get("message", "This is a test email.")

#         example = [
#         "sumeshdhoju@gmail.com",
        
#         ]
#         recipient_list = example

#         try:
#             send_mail(
#                 subject="Shift Allocated Table",
#                 message="Please find the allocated shifts attached.",
#                 from_email="sumesh10.d@gmail.com",  # Sender email (must match EMAIL_HOST_USER)
#                 to = recipient_list,
#                 file_path = "C:\\django\\SAS_final\\SAS\\Updated_Schdeule.csv",
#                 fail_silently=False,
#             )
#             return Response({"message": "Email sent successfully!"}, status=status.HTTP_200_OK)
#         except Exception as e:
            #  return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SendEmailView(APIView):
    def post(self, request):
        try:
            file_path = "D:\\minnor05\\SAS\\Updated_Schedule.xlsx"

           

            if not os.path.exists(file_path):  
                return Response({"error": "File not found!"}, status=status.HTTP_400_BAD_REQUEST)


            send_mail_with_attachment(
                subject="Shift Allocated Table",
                message="Please find the allocated shifts attached.",
                file_path = file_path,
            )
            return Response({"message": "Email sent successfully!"}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
