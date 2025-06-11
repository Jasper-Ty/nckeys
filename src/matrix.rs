use std::collections::{HashMap, HashSet};
use std::hash::Hash;
use std::ops::Mul;

#[derive(Debug)]
struct Matrix<R, C> 
where 
    R: Clone + Hash + Eq,
    C: Clone + Hash + Eq,
{
    data: HashMap<(R, C), usize>,
    rows: Vec<R>,
    cols: Vec<C>
}
impl<R, C> Matrix<R, C> 
where 
    R: Clone + Hash + Eq,
    C: Clone + Hash + Eq,
{
    pub fn new(rows: Vec<R>, cols: Vec<C>) -> Self {
        let mut data = HashMap::new();
        for row in &rows {
            for col in &cols {
                data.insert((row.clone(), col.clone()), 0);
            }
        }
        Self {
            data,
            rows,
            cols
        }
    }

    pub fn get(&self, row: &R, col: &C) -> Option<&usize> {
        self.data.get(&(row.clone(), col.clone()))
    }

    pub fn get_mut(&mut self, row: &R, col: &C) -> Option<&mut usize> {
        self.data.get_mut(&(row.clone(), col.clone()))
    }

    pub fn rows(&self) -> &[R] {
        &self.rows
    }

    pub fn cols(&self) -> &[C] {
        &self.cols
    }
}

fn matmul<I, K, J> (a: &Matrix<I, K>, b: &Matrix<K, J>) -> Matrix<I, J>
where
    I: Clone + Hash + Eq,
    J: Clone + Hash + Eq,
    K: Clone + Hash + Eq
{
    if a.cols() != b.rows() {
        panic!("Multiplying incompatible matrices!")
    }
    let mut c = Matrix::new(a.rows.clone(), b.cols.clone());

    for i in a.rows() {
        for j in b.cols() {
            let c_ij = c.get_mut(i, j).unwrap();
            for k in a.cols() {
                let a_ik = a.get(i, k).cloned().unwrap_or_default();
                let b_kj = b.get(k, j).cloned().unwrap_or_default();
                *c_ij += a_ik * b_kj;
            }
        }
    }

    c   
}

impl <A,B,C> std::ops::Mul<&Matrix<B,C>> for &Matrix<A,B>
where
    A: Clone + Hash + Eq,
    B: Clone + Hash + Eq,
    C: Clone + Hash + Eq,
{
    type Output = Matrix<A,C>;

    fn mul(self, rhs: &Matrix<B,C>) -> Self::Output {
        matmul(self, rhs)
    }
}
impl <A,B,C> std::ops::Mul<Matrix<B,C>> for &Matrix<A,B>
where
    A: Clone + Hash + Eq,
    B: Clone + Hash + Eq,
    C: Clone + Hash + Eq,
{
    type Output = Matrix<A,C>;

    fn mul(self, rhs: Matrix<B,C>) -> Self::Output {
        matmul(self, &rhs)
    }
}
impl <A,B,C> std::ops::Mul<&Matrix<B,C>> for Matrix<A,B>
where
    A: Clone + Hash + Eq,
    B: Clone + Hash + Eq,
    C: Clone + Hash + Eq,
{
    type Output = Matrix<A,C>;

    fn mul(self, rhs: &Matrix<B,C>) -> Self::Output {
        matmul(&self, rhs)
    }
}
impl <A,B,C> std::ops::Mul<Matrix<B,C>> for Matrix<A,B>
where
    A: Clone + Hash + Eq,
    B: Clone + Hash + Eq,
    C: Clone + Hash + Eq,
{
    type Output = Matrix<A,C>;

    fn mul(self, rhs: Matrix<B,C>) -> Self::Output {
        matmul(&self, &rhs)
    }
}

