# Decision Report

- generated_at: 2026-07-02T09:53:37.011882+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8058**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.40% / filled 20/20。**
- 全期間 MARKET基準: n=8058, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+4.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.40% | **+4.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.40% | **+4.40%** |
| ASK | 20/20 | 100.0% | +4.39% | **+4.39%** |
| LIMIT_1PCT | 11/20 | 55.0% | +1.55% | **+0.85%** |
| LIMIT_2PCT | 9/20 | 45.0% | +0.91% | **+0.41%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +2.36% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +2.16% | **+0.76%** |
| LIMIT_9PCT_LONG | 11/20 | 55.0% | +0.34% | **+0.18%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.46% | **-0.12%** |
| LIMIT_8PCT_LONG | 14/20 | 70.0% | -0.29% | **-0.20%** |
| LIMIT_5PCT_LONG | 17/20 | 85.0% | -1.03% | **-0.87%** |

## 2. $100 Live Portfolio

- 残高: **$103.66** / 初期 $100.00 (+3.66%)
- 確定トレード: 48件 (TP 18 / SL 29 / EXP 1)
- 最新: TLM/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.66
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2175件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 548件 (Win 136 / Loss 131 / Flat 281) / skip 921件
- 成長率目線: 平均log +0.000091 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0465 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BIRB/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T09:53:30.137397+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.21% price=61221.7
- Funnel: target 829 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIRB/USDT:USDT | +76.69% | $5,857,528.12 |
| BREV/USDT:USDT | +42.75% | $3,375,810.59 |
| TAIKO/USDT:USDT | +37.30% | $102,091,857.35 |
| TLM/USDT:USDT | +29.67% | $8,772,847.12 |
| LIT/USDT:USDT | +22.18% | $12,621,232.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MET/USDT:USDT | below_1h_threshold | +4.39% | +3.17% |
| GRAM/USDT:USDT | below_1h_threshold | +4.33% | +3.12% |
| B/USDT:USDT | below_1h_threshold | +4.26% | +3.04% |
| H/USDT:USDT | below_1h_threshold | +3.95% | +2.73% |
| CRV/USDT:USDT | below_1h_threshold | +2.04% | +0.82% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
