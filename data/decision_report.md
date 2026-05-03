# Decision Report

- generated_at: 2026-05-03T09:07:32.719610+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3057**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3057, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-2.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.18% | **-2.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.54% | **+0.38%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 18/20 | 90.0% | -0.45% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +4.66% | **+2.56%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +4.34% | **+2.38%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.30% | **+1.72%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.65% | **+1.09%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T09:07:30.927310+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=78368.2
- Funnel: target 755 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +65.80% | $12,501,373.48 |
| BR/USDT:USDT | +26.05% | $3,854,834.06 |
| B/USDT:USDT | +23.56% | $41,700,039.67 |
| TAC/USDT:USDT | +20.78% | $2,735,544.09 |
| FHE/USDT:USDT | +18.97% | $2,904,694.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XMR/USDT:USDT | below_1h_threshold | +0.62% | +0.59% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +0.44% | +0.41% |
| TAC/USDT:USDT | below_1h_threshold | +0.40% | +0.37% |
| ZEC/USDT:USDT | below_1h_threshold | +0.40% | +0.37% |
| ALCH/USDT:USDT | below_1h_threshold | +0.36% | +0.33% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
