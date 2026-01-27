import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { CurrencyService } from './currency.service';
import { CurrencyRate } from '../models/currency-rate.model';

describe('CurrencyService', () => {
  let service: CurrencyService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [CurrencyService],
    });

    service = TestBed.inject(CurrencyService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  describe('fetchRates', () => {
    it('should send POST request to /currencies/fetch and return a message', () => {
      const mockResponse = { message: 'Rates fetched successfully' };

      service.fetchRates().subscribe((response) => {
        expect(response).toEqual(mockResponse);
      });

      const req = httpMock.expectOne('http://localhost:8000/currencies/fetch');
      expect(req.request.method).toBe('POST');
      expect(req.request.body).toEqual({});
      req.flush(mockResponse);
    });
  });

  describe('getRatesByDate', () => {
    it('should send GET request to /currencies/<date> and return CurrencyRate array', () => {
      const mockDate = '2026-01-27';
      const mockRates: CurrencyRate[] = [
        { id: 1, currency: 'USD', rate: 4.12, date: mockDate },
        { id: 2, currency: 'EUR', rate: 4.55, date: mockDate },
      ];

      service.getRatesByDate(mockDate).subscribe((rates) => {
        expect(rates.length).toBe(2);
        expect(rates).toEqual(mockRates);
      });

      const req = httpMock.expectOne(`http://localhost:8000/currencies/${mockDate}`);
      expect(req.request.method).toBe('GET');
      req.flush(mockRates);
    });
  });
});
