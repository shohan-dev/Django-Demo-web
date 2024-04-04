import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Fetch data from an API and filter it before sending a JSON response
def get_filtered_data(request):
    api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json' 

    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()  

        filtered_data = {
            "time": data["time"]["updated"],
            "USD_rate": data["bpi"]["USD"]["rate"],
            "EUR_rate": data["bpi"]["EUR"]["rate"]
        }

        return JsonResponse(filtered_data, status=200)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt  
def post_data(request):
    # Process JSON data sent from Postman and return a JSON response
    if request.method == 'POST':
        try:
            received_data = json.loads(request.body)
            
            key1_value = received_data.get('key1', None)
            key2_value = received_data.get('key2', None)

            response_data = {
                "message": "Data received successfully",
                "key1": key1_value,
                "key2": key2_value
            }

            return JsonResponse(response_data, status=200)
        
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@csrf_exempt
def post_data_file(request):
    # Process uploaded files and return a JSON response
    if request.method == 'POST':
        try:
            if 'file_key' in request.FILES:
                uploaded_file = request.FILES['file_key']
                
                response_data = {
                    "message": "File received successfully",
                    "file_name": uploaded_file.name,
                    "file_size": uploaded_file.size,
                }

                return JsonResponse(response_data, status=200)
            else:
                return JsonResponse({'error': 'No file was uploaded'}, status=400)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    else:
        return JsonResponse({'error': 'Only POST requests are allowed send file in key = file_key '}, status=405)
