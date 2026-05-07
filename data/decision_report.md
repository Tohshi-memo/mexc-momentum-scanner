# Decision Report

- generated_at: 2026-05-07T08:02:46.697080+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3595**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3595, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +5.43% | **+1.63%** |
| LIMIT_8PCT | 7/20 | 35.0% | +3.83% | **+1.34%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.86% | **+0.30%** |
| LIMIT_BB3S | 10/19 | 52.6% | +0.31% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.05% | **+1.53%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.47% | **+0.99%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.85** / 初期 $100.00 (+6.85%)
- 確定: 89件 (Win 31 / Loss 35 / Flat 23) / skip 67件
- 成長率目線: 平均log +0.000744 / 幾何平均 +0.074% per trade / maxDD +2.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $106.85

## 4. Latest Market Context

- 更新: 2026-05-07T08:02:43.705529+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=81500.0
- Funnel: target 771 → liquid 189 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +202.05% | $1,960,733.07 |
| PENGUIN/USDT:USDT | +126.41% | $1,962,707.85 |
| B3/USDT:USDT | +81.23% | $10,179,583.47 |
| D/USDT:USDT | +68.58% | $1,044,012.85 |
| DOGS/USDT:USDT | +66.75% | $12,913,530.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +3.40% | +3.38% |
| SIREN/USDT:USDT | below_1h_threshold | +1.38% | +1.36% |
| IO/USDT:USDT | below_1h_threshold | +1.08% | +1.05% |
| NIL/USDT:USDT | below_1h_threshold | +0.92% | +0.89% |
| B/USDT:USDT | below_1h_threshold | +0.82% | +0.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
