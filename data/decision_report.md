# Decision Report

- generated_at: 2026-09-16T12:36:25.433071+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14691**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14691, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.20% | **-1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.67% | **+0.67%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +2.45% | **+2.33%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.70% | **+2.16%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.02% | **+1.92%** |
| LIMIT_BB3S_LONG | 5/10 | 50.0% | +2.63% | **+1.31%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.41% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,137.93** / 初期 $100.00 (+1037.93%)
- 確定: 5568件 (Win 1666 / Loss 1800 / Flat 2102) / skip 5684件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,137.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$236.37** / 初期 $100.00 (+136.37%)
- 確定: 3095件 (Win 855 / Loss 731 / Flat 1509) / skip 5007件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1612 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $236.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.75** / 初期 $100.00 (+23.75%)
- 確定: 2955件 (Win 878 / Loss 1164 / Flat 913) / pending 1件 / skip 3206件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000356 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.75

## 6. Latest Market Context

- 更新: 2026-09-16T12:36:14.981149+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=75960.7
- Funnel: target 1058 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +110.53% | $22,152,563.95 |
| BR/USDT:USDT | +109.89% | $27,017,560.41 |
| LSK/USDT:USDT | +58.91% | $26,532,923.71 |
| BULLA/USDT:USDT | +44.01% | $2,442,046.17 |
| USELESS/USDT:USDT | +15.03% | $7,856,887.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +3.61% | +3.93% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.69% | +2.02% |
| CNPY/USDT:USDT | below_1h_threshold | +1.22% | +1.54% |
| KORU/USDT:USDT | below_1h_threshold | +1.14% | +1.46% |
| ARB/USDT:USDT | below_1h_threshold | +1.09% | +1.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
