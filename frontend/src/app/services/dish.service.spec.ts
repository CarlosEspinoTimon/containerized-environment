import { TestBed } from '@angular/core/testing';

import { DishService } from './dish.service';

import { HttpHeaders } from '@angular/common/http';

import { BehaviorSubject } from 'rxjs';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { Dish } from '../models/dish';

describe('DishService', () => {
    let service: DishService;
    let headers = new HttpHeaders().set('Content-Type', 'application/json');
    let currentPromotersSubject: BehaviorSubject<Array<Dish>> = new BehaviorSubject<Array<Dish>>({} as Array<Dish>);

  beforeEach(() => TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [DishService],
  }));

  it('should be created', () => {
    const service: DishService = TestBed.get(DishService);
    expect(service).toBeTruthy();
  });
});
