import { TestBed } from '@angular/core/testing';
import { CurrencyTableComponent } from './currency-table.component';
import { provideHttpClient } from '@angular/common/http';
import { provideHttpClientTesting } from '@angular/common/http/testing';

describe('CurrencyTableComponent', () => {

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CurrencyTableComponent],
      providers: [
        provideHttpClient(),
        provideHttpClientTesting()
      ]
    }).compileComponents();
  });

  it('should create component', () => {
    const fixture = TestBed.createComponent(CurrencyTableComponent);
    const component = fixture.componentInstance;
    expect(component).toBeTruthy();
  });

  it('should initialize with empty rates list', () => {
    const fixture = TestBed.createComponent(CurrencyTableComponent);
    const component = fixture.componentInstance;
    expect(component.rates.length).toBe(0);
  });
});
