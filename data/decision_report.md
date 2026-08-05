# Decision Report

- generated_at: 2026-08-05T09:26:38.148829+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10384**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10384, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.01% | **-2.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.15% | **+0.12%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.14% | **+0.11%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.21% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.99% | **+2.99%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.71% | **+1.48%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.49% | **+1.37%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.40% | **+1.32%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.74% | **+1.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$614.48** / 初期 $100.00 (+514.48%)
- 確定: 3766件 (Win 1195 / Loss 1233 / Flat 1338) / skip 3179件
- 成長率目線: 平均log +0.000482 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HFT/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $614.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.75** / 初期 $100.00 (+43.75%)
- 確定: 1314件 (Win 371 / Loss 309 / Flat 634) / skip 2481件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1468 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $143.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.20** / 初期 $100.00 (+19.20%)
- 確定: 1129件 (Win 364 / Loss 435 / Flat 330) / pending 6件 / skip 726件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000418 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $119.20

## 6. Latest Market Context

- 更新: 2026-08-05T09:26:26.870319+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=64134.7
- Funnel: target 944 → liquid 182 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.7 >= 65=1, 4h RSI 80.6 >= 65=1, 4h RSI 86.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HFT/USDT:USDT | +82.11% | $2,850,204.20 |
| BLESS/USDT:USDT | +78.73% | $34,073,246.97 |
| HEI/USDT:USDT | +62.16% | $18,612,410.84 |
| BICO/USDT:USDT | +37.84% | $16,833,057.57 |
| SYN/USDT:USDT | +25.96% | $3,891,728.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 1000RATS/USDT:USDT | below_1h_threshold | +2.68% | +2.62% |
| PI/USDT:USDT | below_1h_threshold | +1.79% | +1.74% |
| BLESS/USDT:USDT | below_1h_threshold | +1.79% | +1.73% |
| RE/USDT:USDT | below_1h_threshold | +1.69% | +1.63% |
| SKR/USDT:USDT | below_1h_threshold | +1.24% | +1.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
