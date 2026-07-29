# Decision Report

- generated_at: 2026-07-29T12:46:23.273614+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9792**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=9792, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.33% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.35% | **+0.68%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.21% | **+0.67%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.67% | **+0.37%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.55% | **+0.36%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$119.27** / 初期 $100.00 (+19.27%)
- 確定トレード: 162件 (TP 63 / SL 94 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $119.27
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2834件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1227件 (Win 338 / Loss 275 / Flat 614) / skip 1976件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0289 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.78** / 初期 $100.00 (+9.78%)
- 確定: 762件 (Win 246 / Loss 293 / Flat 223) / pending 3件 / skip 503件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000452 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $109.78

## 6. Latest Market Context

- 更新: 2026-07-29T12:46:14.638548+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=64305.7
- Funnel: target 907 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +142.51% | $3,594,582.47 |
| BEAT/USDT:USDT | +24.06% | $44,266,562.98 |
| UAI/USDT:USDT | +24.03% | $2,520,471.50 |
| RIF/USDT:USDT | +14.49% | $3,258,158.84 |
| AEON1/USDT:USDT | +13.82% | $2,232,566.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +4.98% | +5.25% |
| ON/USDT:USDT | below_1h_threshold | +4.54% | +4.81% |
| COTI/USDT:USDT | below_1h_threshold | +2.03% | +2.30% |
| EUL/USDT:USDT | below_1h_threshold | +1.68% | +1.95% |
| GGLL/USDT:USDT | below_1h_threshold | +1.00% | +1.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
