import { TestBed, ComponentFixture } from '@angular/core/testing';
import { CurrencyTableComponent } from './currency-table.component';
import { provideHttpClientTesting } from '@angular/common/http/testing';
import { of, throwError } from 'rxjs';
import { CurrencyService } from '../../services/currency.service';
import { FormsModule } from '@angular/forms';

describe('CurrencyTableComponent', () => {
  let component: CurrencyTableComponent;
  let fixture: ComponentFixture<CurrencyTableComponent>;
  let mockCurrencyService: jasmine.SpyObj<CurrencyService>;

  beforeEach(async () => {
    const spy = jasmine.createSpyObj('CurrencyService', ['fetchRates', 'getRatesByDate']);

    await TestBed.configureTestingModule({
      imports: [FormsModule],
      declarations: [CurrencyTableComponent],
      providers: [
        provideHttpClientTesting(),
        { provide: CurrencyService, useValue: spy }
      ]
    }).compileComponents();

    fixture = TestBed.createComponent(CurrencyTableComponent);
    component = fixture.componentInstance;
    mockCurrencyService = TestBed.inject(CurrencyService) as jasmine.SpyObj<CurrencyService>;
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });

  it('should initialize with empty rates and message', () => {
    expect(component.rates.length).toBe(0);
    expect(component.message).toBe('');
  });

  it('should call fetchRates and set success message', () => {
    mockCurrencyService.fetchRates.and.returnValue(of({ message: 'Data fetched successfully' }));

    component.fetchRates();
    expect(mockCurrencyService.fetchRates).toHaveBeenCalled();
    
    fixture.whenStable().then(() => {
      expect(component.message).toBe('Data fetched successfully');
    });
  });

  it('should handle fetchRates error', () => {
    mockCurrencyService.fetchRates.and.returnValue(throwError(() => new Error('API error')));

    component.fetchRates();
    fixture.whenStable().then(() => {
      expect(component.message).toBe('Error fetching rates');
    });
  });

  it('should call loadRates and populate rates', () => {
    const mockData = [
      { id: 1, currency: 'USD', rate: 4, date: '2026-01-01' }
    ];
    mockCurrencyService.getRatesByDate.and.returnValue(of(mockData));

    component.selectedDate = '2026-01-01';
    component.loadRates();

    expect(mockCurrencyService.getRatesByDate).toHaveBeenCalledWith('2026-01-01');
    fixture.whenStable().then(() => {
      expect(component.rates.length).toBe(1);
      expect(component.rates[0].currency).toBe('USD');
      expect(component.message).toBe('');
    });
  });

  it('should handle loadRates when no date is selected', () => {
    component.selectedDate = '';
    component.loadRates();
    expect(mockCurrencyService.getRatesByDate).not.toHaveBeenCalled();
  });

  it('should handle loadRates error', () => {
    mockCurrencyService.getRatesByDate.and.returnValue(throwError(() => new Error('API error')));
    component.selectedDate = '2026-01-01';
    component.loadRates();

    fixture.whenStable().then(() => {
      expect(component.rates.length).toBe(0);
      expect(component.message).toBe('No data for selected date');
    });
  });
});
