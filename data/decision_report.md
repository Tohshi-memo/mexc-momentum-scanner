# Decision Report

- generated_at: 2026-07-15T15:11:24.505491+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8752**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8752, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +3.13% | **+0.94%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.91% | **+0.45%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |
| MARKET_LONG | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.88% | **+0.62%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.75% | **+0.56%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.35% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 98件 (TP 34 / SL 62 / EXP 2)
- 最新: MAGMA/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$340.92** / 初期 $100.00 (+240.92%)
- 確定: 2880件 (Win 901 / Loss 936 / Flat 1043) / skip 2433件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 0G/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $340.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.77** / 初期 $100.00 (+5.77%)
- 確定: 716件 (Win 167 / Loss 167 / Flat 382) / skip 1447件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1167 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DODO/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $105.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 62件 (Win 19 / Loss 39 / Flat 4) / pending 2件 / skip 161件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000316 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAVE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-15T15:11:14.076141+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=65375.8
- Funnel: target 871 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +331.75% | $31,626,043.96 |
| DODO/USDT:USDT | +49.56% | $13,160,936.74 |
| US/USDT:USDT | +39.08% | $7,300,032.98 |
| AEHRSTOCK/USDT:USDT | +29.78% | $6,557,554.74 |
| RAVE/USDT:USDT | +19.74% | $4,953,246.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CCLSTOCK/USDT:USDT | below_1h_threshold | +1.84% | +1.82% |
| FLUTSTOCK/USDT:USDT | below_1h_threshold | +1.79% | +1.77% |
| RAVE/USDT:USDT | below_1h_threshold | +1.71% | +1.70% |
| METASTOCK/USDT:USDT | below_1h_threshold | +1.71% | +1.69% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.21% | +1.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
