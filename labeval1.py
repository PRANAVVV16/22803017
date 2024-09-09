movies = {
    '001': {'title': '3 idiots', 'copies': 5},
    '002': {'title': 'de dana dan', 'copies': 3},
    '003': {'title': 'bajirao mastaani', 'copies': 4}
}

customers = {
    'A101': {'name': 'satish', 'rented_movies': []},
    'B102': {'name': 'gautam', 'rented_movies': []}
}

def rent_movie(customer_id, movie_id):
    if movie_id in movies and movies[movie_id]['copies'] > 0:
        customers[customer_id]['rented_movies'].append(movies[movie_id]['title'])
        movies[movie_id]['copies'] -= 1
        print(f"{customers[customer_id]['name']} rented {movies[movie_id]['title']}")
    else:
        print("Movie not available!")

def return_movie(customer_id, movie_id):
    if movies[movie_id]['title'] in customers[customer_id]['rented_movies']:
        customers[customer_id]['rented_movies'].remove(movies[movie_id]['title'])
        movies[movie_id]['copies'] += 1
        print(f"{customers[customer_id]['name']} returned {movies[movie_id]['title']}")
    else:
        print(f"{customers[customer_id]['name']} did not rent {movies[movie_id]['title']}")

def rental_report():
    for customer_id, customer in customers.items():
        print(f"{customer['name']} has rented: {', '.join(customer['rented_movies']) if customer['rented_movies'] else 'No movies'}")

rent_movie('A101', '001')
rent_movie('B102', '003')
rental_report()
return_movie('A101', '001')
rental_report()
            
