# Decision Report

- generated_at: 2026-05-03T17:52:53.583281+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3093**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3093, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.85% | **-0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/17 | 23.5% | +3.70% | **+0.87%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.89% | **+0.85%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.79% | **+1.95%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.20% | **+1.76%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.64% | **+1.45%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.09% | **+1.39%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T17:52:44.994795+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=78717.0
- Funnel: target 755 → liquid 164 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +31.82% | $316,645,334.68 |
| SKYAI/USDT:USDT | +18.76% | $24,232,553.70 |
| TST/USDT:USDT | +11.43% | $5,312,148.90 |
| MERL/USDT:USDT | +6.63% | $1,002,152.86 |
| ASTEROID/USDT:USDT | +5.05% | $2,083,450.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +4.34% | +4.21% |
| UB/USDT:USDT | below_1h_threshold | +3.91% | +3.79% |
| ORDI/USDT:USDT | below_1h_threshold | +3.74% | +3.62% |
| TRADOOR/USDT:USDT | below_1h_threshold | +3.56% | +3.44% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.15% | +3.03% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
