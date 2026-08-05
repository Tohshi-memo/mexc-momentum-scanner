# Decision Report

- generated_at: 2026-08-05T10:11:34.221638+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10391**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10391, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.45% | **+0.94%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.64% | **+0.54%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.41% | **+0.27%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_BB3S | 5/19 | 26.3% | +0.70% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.99% | **+0.49%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.03% | **+0.46%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.82% | **+0.45%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.30% | **+0.19%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.19% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$611.41** / 初期 $100.00 (+511.41%)
- 確定: 3767件 (Win 1195 / Loss 1234 / Flat 1338) / skip 3185件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $611.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.85** / 初期 $100.00 (+43.85%)
- 確定: 1315件 (Win 372 / Loss 309 / Flat 634) / skip 2487件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1079 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $143.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.78** / 初期 $100.00 (+18.78%)
- 確定: 1132件 (Win 364 / Loss 437 / Flat 331) / pending 5件 / skip 727件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000349 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.78

## 6. Latest Market Context

- 更新: 2026-08-05T10:11:25.048498+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64094.9
- Funnel: target 945 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +78.56% | $36,530,911.60 |
| HEI/USDT:USDT | +77.93% | $19,813,171.17 |
| HFT/USDT:USDT | +64.43% | $3,232,164.86 |
| BICO/USDT:USDT | +28.89% | $16,722,105.69 |
| GRVT/USDT:USDT | +27.44% | $6,928,459.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKR/USDT:USDT | below_1h_threshold | +3.75% | +3.80% |
| EVAA/USDT:USDT | below_1h_threshold | +3.52% | +3.57% |
| CYS/USDT:USDT | below_1h_threshold | +3.36% | +3.41% |
| UAI/USDT:USDT | below_1h_threshold | +2.51% | +2.56% |
| CAP/USDT:USDT | below_1h_threshold | +1.76% | +1.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
