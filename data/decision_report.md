# Decision Report

- generated_at: 2026-05-03T13:27:21.504825+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3069**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3069, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.48% | **-1.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 17/20 | 85.0% | +0.86% | **+0.73%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_BB3S | 11/17 | 64.7% | +0.40% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.66% | **+1.83%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +4.20% | **+1.68%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.71% | **+1.48%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +2.55% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T13:27:19.254723+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=78623.8
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +38.34% | $3,610,305.11 |
| TAC/USDT:USDT | +33.43% | $2,405,697.50 |
| AIGENSYN/USDT:USDT | +30.41% | $4,779,865.93 |
| NAORIS/USDT:USDT | +27.29% | $4,023,734.28 |
| FHE/USDT:USDT | +25.00% | $4,113,230.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +3.70% | +3.82% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +3.25% | +3.37% |
| B/USDT:USDT | below_1h_threshold | +3.05% | +3.16% |
| AKT/USDT:USDT | below_1h_threshold | +2.28% | +2.39% |
| BSB/USDT:USDT | below_1h_threshold | +2.23% | +2.35% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
