import { Dish } from './dish';
import { async } from '@angular/core/testing';

describe('Dish', () => {

  const inter: Dish = {
    id: 1,
    name: '',
    description: '',
    country: '',
    category: '',
  };

  interface MockDish {
    id: number,
    name: string,
    description: string,
    country: string,
    category: string,
  };

  let MockDish = {} as MockDish;

  it('Dish object should have id defined', async(() => {
    expect(inter.id).toEqual(1);
  }));

  it('Dish object should have name defined', async(() => {
    expect(inter.name).toEqual('');
  }));

  it('Dish object should have description defined', async(() => {
    expect(inter.description).toEqual('');
  }));

  it('Dish object should have country defined', async(() => {
    expect(inter.country).toEqual('');
  }));

  it('Dish object should have category defined', async(() => {
    expect(inter.category).toEqual('');
  }));


});
;