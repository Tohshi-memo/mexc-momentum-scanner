# Decision Report

- generated_at: 2026-05-03T12:47:06.486923+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3066**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3066, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.33% | **+0.26%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -1.12% | **-0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.97% | **+1.63%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +3.29% | **+1.48%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.85% | **+1.28%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T12:47:04.495871+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=78734.1
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +44.86% | $3,056,658.03 |
| BABY/USDT:USDT | +33.69% | $19,622,476.75 |
| FHE/USDT:USDT | +27.45% | $3,952,357.17 |
| AIGENSYN/USDT:USDT | +26.59% | $4,603,344.01 |
| TAC/USDT:USDT | +24.82% | $2,226,882.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +4.66% | +4.51% |
| BSB/USDT:USDT | below_1h_threshold | +3.22% | +3.08% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.78% | +2.64% |
| TST/USDT:USDT | below_1h_threshold | +2.67% | +2.52% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.55% | +2.40% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
