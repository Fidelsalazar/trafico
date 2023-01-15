import { Component } from '@angular/core';
import * as L from 'leaflet';
import { marker, tileLayer } from 'leaflet';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'mapa2';

  ngAfterViewInit(): void{

    const map = L.map('map').setView([ -22.9035, -43.2096], 13);

    const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
	    maxZoom: 20,
	    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var marker = L.marker([-22.9035, -43.2096]).addTo(map);

  }
}
