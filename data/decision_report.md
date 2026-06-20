# Decision Report

- generated_at: 2026-06-20T19:51:55.199635+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7271**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7271, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.10% | **+0.41%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +1.11% | **+0.39%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$101.45** / 初期 $100.00 (+1.45%)
- 確定トレード: 24件 (TP 9 / SL 15 / EXP 0)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$237.44** / 初期 $100.00 (+137.44%)
- 確定: 2000件 (Win 590 / Loss 652 / Flat 758) / skip 1832件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALICE/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $237.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 372件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T19:51:50.554416+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.20% price=63905.3
- Funnel: target 796 → liquid 136 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +47.84% | $43,457,633.97 |
| BTW/USDT:USDT | +20.74% | $66,827,999.70 |
| ALICE/USDT:USDT | +15.48% | $1,431,139.98 |
| VELVET/USDT:USDT | +12.02% | $17,448,147.48 |
| LAB/USDT:USDT | +6.14% | $26,773,655.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RE/USDT:USDT | below_1h_threshold | +2.35% | +2.15% |
| LAB/USDT:USDT | below_1h_threshold | +1.56% | +1.36% |
| BTW/USDT:USDT | below_1h_threshold | +1.25% | +1.05% |
| RIF/USDT:USDT | below_1h_threshold | +0.75% | +0.55% |
| RIVER/USDT:USDT | below_1h_threshold | +0.60% | +0.40% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
