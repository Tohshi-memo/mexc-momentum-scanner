# Decision Report

- generated_at: 2026-05-11T12:23:08.472783+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4029**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4029, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.33% | **-1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 18/20 | 90.0% | +1.14% | **+1.03%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.63% | **+0.44%** |
| LIMIT_FIB1272 | 14/20 | 70.0% | +0.17% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.33% | **+1.05%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.19% | **+0.99%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.59% | **+0.95%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.21% | **+0.88%** |
| LIMIT_BB3S_LONG | 8/8 | 100.0% | +0.70% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 372件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T12:23:05.459114+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=81112.8
- Funnel: target 762 → liquid 183 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +39.32% | $13,792,241.75 |
| PENGUIN/USDT:USDT | +38.42% | $1,335,184.08 |
| B/USDT:USDT | +31.37% | $11,496,217.66 |
| SAGA/USDT:USDT | +29.88% | $3,341,254.23 |
| TROLLSOL/USDT:USDT | +20.52% | $4,440,532.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGUIN/USDT:USDT | below_1h_threshold | +4.18% | +4.25% |
| TRUTH/USDT:USDT | below_1h_threshold | +3.62% | +3.68% |
| UB/USDT:USDT | below_1h_threshold | +2.49% | +2.56% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.84% | +1.90% |
| OPG/USDT:USDT | below_1h_threshold | +1.62% | +1.68% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
