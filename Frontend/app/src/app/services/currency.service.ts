import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CurrencyRate } from '../models/currency-rate.model';

@Injectable({
  providedIn: 'root'
})
export class CurrencyService {

  private apiUrl = 'http://localhost:8000/currencies';

  constructor(private http: HttpClient) {}

  fetchRates(): Observable<{ message: string }> {
    return this.http.post<{ message: string }>(
      `${this.apiUrl}/fetch`,
      {}
    );
  }

  getRatesByDate(date: string): Observable<CurrencyRate[]> {
    return this.http.get<CurrencyRate[]>(
      `${this.apiUrl}/${date}`
    );
  }
}
