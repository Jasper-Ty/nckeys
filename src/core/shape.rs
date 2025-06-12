use super::subsets;
use super::word::Word;
use super::matrix::Matrix;

/// A shape is defined to be a subset of ℕ × ℕ
#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct Shape(Vec<(usize,usize)>);

impl From<Vec<(usize,usize)>> for Shape {
    fn from(value: Vec<(usize,usize)>) -> Self {
        Self(value)
    }
}

impl Shape {
    pub fn bounding_box(&self) -> (usize, usize) {
        let mut i_max = 0;
        let mut j_max = 0;
        for (i, j) in self.0.iter().cloned() {
            if i > i_max {
                i_max = i;
            }
            if j > j_max {
                j_max = j;
            }
        }
        (i_max + 1, j_max + 1)
    }

    /// Returns a list of biwords
    pub fn biwords(&self, deg: usize) -> Vec<(Word, Word)> {
        subsets(self.0.len(), deg)
            .into_iter()
            .map(|subset| subset.into_iter().map(|i| self.0[i]).unzip())
            .map(|(l, r): (Vec<usize>, Vec<usize>)| (Word::from(l), Word::from(r)))
            .collect()
    }

    /// 
    pub fn word_matrix(&self, deg: usize) -> Matrix<Word, Word> {
        let (i_max, j_max) = self.bounding_box();

        let rows = Word::words_of_deg(deg, i_max);
        let cols = Word::words_of_deg(deg, j_max);
        
        let mut m = Matrix::new(rows, cols);

        for (left, right) in self.biwords(deg) {
            m[(left, right)] += 1;
        }
       
        m
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn biwords_triangle_0() {
        let triangle = Shape(vec![]);
        assert_eq!(triangle.biwords(0), vec![(word![], word![])]);
        assert_eq!(triangle.biwords(1), vec![]);
    }

    #[test]
    fn biwords_triangle_1() {
        let triangle = Shape(vec![(0,0)]);
        assert_eq!(triangle.biwords(0), vec![(word![], word![])]);
        assert_eq!(
            triangle.biwords(1), 
            vec![(word![0], word![0])]
        );
        assert_eq!(triangle.biwords(2), vec![]);
    }

    #[test]
    fn biwords_triangle_2() {
        let triangle = Shape(vec![(0,0), (1,0), (0,1)]);
        assert_eq!(triangle.biwords(0), vec![(word![], word![])]);
        assert_eq!(
            triangle.biwords(1), 
            vec![(word![0], word![0]), (word![1], word![0]), (word![0], word![1])]
        );
        assert_eq!(
            triangle.biwords(2), 
            vec![(word![0,1], word![0,0]), (word![0,0], word![0,1]), (word![1,0], word![0,1])]
        );
        assert_eq!(triangle.biwords(3), vec![(word![0,1,0], word![0,0,1])]);
        assert_eq!(triangle.biwords(4), vec![]);
    }

    #[test]
    fn biwords_triangle_3() {
        let triangle = Shape(
            vec![
                (0,0), (1,0), (2,0),
                (1,0), (1,1),
                (2,0)
            ]
        );
        assert_eq!(triangle.biwords(0), vec![(word![], word![])]);
        assert_eq!(
            triangle.biwords(1), 
            vec![
                (word![0], word![0]), (word![1], word![0]), (word![2], word![0]),
                (word![1], word![0]), (word![1], word![1]),
                (word![2], word![0]),
            ]
        );
    }
}

