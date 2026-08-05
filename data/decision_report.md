# Decision Report

- generated_at: 2026-08-05T10:06:37.539849+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10390**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10390, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.36% | **+0.89%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.64% | **+0.54%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.41% | **+0.27%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_BB3S | 6/19 | 31.6% | +0.70% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.99% | **+0.49%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.03% | **+0.46%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.82% | **+0.45%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.30% | **+0.19%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$611.41** / 初期 $100.00 (+511.41%)
- 確定: 3767件 (Win 1195 / Loss 1234 / Flat 1338) / skip 3184件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $611.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.75** / 初期 $100.00 (+43.75%)
- 確定: 1314件 (Win 371 / Loss 309 / Flat 634) / skip 2487件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0983 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $143.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.78** / 初期 $100.00 (+18.78%)
- 確定: 1132件 (Win 364 / Loss 437 / Flat 331) / pending 4件 / skip 727件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000285 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.78

## 6. Latest Market Context

- 更新: 2026-08-05T10:06:26.462073+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64157.6
- Funnel: target 945 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +77.79% | $35,935,347.89 |
| HEI/USDT:USDT | +73.50% | $19,593,283.43 |
| HFT/USDT:USDT | +63.23% | $3,218,543.70 |
| SYN/USDT:USDT | +30.11% | $4,238,403.00 |
| GRVT/USDT:USDT | +29.78% | $6,904,297.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +4.48% | +4.43% |
| UAI/USDT:USDT | below_1h_threshold | +3.54% | +3.50% |
| GRVT/USDT:USDT | below_1h_threshold | +2.99% | +2.94% |
| CYS/USDT:USDT | below_1h_threshold | +2.79% | +2.75% |
| SKR/USDT:USDT | below_1h_threshold | +2.27% | +2.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
