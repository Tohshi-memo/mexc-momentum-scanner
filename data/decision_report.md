# Decision Report

- generated_at: 2026-08-30T03:51:22.384940+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13005**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13005, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.06% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +5.60% | **+2.80%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +3.43% | **+2.57%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +3.38% | **+2.20%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.41% | **+1.13%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$789.05** / 初期 $100.00 (+689.05%)
- 確定: 4775件 (Win 1457 / Loss 1572 / Flat 1746) / skip 4791件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $789.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$172.79** / 初期 $100.00 (+72.79%)
- 確定: 2089件 (Win 584 / Loss 508 / Flat 997) / skip 4327件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1237 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $172.79

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.63** / 初期 $100.00 (+16.63%)
- 確定: 2052件 (Win 604 / Loss 798 / Flat 650) / pending 5件 / skip 2424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000519 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.63

## 6. Latest Market Context

- 更新: 2026-08-30T03:51:12.767931+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=78119.7
- Funnel: target 1023 → liquid 118 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.9 >= 65=1, 4h RSI 84.3 >= 65=1, 4h RSI 87.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +67.48% | $2,003,005.61 |
| HNT/USDT:USDT | +43.89% | $27,483,778.66 |
| PONS/USDT:USDT | +42.22% | $1,449,610.46 |
| FONE/USDT:USDT | +32.85% | $1,305,748.11 |
| PROM/USDT:USDT | +32.56% | $13,741,255.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +3.71% | +3.65% |
| O/USDT:USDT | below_1h_threshold | +3.00% | +2.94% |
| DEXE/USDT:USDT | below_1h_threshold | +2.28% | +2.22% |
| BICO/USDT:USDT | below_1h_threshold | +2.03% | +1.97% |
| CYS/USDT:USDT | below_1h_threshold | +1.58% | +1.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
