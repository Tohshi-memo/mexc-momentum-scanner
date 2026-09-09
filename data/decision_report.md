# Decision Report

- generated_at: 2026-09-09T00:41:24.652248+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14024**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.23% / filled 20/20。**
- 全期間 MARKET基準: n=14024, expectancy=-0.00%
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
| LIMIT_ATR | 13/20 | 65.0% | +0.86% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.21% | **-0.11%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | -0.29% | **-0.23%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,013.58** / 初期 $100.00 (+913.58%)
- 確定: 5288件 (Win 1588 / Loss 1707 / Flat 1993) / skip 5297件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: WAVES/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,013.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.66** / 初期 $100.00 (+90.66%)
- 確定: 2627件 (Win 726 / Loss 622 / Flat 1279) / skip 4808件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0470 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: WAVES/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $190.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 2606件 (Win 763 / Loss 991 / Flat 852) / pending 4件 / skip 2887件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000120 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: WAVES/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-09-09T00:41:14.036908+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=78622.9
- Funnel: target 1070 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1, 4h RSI 74.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OL/USDT:USDT | +33.84% | $1,647,518.49 |
| WAVES/USDT:USDT | +19.27% | $1,146,684.51 |
| ARX/USDT:USDT | +10.23% | $1,311,636.80 |
| EGLD/USDT:USDT | +9.62% | $2,181,117.01 |
| RAY/USDT:USDT | +7.42% | $3,029,863.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOFTBANKSTOCK/USDT:USDT | below_1h_threshold | +2.87% | +2.63% |
| ETC/USDT:USDT | below_1h_threshold | +2.09% | +1.84% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.88% | +1.63% |
| JUP/USDT:USDT | below_1h_threshold | +1.83% | +1.58% |
| INJ/USDT:USDT | below_1h_threshold | +1.72% | +1.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
