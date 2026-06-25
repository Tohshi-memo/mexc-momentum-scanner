# Decision Report

- generated_at: 2026-06-25T06:43:22.238090+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7531**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7531, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.58% | **-0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/15 | 26.7% | +1.21% | **+0.32%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.00% | **+0.00%** |
| LIMIT_1PCT | 18/20 | 90.0% | -0.20% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +4.13% | **+2.06%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.46% | **+1.90%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.52% | **+1.89%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.97% | **+1.58%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.74% | **+1.48%** |

## 2. $100 Live Portfolio

- 残高: **$102.94** / 初期 $100.00 (+2.94%)
- 確定トレード: 39件 (TP 15 / SL 24 / EXP 0)
- 最新: MUSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$220.34** / 初期 $100.00 (+120.34%)
- 確定: 2131件 (Win 629 / Loss 714 / Flat 788) / skip 1961件
- 成長率目線: 平均log +0.000371 / 幾何平均 +0.037% per trade / maxDD +7.67%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $220.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 350件 (Win 98 / Loss 95 / Flat 157) / skip 592件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-25T06:43:17.296329+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=61713.7
- Funnel: target 807 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +34.14% | $15,122,942.65 |
| RESOLV/USDT:USDT | +18.86% | $2,788,365.47 |
| MUSTOCK/USDT:USDT | +18.66% | $114,605,542.20 |
| KORU/USDT:USDT | +17.64% | $5,468,619.42 |
| ESPORTS/USDT:USDT | +15.37% | $3,060,030.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +2.57% | +2.33% |
| SYN/USDT:USDT | below_1h_threshold | +1.96% | +1.72% |
| AERO/USDT:USDT | below_1h_threshold | +1.58% | +1.34% |
| XPL/USDT:USDT | below_1h_threshold | +1.45% | +1.20% |
| ENA/USDT:USDT | below_1h_threshold | +1.41% | +1.17% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
