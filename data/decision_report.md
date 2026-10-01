# Decision Report

- generated_at: 2026-10-01T17:31:28.638510+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15928**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15928, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.05% | **-0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +3.12% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.46% | **+1.85%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.86% | **+1.21%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.40% | **+0.84%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.88% | **+0.84%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.82% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 226件 (TP 82 / SL 137 / EXP 7)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,296.15** / 初期 $100.00 (+1196.15%)
- 確定: 6037件 (Win 1789 / Loss 1945 / Flat 2303) / skip 6452件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,296.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.87** / 初期 $100.00 (+177.87%)
- 確定: 3581件 (Win 998 / Loss 829 / Flat 1754) / skip 5758件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.029% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1310 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $277.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4091件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000287 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T17:31:14.727137+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.98% price=84990.0
- Funnel: target 1097 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNXX/USDT:USDT | +6.81% | $5,600,055.64 |
| US/USDT:USDT | +6.63% | $1,531,370.02 |
| KORU/USDT:USDT | +5.19% | $27,412,834.36 |
| MUU/USDT:USDT | +5.08% | $19,151,089.08 |
| MONAD/USDT:USDT | +4.75% | $11,421,358.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_relative_strength | +5.67% | +4.70% |
| GRASS/USDT:USDT | below_1h_threshold | +4.88% | +3.90% |
| MONAD/USDT:USDT | below_1h_threshold | +4.87% | +3.89% |
| WIF/USDT:USDT | below_1h_threshold | +4.79% | +3.81% |
| VVV/USDT:USDT | below_1h_threshold | +3.76% | +2.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
