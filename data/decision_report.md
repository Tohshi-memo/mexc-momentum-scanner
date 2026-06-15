# Decision Report

- generated_at: 2026-06-15T06:48:42.227180+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6755**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6755, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.54% | **+0.16%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.04% | **-0.02%** |
| LIMIT_6PCT | 6/20 | 30.0% | -0.08% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +2.97% | **+2.52%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +3.93% | **+2.25%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +2.82% | **+2.12%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.80% | **+1.53%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.00% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$175.36** / 初期 $100.00 (+75.36%)
- 確定: 1628件 (Win 426 / Loss 504 / Flat 698) / skip 1688件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $175.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.23** / 初期 $100.00 (-0.77%)
- 確定: 122件 (Win 25 / Loss 20 / Flat 77) / skip 44件
- 成長率目線: 平均log -0.000063 / 幾何平均 -0.006% per trade / maxDD +2.07%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score +0.0550 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $99.23

## 5. Latest Market Context

- 更新: 2026-06-15T06:48:37.745100+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=65816.5
- Funnel: target 770 → liquid 142 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.8 >= 65=1, 4h RSI 90.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +84.61% | $3,593,947.76 |
| EVAA/USDT:USDT | +59.58% | $22,147,608.56 |
| CLO/USDT:USDT | +45.87% | $2,193,506.69 |
| JELLYJELLY/USDT:USDT | +24.72% | $1,531,314.21 |
| GRASS/USDT:USDT | +22.76% | $1,623,493.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +4.76% | +4.78% |
| JTO/USDT:USDT | below_1h_threshold | +2.72% | +2.74% |
| TAO/USDT:USDT | below_1h_threshold | +2.63% | +2.65% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.15% | +2.17% |
| EDEN/USDT:USDT | below_1h_threshold | +2.09% | +2.11% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
