# Decision Report

- generated_at: 2026-07-22T09:36:34.911277+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9268**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9268, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/14 | 21.4% | +5.13% | **+1.10%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.68% | **+1.01%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.60% | **+1.12%** |
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.33% | **+0.80%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.05% | **+0.53%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.82% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$426.72** / 初期 $100.00 (+326.72%)
- 確定: 3266件 (Win 1029 / Loss 1047 / Flat 1190) / skip 2563件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $426.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1519件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1495 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定: 408件 (Win 140 / Loss 168 / Flat 100) / pending 6件 / skip 329件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000509 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $102.36

## 6. Latest Market Context

- 更新: 2026-07-22T09:36:24.785123+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=65874.0
- Funnel: target 888 → liquid 176 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +49.10% | $3,337,254.03 |
| RE/USDT:USDT | +26.90% | $6,101,831.02 |
| SMCISTOCK/USDT:USDT | +18.47% | $4,340,584.53 |
| UB/USDT:USDT | +13.19% | $1,171,672.59 |
| BNCSTOCK/USDT:USDT | +12.35% | $2,920,376.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TLM/USDT:USDT | below_1h_threshold | +4.97% | +5.09% |
| PONS/USDT:USDT | below_1h_threshold | +4.41% | +4.53% |
| RE/USDT:USDT | below_1h_threshold | +3.61% | +3.73% |
| PLAY/USDT:USDT | below_1h_threshold | +1.96% | +2.08% |
| UB/USDT:USDT | below_1h_threshold | +1.91% | +2.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
