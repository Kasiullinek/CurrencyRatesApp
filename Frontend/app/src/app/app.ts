import { Component } from '@angular/core';
import { CurrencyTableComponent } from './components/currency-table/currency-table.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CurrencyTableComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class AppComponent {}
