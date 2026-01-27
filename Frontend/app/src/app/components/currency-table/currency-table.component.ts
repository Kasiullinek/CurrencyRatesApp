import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CurrencyService } from '../../services/currency.service';
import { CurrencyRate } from '../../models/currency-rate.model';

@Component({
  selector: 'app-currency-table',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './currency-table.component.html'
})
export class CurrencyTableComponent {

  selectedDate = '';
  rates: CurrencyRate[] = [];
  message = '';

  constructor(private currencyService: CurrencyService) {}

  fetchRates(): void {
    this.currencyService.fetchRates().subscribe({
      next: res => this.message = res.message,
      error: () => this.message = 'Error fetching rates'
    });
  }

  loadRates(): void {
    if (!this.selectedDate) return;

    this.currencyService.getRatesByDate(this.selectedDate)
      .subscribe({
        next: data => this.rates = data,
        error: () => {
          this.message = 'No data for selected date';
          this.rates = [];
        }
      });
  }
}
