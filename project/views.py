from sqlite3 import Connection, connect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import connections
from django.db import connection
# from .forms import RegistrationForm
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# from ldap3 import SIMPLE, SYNC, Server, Connection, ALL
import datetime

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def view_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            if connect.bind():
                user, _ = User.objects.get_or_create(username=username)
                with connections['saspo_training'].cursor() as cursor:
                 cursor.execute("EXEC [dbo].[Panel_Support_Login]  @Username=%s", [username])
                 result_set = cursor.fetchall()
                 result_message = result_set[0][0]
                 if result_message == 'Login successful':
                # Successful authentication
                   print("LDAP Bind Successful")
                   login(request, user)
                   return redirect('partneret')
                 else:
                     messages.error(request, 'You are not allowed to sign in')
            else:
                messages.error(request, 'Invalid username or password ')
        except Exception as e:
            print(f"LDAP Error: {str(e)}")
        finally:
            Connection.unbind()


    
    return render(request, 'login.html')


def register(request):

    # if request.method == 'GET':
    #     form = RegistrationForm()
        
    #     return render(request, 'register.html', {'form': form}) 
     
    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.username = user.username.lower()
    #         user.save()
    #         messages.success(request, 'You have register successfully.')
    #         return render(request, 'register.html', {'form': form})
    #     else:
            return render(request, 'register-user.html')

def create_timetable(request):

    # with connections['database'].cursor() as cursor1:
    #     cursor1.execute("SELECT * ") # Replace 'your_first_view_name' with the actual name of your first view
    #     results1 = dictfetchall(cursor1)

    # # Execute the second view or query
    # with connections['database'].cursor() as cursor2:
    #     cursor2.execute("EXEC your_second_view_name")  # Replace 'your_second_view_name' with the actual name of your second view
    #     results2 = dictfetchall(cursor2)

    # # Combine the results into a single context
    # context = {'results1': results1, 'results2': results2}

    # return render(request, 'your_combined_template.html', context)
            return render(request, 'krijo-orar.html')

def timetable_list(request):

    # with connections['database'].cursor() as cursor1:
    #     cursor1.execute("SELECT * ") # Replace 'your_first_view_name' with the actual name of your first view
    #     results1 = dictfetchall(cursor1)

    # # Execute the second view or query
    # with connections['database'].cursor() as cursor2:
    #     cursor2.execute("EXEC your_second_view_name")  # Replace 'your_second_view_name' with the actual name of your second view
    #     results2 = dictfetchall(cursor2)

    # # Combine the results into a single context
    # context = {'results1': results1, 'results2': results2}

    # return render(request, 'your_combined_template.html', context)
            return render(request, 'lista-e-orarit.html')

# def get_options(request):
#     dega = request.GET.get('dega')
#     viti = request.GET.get('viti')

#     # Execute the query to get options based on dega and viti
#     with connections['database'].cursor() as cursor:
#         cursor.execute("SELECT value, text FROM YourOptionsTable WHERE dega = %s AND viti = %s", [dega, viti])
#         options = dictfetchall(cursor)

#     return JsonResponse(options, safe=False)






# context={}
#     results = None
#     if request.method == 'POST':
#          PrincipalAmount = request.POST.get('PrincipalAmount')
#          PrincipalAmountprev = request.POST.get('PrincipalAmountprev')
#          PrincipalAmountEMerge = request.POST.get('PrincipalAmountEMerge')
#          PrincipalAmountEMergeprev = request.POST.get('PrincipalAmountEMergeprev')
#          Item_id = request.POST.get('item_id')
#          Search_Item_id = request.POST.get('search_item_id')
#          DisbursementValue = request.POST.get('DisbursementValue')
#          DisbursementValueprev = request.POST.get('DisbursementValueprev')
#          CCDesInterestRate = request.POST.get('CCDesInterestRate')
#          CCDesInterestRateprev = request.POST.get('CCDesInterestRateprev')
#          CCDesPPI = request.POST.get('CCDesPPI')
#          CCDesPPIprev = request.POST.get('CCDesPPIprev')
    
#          if Search_Item_id != '' :
#             with connections['saspo_training'].cursor() as cursor:
#                 cursor.execute("EXEC [dbo].[Search_Pan_Support] @Operation=%s, @item_id=%s", ["S",Search_Item_id])
#                 results = dictfetchall(cursor)
#                 context={'results':results[0]}
                
#                 cursor.close()
#          else:
#             if Item_id is not '' :
#               with connections['saspo_training'].cursor() as cursor:
#                    cursor.execute("EXEC [dbo].[Search_Pan_Support] @Operation=%s, @item_id=%s", ["S",Item_id])
#                    results = dictfetchall(cursor)
#                    context={'results':results[0]}
#                    cursor.close()
#               if len(results) > 0:
#                 result = results[0]  # Access the first dictionary in the results list
              
#                 if DisbursementValue != DisbursementValueprev:
#                    with connections['saspo_training'].cursor() as cursor:
#                     cursor.execute("EXEC [dbo].[PanSupport_changes]  @Operation=%s,@Code=%s,@DisbursementValue=%s,@item_id=%s", ["U","O",DisbursementValue,Item_id])
#                     cursor.close()
#                 connection.commit()
#                 if PrincipalAmount != PrincipalAmountprev:
#                   with connections['saspo_training'].cursor() as cursor:
#                      cursor.execute("EXEC [dbo].[PanSupport_changes]  @Operation=%s,@Code=%s,@PrincipalAmount=%s,@item_id=%s", ["U","O",PrincipalAmount,Item_id])
#                      cursor.close()
#                 connection.commit()
#                 if PrincipalAmountEMerge != PrincipalAmountEMergeprev:
#                   with connections['saspo_training'].cursor() as cursor:
#                      cursor.execute("EXEC [dbo].[PanSupport_changes]  @Operation=%s,@Code=%s,@PrincipalAmountEMerge=%s,@item_id=%s", ["U","O",PrincipalAmountEMerge,Item_id])
#                      cursor.close()
#                 connection.commit()
              
#                 if CCDesInterestRate != CCDesInterestRateprev:
                 
#                    with connections['saspo_training'].cursor() as cursor:
#                     cursor.execute("EXEC [dbo].[PanSupport_changes]  @Operation=%s,@Code=%s,@CCDesInterestRate=%s,@item_id=%s", ["U","O",CCDesInterestRate,Item_id])
#                     cursor.close()
#                 connection.commit()
             
#               if CCDesPPI != CCDesPPIprev:
                  
#                   with connections['saspo_training'].cursor() as cursor:
#                    cursor.execute("EXEC [dbo].[PanSupport_changes]  @Operation=%s,@Code=%s,@CCDesPPI=%s,@item_id=%s", ["U","O",CCDesPPI,Item_id])
#                    cursor.close()
#               connection.commit()
#               messages.success(request,'Ndryshimet u regjistruan!')
#               return redirect ('forma-e-vendimit')