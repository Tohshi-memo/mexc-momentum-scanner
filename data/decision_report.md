# Decision Report

- generated_at: 2026-08-17T01:46:32.164728+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11783**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.12% / filled 20/20。**
- 全期間 MARKET基準: n=11783, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.12% | **+3.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.12% | **+3.12%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.91% | **+2.62%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.03% | **+1.42%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.71% | **+0.94%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.15% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.38% | **-0.21%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.73% | **-0.40%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -1.55% | **-0.85%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 185件 (TP 71 / SL 109 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4184件 (Win 1292 / Loss 1363 / Flat 1529) / skip 4160件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.35** / 初期 $100.00 (+54.35%)
- 確定: 1791件 (Win 497 / Loss 419 / Flat 875) / skip 3403件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0425 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $154.35

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.37** / 初期 $100.00 (+18.37%)
- 確定: 1672件 (Win 503 / Loss 635 / Flat 534) / pending 0件 / skip 1582件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000351 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GPS/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $118.37

## 6. Latest Market Context

- 更新: 2026-08-17T01:46:22.993477+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.45% price=63174.0
- Funnel: target 986 → liquid 151 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.6 >= 65=1, 4h RSI 83.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +21.87% | $14,247,801.02 |
| BTW/USDT:USDT | +20.08% | $30,065,385.68 |
| GPS/USDT:USDT | +13.15% | $1,863,687.11 |
| ONG/USDT:USDT | +12.26% | $1,355,958.02 |
| US/USDT:USDT | +12.10% | $1,807,655.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +3.15% | +2.70% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +3.11% | +2.66% |
| SNXX/USDT:USDT | below_1h_threshold | +2.24% | +1.78% |
| US/USDT:USDT | below_1h_threshold | +2.22% | +1.76% |
| AKE/USDT:USDT | below_1h_threshold | +2.00% | +1.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
