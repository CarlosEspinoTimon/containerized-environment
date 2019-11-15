import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DishListComponent } from './dish-list.component';

import { MatIconModule } from '@angular/material/icon';
import { MatListModule } from '@angular/material/list';
import { Dish } from '../models/dish';
import { of, Observable, BehaviorSubject } from 'rxjs';
import { DishService } from '../services/dish.service';

describe('DishListComponent', () => {
  let component: DishListComponent;
  let fixture: ComponentFixture<DishListComponent>;

  class MockDishService {
      dishList: Array<Dish> = [];
      getDishes(): Observable<any[]> {
          return of(this.dishList);
      }
      currentDishSubject: BehaviorSubject<Array<Dish>> = new BehaviorSubject<Array<Dish>>({} as Array<Dish>);
  }

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DishListComponent ],
      imports: [
          MatIconModule,
          MatListModule,
      ],
      providers: [
          { provide: DishService, useClass: MockDishService },
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DishListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
