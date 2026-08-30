# Decision Report

- generated_at: 2026-08-30T04:51:23.585007+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13016**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13016, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.75% | **-1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 16/20 | 80.0% | +1.25% | **+1.00%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.97% | **+0.89%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.09% | **+0.63%** |
| LIMIT_BB3S | 9/15 | 60.0% | +0.72% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +4.54% | **+2.95%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +5.10% | **+2.80%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.32% | **+2.16%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.98% | **+1.79%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.53% | **+1.22%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.09** / 初期 $100.00 (+692.09%)
- 確定: 4786件 (Win 1460 / Loss 1575 / Flat 1751) / skip 4791件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $792.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$172.71** / 初期 $100.00 (+72.71%)
- 確定: 2100件 (Win 588 / Loss 513 / Flat 999) / skip 4327件
- 成長率目線: 平均log +0.000260 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0386 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $172.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.33** / 初期 $100.00 (+17.33%)
- 確定: 2060件 (Win 607 / Loss 800 / Flat 653) / pending 4件 / skip 2425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000444 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.33

## 6. Latest Market Context

- 更新: 2026-08-30T04:51:13.884034+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=77979.9
- Funnel: target 1023 → liquid 119 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 89.0 >= 65=1, 4h RSI 87.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +62.38% | $2,443,194.46 |
| FONE/USDT:USDT | +61.74% | $1,359,315.36 |
| HNT/USDT:USDT | +59.32% | $29,327,499.34 |
| PONS/USDT:USDT | +44.40% | $1,513,727.51 |
| PROM/USDT:USDT | +31.55% | $14,449,815.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.97% | +5.13% |
| MOVR/USDT:USDT | below_1h_threshold | +3.43% | +3.59% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.87% | +2.03% |
| VET/USDT:USDT | below_1h_threshold | +1.43% | +1.59% |
| TUT/USDT:USDT | below_1h_threshold | +1.17% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
