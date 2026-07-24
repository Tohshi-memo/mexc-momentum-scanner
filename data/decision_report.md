# Decision Report

- generated_at: 2026-07-24T05:36:13.612327+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9414**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9414, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.13% | **+0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| MARKET | 20/20 | 100.0% | +0.13% | **+0.13%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.21% | **-0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.86% | **+1.58%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.05% | **+1.43%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.84% | **+0.75%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.96% | **+0.53%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$425.48** / 初期 $100.00 (+325.48%)
- 確定: 3323件 (Win 1048 / Loss 1076 / Flat 1199) / skip 2652件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $425.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1163件 (Win 312 / Loss 254 / Flat 597) / skip 1662件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1248 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BILL/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.25** / 初期 $100.00 (+2.25%)
- 確定: 475件 (Win 158 / Loss 188 / Flat 129) / pending 2件 / skip 406件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000451 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $102.25

## 6. Latest Market Context

- 更新: 2026-07-24T05:36:06.551861+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=65255.1
- Funnel: target 897 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +35.24% | $9,959,471.44 |
| RE/USDT:USDT | +21.02% | $14,363,540.28 |
| BILL/USDT:USDT | +19.82% | $9,654,082.80 |
| AKE/USDT:USDT | +17.14% | $28,025,487.89 |
| ON/USDT:USDT | +13.97% | $6,046,954.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +4.68% | +4.72% |
| CAP/USDT:USDT | below_1h_threshold | +3.65% | +3.69% |
| US/USDT:USDT | below_1h_threshold | +3.06% | +3.11% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.93% | +1.97% |
| BILL/USDT:USDT | below_1h_threshold | +1.82% | +1.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
