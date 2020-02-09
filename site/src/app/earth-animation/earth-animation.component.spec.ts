import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EarthAnimationComponent } from './earth-animation.component';

describe('EarthAnimationComponent', () => {
  let component: EarthAnimationComponent;
  let fixture: ComponentFixture<EarthAnimationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EarthAnimationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EarthAnimationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
