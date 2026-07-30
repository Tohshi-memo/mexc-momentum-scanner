# Decision Report

- generated_at: 2026-07-30T01:56:31.298772+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9850**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.16% / filled 20/20。**
- 全期間 MARKET基準: n=9850, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.16% | **+2.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.16% | **+2.16%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.91% | **+1.53%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.76% | **+1.23%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.40% | **+0.70%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.82% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.35% | **-0.19%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |
| MARKET_LONG | 20/20 | 100.0% | -0.49% | **-0.49%** |

## 2. $100 Live Portfolio

- 残高: **$120.45** / 初期 $100.00 (+20.45%)
- 確定トレード: 169件 (TP 66 / SL 98 / EXP 5)
- 最新: TOKYOELSTOCK/USDT:USDT SL_HIT PnL -2.11% 残高後 $120.45
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2892件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 2019件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.01** / 初期 $100.00 (+9.01%)
- 確定: 766件 (Win 246 / Loss 297 / Flat 223) / pending 1件 / skip 561件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000424 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIF/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $109.01

## 6. Latest Market Context

- 更新: 2026-07-30T01:56:23.046979+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.00% price=64311.4
- Funnel: target 911 → liquid 182 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +16.16% | $15,135,140.45 |
| RE/USDT:USDT | +14.84% | $8,144,569.96 |
| ADVANTESTSTOCK/USDT:USDT | +13.54% | $1,561,338.81 |
| MSFU/USDT:USDT | +13.29% | $4,478,863.86 |
| KIOXIASTOCK/USDT:USDT | +13.04% | $1,126,985.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COTI/USDT:USDT | below_relative_strength | +5.98% | +4.98% |
| BANK/USDT:USDT | below_relative_strength | +5.42% | +4.42% |
| ACH/USDT:USDT | below_1h_threshold | +4.53% | +3.53% |
| ANSEM/USDT:USDT | below_1h_threshold | +4.43% | +3.43% |
| AEON1/USDT:USDT | below_1h_threshold | +4.25% | +3.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
