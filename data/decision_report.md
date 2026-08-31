# Decision Report

- generated_at: 2026-08-31T00:06:15.605191+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13114**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13114, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.17% | **-0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +0.90% | **+0.63%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_BB3S | 5/20 | 25.0% | +1.67% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.22% | **+0.92%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.82% | **+0.91%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.33% | **+0.70%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$782.69** / 初期 $100.00 (+682.69%)
- 確定: 4846件 (Win 1474 / Loss 1596 / Flat 1776) / skip 4829件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $782.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.14** / 初期 $100.00 (+73.14%)
- 確定: 2167件 (Win 601 / Loss 528 / Flat 1038) / skip 4358件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0900 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZORA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $173.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.89** / 初期 $100.00 (+15.89%)
- 確定: 2083件 (Win 610 / Loss 812 / Flat 661) / pending 0件 / skip 2499件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000236 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.89

## 6. Latest Market Context

- 更新: 2026-08-31T00:06:06.055215+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=77724.0
- Funnel: target 1026 → liquid 136 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKR/USDT:USDT | +46.19% | $17,781,338.78 |
| BASECAT/USDT:USDT | +34.18% | $1,263,249.83 |
| HEMI/USDT:USDT | +32.29% | $2,539,856.03 |
| FONE/USDT:USDT | +27.06% | $1,813,386.35 |
| PONS/USDT:USDT | +12.49% | $2,252,027.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +3.67% | +3.56% |
| HEMI/USDT:USDT | below_1h_threshold | +2.03% | +1.92% |
| AUCTION/USDT:USDT | below_1h_threshold | +1.54% | +1.43% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.52% | +1.41% |
| O/USDT:USDT | below_1h_threshold | +1.46% | +1.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
