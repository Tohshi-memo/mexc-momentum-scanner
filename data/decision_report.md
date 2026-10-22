# Decision Report

- generated_at: 2026-10-22T06:46:33.751761+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17119**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=17119, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.40% | **+0.34%** |
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.33% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.87% | **+0.61%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.45% | **+0.32%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.54% | **+0.27%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.85% | **+0.25%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,343.71** / 初期 $100.00 (+1243.71%)
- 確定: 6501件 (Win 1891 / Loss 2074 / Flat 2536) / skip 7179件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,343.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.30** / 初期 $100.00 (+178.30%)
- 確定: 3829件 (Win 1052 / Loss 896 / Flat 1881) / skip 6701件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $278.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5281件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000219 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-22T06:46:14.512371+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=82483.9
- Funnel: target 1090 → liquid 188 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PTB/USDT:USDT | +37.42% | $1,209,755.04 |
| BTW/USDT:USDT | +18.95% | $32,178,331.36 |
| PHA/USDT:USDT | +17.62% | $4,835,607.83 |
| SOXS/USDT:USDT | +10.38% | $11,057,905.84 |
| MAGMA/USDT:USDT | +9.64% | $1,594,567.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHA/USDT:USDT | below_1h_threshold | +4.31% | +4.67% |
| RUNE/USDT:USDT | below_1h_threshold | +4.15% | +4.51% |
| BTW/USDT:USDT | below_1h_threshold | +2.85% | +3.21% |
| NIL/USDT:USDT | below_1h_threshold | +1.64% | +2.00% |
| SOXS/USDT:USDT | below_1h_threshold | +1.15% | +1.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
