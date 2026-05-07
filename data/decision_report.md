# Decision Report

- generated_at: 2026-05-07T10:22:30.297220+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3615**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.38% / filled 20/20。**
- 全期間 MARKET基準: n=3615, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.10% | **+1.99%** |
| MARKET | 20/20 | 100.0% | +1.38% | **+1.38%** |
| ASK | 20/20 | 100.0% | +1.30% | **+1.30%** |
| LIMIT_BB3S | 2/14 | 14.3% | +3.09% | **+0.44%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.80% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.95% | **+0.57%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.86% | **+0.46%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.97% | **+0.44%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.38% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.06** / 初期 $100.00 (+7.06%)
- 確定: 109件 (Win 36 / Loss 44 / Flat 29) / skip 67件
- 成長率目線: 平均log +0.000626 / 幾何平均 +0.063% per trade / maxDD +2.62%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_7PCT_LONG` TP_HIT account +1.00% 残高後 $107.06

## 4. Latest Market Context

- 更新: 2026-05-07T10:22:27.088982+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=80839.0
- Funnel: target 771 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +140.05% | $2,139,931.40 |
| PENGUIN/USDT:USDT | +107.27% | $3,190,763.82 |
| B3/USDT:USDT | +104.99% | $11,158,455.20 |
| DOGS/USDT:USDT | +67.21% | $14,879,104.25 |
| SIREN/USDT:USDT | +43.17% | $12,234,417.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGUIN/USDT:USDT | below_1h_threshold | +3.34% | +3.41% |
| DYDX/USDT:USDT | below_1h_threshold | +3.12% | +3.19% |
| B3/USDT:USDT | below_1h_threshold | +2.73% | +2.79% |
| LAB/USDT:USDT | below_1h_threshold | +2.03% | +2.09% |
| EVAA/USDT:USDT | below_1h_threshold | +1.96% | +2.02% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
