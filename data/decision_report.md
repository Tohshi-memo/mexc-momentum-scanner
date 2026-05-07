# Decision Report

- generated_at: 2026-05-07T03:07:41.450675+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3542**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3542, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_8PCT | 5/20 | 25.0% | +4.74% | **+1.19%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_6PCT | 10/20 | 50.0% | +1.34% | **+0.67%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +4.66% | **+2.56%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK_LONG | 20/20 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$102.77** / 初期 $100.00 (+2.77%)
- 確定: 37件 (Win 12 / Loss 14 / Flat 11) / skip 66件
- 成長率目線: 平均log +0.000737 / 幾何平均 +0.074% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $102.77

## 4. Latest Market Context

- 更新: 2026-05-07T03:07:38.881005+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=81001.7
- Funnel: target 770 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +229.67% | $1,242,156.81 |
| DOGS/USDT:USDT | +77.01% | $8,495,273.84 |
| FHE/USDT:USDT | +38.44% | $15,864,117.47 |
| PENGUIN/USDT:USDT | +32.17% | $1,155,251.56 |
| NOT/USDT:USDT | +16.92% | $5,642,242.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +3.37% | +3.46% |
| SATO/USDT:USDT | below_1h_threshold | +1.75% | +1.85% |
| ORCA/USDT:USDT | below_1h_threshold | +1.20% | +1.29% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.95% | +1.05% |
| BLESS/USDT:USDT | below_1h_threshold | +0.69% | +0.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
