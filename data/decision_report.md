# Decision Report

- generated_at: 2026-09-09T00:31:30.765632+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14023**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.23% / filled 20/20。**
- 全期間 MARKET基準: n=14023, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.67% | **+1.26%** |
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.93% | **+0.83%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.80% | **+0.64%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.82% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | -0.09% | **-0.06%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.21% | **-0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,013.58** / 初期 $100.00 (+913.58%)
- 確定: 5287件 (Win 1588 / Loss 1707 / Flat 1992) / skip 5297件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,013.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.66** / 初期 $100.00 (+90.66%)
- 確定: 2626件 (Win 726 / Loss 622 / Flat 1278) / skip 4808件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0472 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $190.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.49** / 初期 $100.00 (+19.49%)
- 確定: 2605件 (Win 763 / Loss 990 / Flat 852) / pending 4件 / skip 2887件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000378 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BNCSTOCK/USDT:USDT `MARKET` EXPIRED account +0.02% 残高後 $119.49

## 6. Latest Market Context

- 更新: 2026-09-09T00:31:19.741766+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=78591.5
- Funnel: target 1070 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.8 >= 65=1, 4h RSI 72.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OL/USDT:USDT | +38.37% | $1,562,716.90 |
| ARX/USDT:USDT | +12.67% | $1,296,856.66 |
| WAVES/USDT:USDT | +11.17% | $1,095,987.24 |
| EGLD/USDT:USDT | +9.26% | $2,148,661.14 |
| RAY/USDT:USDT | +8.49% | $3,023,364.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| G/USDT:USDT | below_1h_threshold | +3.98% | +3.77% |
| FORM/USDT:USDT | below_1h_threshold | +2.88% | +2.67% |
| ARX/USDT:USDT | below_1h_threshold | +2.88% | +2.67% |
| SOFTBANKSTOCK/USDT:USDT | below_1h_threshold | +2.87% | +2.67% |
| ETC/USDT:USDT | below_1h_threshold | +1.96% | +1.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
