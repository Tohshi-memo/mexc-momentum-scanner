# Decision Report

- generated_at: 2026-09-16T16:46:33.032217+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14720**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14720, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +4.54% | **+1.36%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.54% | **+0.92%** |
| LIMIT_ATR | 8/20 | 40.0% | +1.73% | **+0.69%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.31% | **+1.12%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,183.26** / 初期 $100.00 (+1083.26%)
- 確定: 5596件 (Win 1679 / Loss 1810 / Flat 2107) / skip 5685件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,183.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$244.99** / 初期 $100.00 (+144.99%)
- 確定: 3124件 (Win 870 / Loss 741 / Flat 1513) / skip 5007件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1796 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $244.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2956件 (Win 878 / Loss 1165 / Flat 913) / pending 0件 / skip 3236件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000461 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-16T16:46:18.838418+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=75711.1
- Funnel: target 1059 → liquid 150 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.3 >= 65=1, 4h RSI 77.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +23.33% | $4,821,209.99 |
| LSK/USDT:USDT | +13.51% | $33,643,310.08 |
| CNPY/USDT:USDT | +6.17% | $1,463,513.57 |
| SAGA/USDT:USDT | +3.88% | $7,599,016.94 |
| LONGXIA/USDT:USDT | +3.83% | $2,752,481.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +3.88% | +3.94% |
| LONGXIA/USDT:USDT | below_1h_threshold | +3.84% | +3.90% |
| REZ/USDT:USDT | below_1h_threshold | +3.34% | +3.40% |
| HEI/USDT:USDT | below_1h_threshold | +2.29% | +2.35% |
| BEAT/USDT:USDT | below_1h_threshold | +2.29% | +2.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
