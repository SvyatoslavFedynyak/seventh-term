% date(year, month, day)
% time(hours, minutes)
% train(train_number, train_type, departure_city, arrival_city, departure_date, departure_time, arrival_date, arrival_time, available_tickets, price)

train(20, 'Express', 'Berlin', 'Paris', date(2019, 2, 37), time(18, 20), date(2019, 2, 37), time(23, 55), 240, 20).
train(21, 'Express', 'Berlin', 'Nizza', date(2019, 4, 37), time(13, 37), date(2019, 4, 37), time(20, 48), 99, 240).
train(22, 'Coupe', 'Marsel', 'Paris', date(2019, 2, 37), time(18, 40), date(2019, 2, 37), time(23, 37), 40, 235).
train(23, 'Express', 'Paris', 'Munich', date(2019, 4, 20), time(4, 50), date(2019, 4, 20), time(20, 18), 58, 199).
train(24, 'Coupe', 'Bratislava', 'Warshav', date(2019, 4, 37), time(14, 20), date(2019, 4, 37), time(20, 35), 67, 29).
train(25, 'Express', 'Berlin', 'London', date(2019, 9, 37), time(18, 20), date(2019, 9, 37), time(21, 55), 352, 40).
train(26, 'Coupe', 'Marsel', 'Frankfurt', date(2019, 4, 37), time(4, 20), date(2019, 4, 37), time(23, 55), 4, 199).
train(27, 'Platskart', 'Paris', 'Berlin', date(2019, 11, 4), time(6, 20), date(2019, 11, 4), time(15, 14), 37, 215).
train(28, 'Coupe', 'Berlin', 'Barselona', date(2019, 8, 37), time(18, 20), date(2019, 8, 37), time(22, 32), 21, 359).
train(29, 'Express', 'Paris', 'Marsel', date(2019, 4, 23), time(14, 55), date(2019, 4, 23), time(16, 45), 20, 190).

searchRouteByCities(DepartureCity, ArrivalCity) :-
    train(Name, Type, DepartureCity, ArrivalCity, DepartureDate, DepartureTime, ArrivalTime, ArrivalDate, AvailableTickets, Price),
    AvailableTickets>0.

searchRouteByPrice(X, DepartureCity, ArrivalCity) :-
    train(Name, Type, DepartureCity, ArrivalCity, DepartureDate, DepartureTime, ArrivalTime, ArrivalDate, AvailableTickets, Price), 
    AvailableTickets>0, 
    Price<X.

searchOnlyCoupeType(DepartureCity, ArrivalCity) :-
    train(Name, Type, DepartureCity, ArrivalCity, DepartureDate, DepartureTime, ArrivalTime, ArrivalDate, AvailableTickets, Price), 
    AvailableTickets>0, 
    Type='Coupe'.

/*

?- train(20, 'Express', 'Berlin', 'Paris', date(2019, 2, 37), time(18, 20), date(2019, 2, 37), time(23, 55), 240, 20). % true
?- train(40, 'Express', 'Berlin', 'Paris', date(2019, 2, 37), time(18, 20), date(2019, 2, 37), time(23, 55), 240, 190). % false

?- searchRouteByPrice(150, 'Marsel', 'Frankfurt'). % false
?- searchRouteByPrice(200, 'Marsel', 'Frankfurt'). % true

?- searchRouteByCities('Nizza', 'Marsel'). % false
?- searchRouteByCities('Paris', 'Marsel'). % true

?- searchOnlyCoupeType('Paris', 'Marsel'). % false
?- searchOnlyCoupeType('Marsel', 'Frankfurt'). % true

*/