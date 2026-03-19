// types.ts
import { Action, Reducer } from 'redux';

// Action Types
export enum ActionTypes {
  UPDATE_FOO = 'UPDATE_FOO',
  UPDATE_BAR = 'UPDATE_BAR',
}

// Action Creators
export interface UpdateFooAction extends Action<ActionTypes.UPDATE_FOO> {
  type: ActionTypes.UPDATE_FOO;
  foo: string;
}

export interface UpdateBarAction extends Action<ActionTypes.UPDATE_BAR> {
  type: ActionTypes.UPDATE_BAR;
  bar: string;
}

export type Actions =
  | UpdateFooAction
  | UpdateBarAction;

// State Types
export interface FooState {
  foo: string;
}

export interface BarState {
  bar: string;
}

export interface RootState {
  foo: FooState;
  bar: BarState;
}

// Reducer Types
export type Reducer<T> = (state: T, action: Actions) => T;