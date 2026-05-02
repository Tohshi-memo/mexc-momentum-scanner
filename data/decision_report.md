# Decision Report

- generated_at: 2026-05-02T00:05:46.058257+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2846**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2846, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.69% | **-0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.25% | **+0.67%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.41% | **+1.57%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.50% | **+1.37%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.89% | **+1.30%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.66% | **+1.24%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +3.58% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T00:05:44.336599+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=78217.0
- Funnel: target 755 → liquid 183 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +71.07% | $18,026,684.97 |
| CHILLGUY/USDT:USDT | +15.41% | $1,066,850.21 |
| FIGHT/USDT:USDT | +10.18% | $1,270,499.94 |
| RLS/USDT:USDT | +10.13% | $2,521,932.16 |
| WOJAK/USDT:USDT | +9.83% | $1,077,065.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RLS/USDT:USDT | below_1h_threshold | +2.11% | +2.08% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.55% | +1.52% |
| AXS/USDT:USDT | below_1h_threshold | +1.29% | +1.26% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.06% | +1.03% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.82% | +0.79% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
