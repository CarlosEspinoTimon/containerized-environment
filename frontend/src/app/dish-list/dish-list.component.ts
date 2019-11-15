import { Component, OnInit } from '@angular/core';

import { Dish } from '../models/dish';
import { DishService } from '../services/dish.service';

@Component({
  selector: 'app-dish-list',
  templateUrl: './dish-list.component.html',
  styleUrls: ['./dish-list.component.css']
})
export class DishListComponent implements OnInit {


  dishList: Array<Dish> = new Array<Dish>();


  constructor(private dishProvider: DishService) { }

  ngOnInit() {
    this.dishProvider.getDishes().subscribe(
        (data) => {
            this.dishProvider.currentDishSubject.next(data);
        }
    );
    this.dishProvider.currentDishSubject.subscribe(
        (data) => {
            this.dishList = Array.from(data);
        }
    )
  }

}
