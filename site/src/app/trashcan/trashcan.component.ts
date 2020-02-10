import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-trashcan',
  templateUrl: './trashcan.component.html',
  styleUrls: ['./trashcan.component.css']
})
export class TrashcanComponent implements OnInit {

  constructor() { }

  @Input() text="Trash";

  ngOnInit(): void {
  }

}
