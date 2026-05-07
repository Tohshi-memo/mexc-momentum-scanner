# Decision Report

- generated_at: 2026-05-07T06:07:38.844008+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3577**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3577, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.10% | **+1.10%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.87% | **+0.78%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_BB3S | 4/17 | 23.5% | +0.50% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.55% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.29% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.17** / 初期 $100.00 (+6.17%)
- 確定: 71件 (Win 26 / Loss 28 / Flat 17) / skip 67件
- 成長率目線: 平均log +0.000843 / 幾何平均 +0.084% per trade / maxDD +2.48%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $106.17

## 4. Latest Market Context

- 更新: 2026-05-07T06:07:35.298878+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=81008.4
- Funnel: target 770 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +238.07% | $1,737,746.48 |
| B3/USDT:USDT | +105.54% | $9,480,889.27 |
| DOGS/USDT:USDT | +71.74% | $11,880,232.35 |
| PENGUIN/USDT:USDT | +47.85% | $1,395,670.38 |
| FHE/USDT:USDT | +24.27% | $16,737,948.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B3/USDT:USDT | below_1h_threshold | +3.22% | +3.27% |
| SATO/USDT:USDT | below_1h_threshold | +3.12% | +3.17% |
| IO/USDT:USDT | below_1h_threshold | +2.90% | +2.95% |
| BILL/USDT:USDT | below_1h_threshold | +1.01% | +1.05% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.53% | +0.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
