import { ɵangular_packages_common_http_http_h } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
// import { HttpService } from '../services/httpclient.service'
interface Food {
  value: string;
  viewValue: string;
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  selected: any;
  trackingno: any;
  constructor(){}
  checkStatus()
  {
   

  }

  ngOnInit()
  {

  }
}
