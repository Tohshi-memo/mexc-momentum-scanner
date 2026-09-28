# Decision Report

- generated_at: 2026-09-28T07:41:22.786552+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15700**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.34% / filled 20/20。**
- 全期間 MARKET基準: n=15700, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.30% | **+1.17%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.83% | **+0.66%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.88% | **+0.48%** |
| LIMIT_BB3S | 3/17 | 17.6% | +2.05% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.07% | **+0.03%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.02% | **+0.01%** |
| MARKET_LONG | 20/20 | 100.0% | -0.28% | **-0.28%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.75% | **-0.35%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,233.41** / 初期 $100.00 (+1133.41%)
- 確定: 5982件 (Win 1766 / Loss 1924 / Flat 2292) / skip 6279件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,233.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5577件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 3269件 (Win 952 / Loss 1285 / Flat 1032) / pending 2件 / skip 3898件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000133 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONDO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-09-28T07:41:11.330670+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=82909.4
- Funnel: target 1059 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +52.71% | $274,533,974.76 |
| BATON/USDT:USDT | +27.23% | $1,359,331.64 |
| BTW/USDT:USDT | +22.45% | $8,796,366.86 |
| ONE/USDT:USDT | +15.02% | $5,670,893.15 |
| GRT/USDT:USDT | +14.09% | $10,990,533.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.37% | +4.63% |
| GRAM/USDT:USDT | below_1h_threshold | +1.43% | +1.69% |
| MONAD/USDT:USDT | below_1h_threshold | +1.11% | +1.37% |
| NICKEL/USDT:USDT | below_1h_threshold | +0.45% | +0.71% |
| HBAR/USDT:USDT | below_1h_threshold | +0.29% | +0.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
