use std::collections::HashMap;
use std::hash::Hash;
use std::ops::{Index, IndexMut, Mul};

#[derive(Debug)]
pub struct Matrix<R, C> 
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

    pub fn nrows(&self) -> usize {
        self.rows.len()
    }

    pub fn ncols(&self) -> usize {
        self.cols.len()
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

impl <A,B,C> Mul<&Matrix<B,C>> for &Matrix<A,B>
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
impl <A,B,C> Mul<Matrix<B,C>> for &Matrix<A,B>
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
impl <A,B,C> Mul<&Matrix<B,C>> for Matrix<A,B>
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
impl <A,B,C> Mul<Matrix<B,C>> for Matrix<A,B>
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

impl <R, C> Index<(R, C)> for Matrix<R, C> 
where
    R: Clone + Hash + Eq,
    C: Clone + Hash + Eq,
{
    type Output = usize;

    fn index(&self, (row, col): (R, C)) -> &Self::Output {
        self.get(&row, &col).expect("Value at index does not exist")
    }
}

impl <R, C> Index<(&R, &C)> for Matrix<R, C> 
where
    R: Clone + Hash + Eq,
    C: Clone + Hash + Eq,
{
    type Output = usize;

    fn index(&self, (row, col): (&R, &C)) -> &Self::Output {
        self.get(row, col).expect("Value at index does not exist")
    }
}

impl <R, C> IndexMut<(R, C)> for Matrix<R, C> 
where
    R: Clone + Hash + Eq,
    C: Clone + Hash + Eq,
{
    fn index_mut(&mut self, (row, col): (R, C)) -> &mut Self::Output {
        self.get_mut(&row, &col).expect("Value at index does not exist")
    }
}

impl <R, C> IndexMut<(&R, &C)> for Matrix<R, C> 
where
    R: Clone + Hash + Eq,
    C: Clone + Hash + Eq,
{
    fn index_mut(&mut self, (row, col): (&R, &C)) -> &mut Self::Output {
        self.get_mut(row, col).expect("Value at index does not exist")
    }
}

use std::fmt;
use tabled::{builder::Builder, settings::Style};


impl <R, C> fmt::Display for Matrix<R, C> 
where
    R: Clone + Hash + Eq + fmt::Display,
    C: Clone + Hash + Eq + fmt::Display,
{
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let m = self.nrows();
        let n = self.ncols();
        
        let mut builder = Builder::default();
        
        // Matrix contents
        for row in self.rows.iter() {
            let record = self.cols.iter().map(|col| self[(row,col)].to_string());
            builder.push_record(record);
        }
        
        builder.insert_record(0, self.cols.iter().map(|col| col.to_string()));
        builder.insert_column(0, 
            std::iter::once(String::new())
            .chain(self.rows.iter().map(|row| row.to_string()))
        );
        
        let mut table = builder.build();
        table.with(Style::rounded());

        write!(f, "{}", table)
    }
}

