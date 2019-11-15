import { Injectable } from '@angular/core';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { environment } from './../../environments/environment';
import { Observable, BehaviorSubject } from 'rxjs';
import { Dish } from '../models/dish';

@Injectable({
  providedIn: 'root'
})
export class DishService {

    public currentDishSubject: BehaviorSubject<Array<Dish>>;
    headers = new HttpHeaders().set('Content-Type', 'application/json');
    baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) { 
      this.currentDishSubject = new BehaviorSubject<Array<Dish>>({} as Array<Dish>);
  }

  public getDishes(): Observable<Array<Dish>> {
      return this.http.get<Array<Dish>>(this.baseUrl + '/api/dishes/', { headers: this.headers });
  }
}
